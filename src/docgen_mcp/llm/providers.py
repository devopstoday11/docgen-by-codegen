"""
LLM Provider implementations.

This module contains the base provider interface and factory for creating
provider instances.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from .models import LLMModel, LLMResponse
from .config import LLMConfig


class LLMProvider(ABC):
    """Base class for all LLM providers."""
    
    def __init__(self, config: LLMConfig):
        """Initialize the provider with configuration."""
        self.config = config
    
    @abstractmethod
    async def generate(
        self, 
        prompt: str, 
        model: Optional[str] = None,
        **kwargs: Any
    ) -> LLMResponse:
        """Generate a response from the LLM."""
        pass
    
    @abstractmethod
    async def list_models(self) -> List[LLMModel]:
        """List available models for this provider."""
        pass


class LLMProviderFactory:
    """Factory for creating LLM provider instances."""
    
    _providers: Dict[str, type] = {}
    
    @classmethod
    def register_provider(cls, name: str, provider_class: type) -> None:
        """Register a provider class."""
        cls._providers[name] = provider_class
    
    @classmethod
    def create_provider(cls, name: str, config: LLMConfig) -> LLMProvider:
        """Create a provider instance."""
        if name not in cls._providers:
            raise ValueError(f"Unknown provider: {name}")
        
        return cls._providers[name](config)
    
    @classmethod
    def list_providers(cls) -> List[str]:
        """List available provider names."""
        return list(cls._providers.keys())
