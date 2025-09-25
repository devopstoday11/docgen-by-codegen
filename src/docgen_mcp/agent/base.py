"""
Base Agent class.

This module contains the base agent interface that all agents inherit from.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseAgent(ABC):
    """Base class for all agents in the DocGen MCP system."""
    
    def __init__(self, name: str, **kwargs: Any):
        """Initialize the agent."""
        self.name = name
        self.config = kwargs
    
    @abstractmethod
    async def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Any:
        """Execute a task."""
        pass
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the agent."""
        pass
    
    async def shutdown(self) -> None:
        """Shutdown the agent."""
        pass
