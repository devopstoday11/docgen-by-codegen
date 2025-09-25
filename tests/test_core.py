"""
Tests for the core DocGenMCP class.

This module contains tests for the main DocGenMCP orchestration class.
"""

import pytest
from pathlib import Path
from docgen_mcp.core import DocGenMCP
from docgen_mcp.config import DocGenConfig


class TestDocGenMCP:
    """Tests for DocGenMCP class."""
    
    def test_create_docgen_mcp_default_config(self):
        """Test creating DocGenMCP with default configuration."""
        docgen = DocGenMCP()
        
        assert docgen.config is not None
        assert isinstance(docgen.config, DocGenConfig)
        assert docgen._initialized is False
    
    def test_create_docgen_mcp_custom_config(self):
        """Test creating DocGenMCP with custom configuration."""
        config = DocGenConfig(
            project_name="Test Project",
            project_path=Path("/test/project")
        )
        
        docgen = DocGenMCP(config=config)
        
        assert docgen.config == config
        assert docgen.config.project_name == "Test Project"
        assert docgen._initialized is False
    
    @pytest.mark.asyncio
    async def test_initialize(self):
        """Test initializing DocGenMCP."""
        docgen = DocGenMCP()
        
        assert docgen._initialized is False
        
        await docgen.initialize()
        
        assert docgen._initialized is True
        
        # Should not reinitialize if already initialized
        await docgen.initialize()
        assert docgen._initialized is True
    
    @pytest.mark.asyncio
    async def test_generate_documentation(self, temp_dir):
        """Test documentation generation."""
        docgen = DocGenMCP()
        
        project_path = temp_dir / "test_project"
        project_path.mkdir()
        
        # This should initialize if not already initialized
        await docgen.generate_documentation(project_path)
        
        assert docgen._initialized is True
    
    @pytest.mark.asyncio
    async def test_start_mcp_server(self):
        """Test starting MCP server."""
        docgen = DocGenMCP()
        
        # This should initialize if not already initialized
        await docgen.start_mcp_server()
        
        assert docgen._initialized is True
    
    @pytest.mark.asyncio
    async def test_shutdown(self):
        """Test shutting down DocGenMCP."""
        docgen = DocGenMCP()
        
        await docgen.initialize()
        assert docgen._initialized is True
        
        await docgen.shutdown()
        assert docgen._initialized is False
