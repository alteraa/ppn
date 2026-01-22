
"""Core MultiModelManager class for managing multiple OpenAI client instances."""

import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Optional, Union, List, Dict

from pydantic import BaseModel, PrivateAttr
from openai import OpenAI

# Set up logger
logger = logging.getLogger(__name__)


@dataclass
class ModelConfig:
    """Configuration for a managed OpenAI client instance.

    Attributes:
        priority: Priority level for the model (higher = more preferred). Default is 0.
        max_rpm: Maximum requests per minute allowed for this model.
        max_rps: Maximum requests per second allowed for this model.
        cost_per_1k_tokens: Cost in dollars per 1000 tokens for pricing strategy.
        timeout: Request timeout in seconds.
        retry_on_errors: List of exception types that should trigger retry/fallback.
    """

    priority: int = 0
    max_rpm: Optional[int] = None
    max_rps: Optional[int] = None
    cost_per_1k_tokens: float = 0.0
    timeout: Optional[float] = None
    retry_on_errors: list[type[Exception]] = field(default_factory=list)
    model: Optional[str] = None


class MultiModelManager:
    """Manages multiple OpenAI client instances with intelligent routing and fallback."""

    def __init__(
        self,
        models: List[OpenAI],
        model_configs: Optional[List[ModelConfig]] = None,
        strategy: Union[str, Callable] = "priority",
        default_fallback: bool = True,
        **kwargs: Any,
    ):
        """Initialize the MultiModelManager.

        Args:
            models: List of OpenAI client instances to manage.
            model_configs: Optional list of ModelConfig objects, one per model.
                If not provided, default configurations will be created.
            strategy: Routing strategy to use. Can be a string ("priority",
                "round_robin", "least_used", "cost_aware") or a custom callable.
                Default is "priority".
            default_fallback: Whether to enable automatic fallback on errors.
                Default is True.
            **kwargs: Additional configuration (e.g., model_names as 'models' list of strings).

        Raises:
            ValueError: If models list is empty or if model_configs length
                doesn't match models length.
        """
        if not models:
            raise ValueError("At least one model must be provided")

        self.models = models
        self.strategy = strategy
        self.default_fallback = default_fallback
        
        # Shorthand for model names if provided via kwargs['models'] or just 'models' argument
        # Note: 'models' argument is already taken by the list of OpenAI clients.
        # So we use kwargs.get('model_names') or similar?
        # The user's request suggests they want to 'select models'.
        model_names = kwargs.get('model_names')

        # Create default configs if not provided
        if model_configs is None:
            self.model_configs = [ModelConfig() for _ in models]
            if model_names:
                if len(model_names) != len(models):
                     raise ValueError(
                        f"Number of model_names ({len(model_names)}) must match "
                        f"number of models ({len(models)})"
                    )
                for i, name in enumerate(model_names):
                    self.model_configs[i].model = name
        else:
            if len(model_configs) != len(models):
                raise ValueError(
                    f"Number of model_configs ({len(model_configs)}) must match "
                    f"number of models ({len(models)})"
                )
            self.model_configs = model_configs
            if model_names:
                if len(model_names) != len(models):
                    raise ValueError(
                        f"Number of model_names ({len(model_names)}) must match "
                        f"number of models ({len(models)})"
                    )
                for i, name in enumerate(model_names):
                    self.model_configs[i].model = name

        # Initialize internal components
        from .rate_limiter import RateLimiter
        from .strategy import StrategySelector
        from .usage_tracker import UsageTracker

        self._usage_tracker = UsageTracker()
        self._rate_limiter = RateLimiter()
        self._strategy_selector = StrategySelector()

    def _select_model(self, model_name: Optional[str] = None) -> tuple[OpenAI, int]:
        """Select a model based on strategy and availability."""
        from .exceptions import RateLimitExceededError

        # Filter available models based on rate limits
        available_models = []
        for idx, config in enumerate(self.model_configs):
            # Check model compatibility
            if model_name and config.model and config.model != model_name:
                continue
                
            if self._rate_limiter.is_available(idx, config):
                available_models.append(idx)

        # Check if any models are available
        if not available_models:
            logger.warning("All models are currently rate limited or unavailable")
            raise RateLimitExceededError("All models are currently rate limited or unavailable")

        # Get usage statistics for strategy selection
        usage_stats = self._usage_tracker.get_all_stats()

        # Use strategy selector to choose model
        # Note: Strategy logic might need adjustment if it depended on LangChain model attrs.
        # Assuming strategy.py uses indices mostly, or we fix it later.
        selected_idx = self._strategy_selector.select(
            strategy=self.strategy,
            models=self.models,
            configs=self.model_configs,
            usage_stats=usage_stats,
            available_models=available_models,
        )

        selected_model = self.models[selected_idx]

        logger.debug(
            f"Selected model {selected_idx} using strategy {self.strategy}"
        )

        return selected_model, selected_idx

    def create(self, **kwargs: Any) -> Any:
        """
        Execute a completion request (create) with routing and fallback.
        This mimics openai.chat.completions.create but routes to managed clients.
        """
        
        # We assume kwargs are valid for client.chat.completions.create
        
        from .exceptions import AllModelsFailedError

        tried_models = set()
        errors = {}
        
        
        # Initial model selection
        try:
             # We might need to retry selection if the first selected one fails immediately due to internal checks
             # But _select_model already checks rate limits.
            model_name = kwargs.get('model')
            selected_model, current_idx = self._select_model(model_name=model_name)
        except Exception as e:
            # If we can't select any model initially
            raise
        
        # Loop for fallback
        while True:
            tried_models.add(current_idx)
            model = self.models[current_idx]
            config = self.model_configs[current_idx]
            
            try:
                logger.debug(f"Attempting request with model {current_idx}")
                # Prepare kwargs for the actual call
                call_kwargs = kwargs.copy()
                
                # If model is not in kwargs, try to get it from config
                if ('model' not in call_kwargs or call_kwargs['model'] is None) and config.model:
                    call_kwargs['model'] = config.model
                    
                # Record the request for rate limiting
                self._rate_limiter.record_request(current_idx)
                
                # Perform the actual API call
                # Note: We are assuming all models are OpenAI clients
                result = model.chat.completions.create(**call_kwargs)
                
                # Success
                # Attempt to track usage if available in result
                tokens = 0
                if hasattr(result, 'usage') and result.usage:
                     tokens = result.usage.total_tokens
                
                self._usage_tracker.record_request(current_idx, success=True, tokens=tokens)
                logger.info(f"Successfully completed request with model {current_idx}")
                
                return result

            except Exception as e:
                # Failure
                self._usage_tracker.record_request(current_idx, success=False)
                
                errors[current_idx] = {
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                }
                logger.warning(f"Model {current_idx} failed: {e}")
                
                should_retry = False
                # Simple error classification
                error_str = str(e).lower()
                if "rate limit" in error_str or "429" in str(e):
                    logger.info(f"Rate limit for model {current_idx}")
                    self._rate_limiter.set_cooldown(current_idx, 60.0)
                    should_retry = True
                elif "timeout" in error_str:
                    logger.info(f"Timeout detected for model {current_idx}")
                    should_retry = True
                elif "connection" in error_str:
                     logger.info(f"Connection error detected for model {current_idx}")
                     should_retry = True
                elif config.retry_on_errors:
                    for err_type in config.retry_on_errors:
                         if isinstance(e, err_type):
                             should_retry = True
                             break
                
                if not self.default_fallback or not should_retry:
                    raise
                
                # Try to select next model from UNTRIED ones
                # _select_model might pick the same one if we don't mark it unavailable enough?
                # Actually _select_model filters by rate limit availability.
                # If we just failed with non-rate-limit error but want to skip it, we need to handle that.
                
                # For this simplified logic, we'll try to get another model.
                # Ideally, we should exclude 'tried_models' from selection.
                
                # Let's do a manual selection loop over available models avoiding tried ones
                
                try:
                    # Get fresh available models
                     # Filter available models based on rate limits
                    available_models = []
                    model_name = kwargs.get('model')
                    for idx, conf in enumerate(self.model_configs):
                        # Check model compatibility
                        if model_name and conf.model and conf.model != model_name:
                            continue
                            
                        if idx not in tried_models and self._rate_limiter.is_available(idx, conf):
                            available_models.append(idx)
                    
                    if not available_models:
                         logger.error("No more models available for fallback")
                         break
                         
                    # Use strategy to pick best among remaining
                    usage_stats = self._usage_tracker.get_all_stats()
                    next_idx = self._strategy_selector.select(
                        strategy=self.strategy,
                        models=self.models,
                        configs=self.model_configs,
                        usage_stats=usage_stats,
                        available_models=available_models,
                    )
                    
                    current_idx = next_idx
                    
                except Exception as ex:
                    logger.error(f"Fallback selection failed: {ex}")
                    break

        raise AllModelsFailedError(
            errors=errors,
            message=f"All {len(tried_models)} tried models failed. Errors: {errors}"
        )

