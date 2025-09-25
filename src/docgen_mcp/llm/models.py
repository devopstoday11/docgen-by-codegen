"""
LLM Model data structures.

This module contains data models for representing LLM models and responses.
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class LLMModel(BaseModel):
    """Represents an LLM model."""
    
    name: str = Field(..., description="Model name")
    provider: str = Field(..., description="Provider name")
    description: Optional[str] = Field(None, description="Model description")
    max_tokens: Optional[int] = Field(None, description="Maximum context length")
    supports_functions: bool = Field(False, description="Supports function calling")
    supports_vision: bool = Field(False, description="Supports vision/image input")


class LLMUsage(BaseModel):
    """Token usage information."""
    
    prompt_tokens: int = Field(0, description="Tokens in the prompt")
    completion_tokens: int = Field(0, description="Tokens in the completion")
    total_tokens: int = Field(0, description="Total tokens used")


class LLMResponse(BaseModel):
    """Response from an LLM."""
    
    content: str = Field(..., description="Generated content")
    model: str = Field(..., description="Model used for generation")
    usage: Optional[LLMUsage] = Field(None, description="Token usage information")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
