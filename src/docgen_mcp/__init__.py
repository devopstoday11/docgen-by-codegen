"""
DocGen MCP - AI-powered code documentation generator with MCP server integration.

This package provides a comprehensive solution for generating high-quality
documentation from codebases using AI agents and MCP (Model Context Protocol) servers.

Key Features:
- Multi-LLM provider support (OpenAI, Anthropic, Google, Ollama, etc.)
- Hierarchical documentation structure matching codebase organization
- Mermaid.js diagram generation with CLI integration
- Obsidian-like knowledge base with wikilinks and backlinks
- Advanced code analysis using tree-sitter and universal ctags
- Plugin architecture for extensibility
- MCP server integration for tool calling
- Agentic approach with sub-agents for specialized tasks

Version: 0.1.0
Author: Codegen AI
License: MIT
"""

__version__ = "0.1.0"
__author__ = "Codegen AI"
__email__ = "ai@codegen.com"
__license__ = "MIT"

# Core exports
from .config import DocGenConfig
from .core import DocGenMCP

__all__ = [
    "__version__",
    "__author__", 
    "__email__",
    "__license__",
    "DocGenConfig",
    "DocGenMCP",
]
