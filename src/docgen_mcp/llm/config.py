"""
LLM Configuration.

This module contains configuration classes for LLM providers.
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    """Configuration for LLM providers."""
    
    provider: str = Field(..., description="Provider name")
    model: str = Field(..., description="Model name")
    api_key: Optional[str] = Field(None, description="API key")
    base_url: Optional[str] = Field(None, description="Base URL for API")
    temperature: float = Field(0.7, description="Temperature for generation")
    max_tokens: int = Field(4000, description="Maximum tokens for generation")
    timeout: int = Field(60, description="Request timeout in seconds")
    extra_params: Dict[str, Any] = Field(default_factory=dict, description="Additional parameters")
