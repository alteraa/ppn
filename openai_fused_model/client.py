
from typing import Any, Mapping, Optional, Union, List
import httpx
from openai import OpenAI, AsyncOpenAI
from openai._types import NOT_GIVEN, NotGiven
from openai._utils import is_given
from pydantic import BaseModel
from functools import cached_property

from .manager import MultiModelManager

class FusedCompletions:
    def __init__(self, client: "FusedClient"):
        self._client = client

    def create(self, **kwargs):
        """
        Create a completion by routing to the appropriate client via the manager.
        """
        # Delegate directly to the manager's functionality
        return self._client.manager.create(**kwargs)


class FusedChat:
    def __init__(self, client: "FusedClient"):
        self.completions = FusedCompletions(client)

class FusedClient(OpenAI):
    """
    A unified client that manages multiple OpenAI-compatible clients.
    It inherits from OpenAI to maintain type compatibility but overrides
    functionality to route requests to different underlying clients.
    """
    
    def __init__(
        self,
        *,
        clients: List[OpenAI],
        model_names: Optional[List[str]] = None,
        manager: Optional[Any] = None, # Type Any to avoid circular imports during refactor
        **kwargs: Any,
    ) -> None:
        """
        Initialize the FusedClient.
        
        Args:
            clients: List of OpenAI client instances to manage.
            manager: Optional pre-configured MultiModelManager. 
                     If not provided, one will be created from the clients.
            **kwargs: Arguments passed to the base OpenAI class (mostly ignored/placeholder).
        """
        # Extract specific params for MultiModelManager from kwargs
        strategy = kwargs.pop('strategy', 'priority')
        model_configs = kwargs.pop('model_configs', None)
        default_fallback = kwargs.pop('default_fallback', True)
        
        # Support 'models' as an alias for 'model_names' if it's a list of strings
        if model_names is None and 'models' in kwargs and isinstance(kwargs['models'], list):
            if all(isinstance(m, str) for m in kwargs['models']):
                model_names = kwargs.pop('models')

        # We initialize the base class with dummy values because we won't use its connection pool directly
        # for multiple clients.
        super().__init__(api_key="dummy", **kwargs)

        # We will need a manager to handle the logic. 
        # If the user passed a MultiModelManager (refactored version), use it.
        # Otherwise, we might need to construct one.
        if manager:
            self._manager = manager
        else:
            from .manager import MultiModelManager
            self._manager = MultiModelManager(
                models=clients, 
                strategy=strategy,
                model_configs=model_configs,
                default_fallback=default_fallback,
                model_names=model_names
            )


    @cached_property
    def chat(self) -> FusedChat:
        return FusedChat(self)


    @property
    def manager(self):
        return self._manager

# We can also implement AsyncFusedClient similarly if needed, but for now we focus on sync.
