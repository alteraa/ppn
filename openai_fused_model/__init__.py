
"""
langchain-fused-model: Intelligent routing and management for multiple OpenAI Client instances.
"""

__version__ = "0.1.2"

from .client import FusedClient
from .exceptions import (
    AllModelsFailedError,
    MultiModelError,
    RateLimitExceededError,
    StructuredOutputError,
)
from .manager import ModelConfig, MultiModelManager
from .rate_limiter import RateLimiter
from .strategy import RoutingStrategy, StrategySelector
from .usage_tracker import UsageStats, UsageTracker

__all__ = [
    "FusedClient",
    "MultiModelManager",
    "ModelConfig",
    "RoutingStrategy",
    "StrategySelector",
    "UsageTracker",
    "UsageStats",
    "RateLimiter",
    "RateLimiter",
    "MultiModelError",
    "AllModelsFailedError",
    "RateLimitExceededError",
    "StructuredOutputError",
]
