"""
Agent System Module.

This module implements the agentic architecture for documentation generation,
including main agents and specialized sub-agents for different tasks.

Features:
- Deep agent architecture inspired by deepagents
- Sub-agent spawning for specialized tasks
- Planning and task management
- Memory and context management
- Tool calling and MCP integration
"""

from .base import BaseAgent
from .deep_agent import DeepDocAgent
from .sub_agents import SubAgentFactory
from .planning import PlanningAgent
from .memory import AgentMemory

__all__ = [
    "BaseAgent",
    "DeepDocAgent",
    "SubAgentFactory",
    "PlanningAgent", 
    "AgentMemory",
]
