"""
Tests for configuration management.

This module contains tests for the DocGenConfig class and related functionality.
"""

import pytest
from pathlib import Path
from docgen_mcp.config import DocGenConfig, LLMProviderConfig


class TestLLMProviderConfig:
    """Tests for LLMProviderConfig."""
    
    def test_create_llm_provider_config(self):
        """Test creating an LLM provider configuration."""
        config = LLMProviderConfig(
            provider="openai",
            model="gpt-4",
            api_key="test-key",
            temperature=0.5,
            max_tokens=2000
        )
        
        assert config.provider == "openai"
        assert config.model == "gpt-4"
        assert config.api_key == "test-key"
        assert config.temperature == 0.5
        assert config.max_tokens == 2000
        assert config.timeout == 60  # default value
    
    def test_llm_provider_config_defaults(self):
        """Test LLM provider configuration with defaults."""
        config = LLMProviderConfig(
            provider="anthropic",
            model="claude-3-sonnet"
        )
        
        assert config.provider == "anthropic"
        assert config.model == "claude-3-sonnet"
        assert config.api_key is None
        assert config.base_url is None
        assert config.temperature == 0.7
        assert config.max_tokens == 4000
        assert config.timeout == 60


class TestDocGenConfig:
    """Tests for DocGenConfig."""
    
    def test_create_docgen_config_minimal(self):
        """Test creating a minimal DocGen configuration."""
        config = DocGenConfig(project_path=Path("/test/project"))
        
        assert config.project_name == "DocGen Project"
        assert config.project_path == Path("/test/project")
        assert config.output_path == Path("./docs")
        assert config.default_provider == "openai"
        assert config.include_diagrams is True
        assert config.include_search is True
        assert config.include_wikilinks is True
        assert config.use_tree_sitter is True
        assert config.use_ctags is True
        assert config.use_ripgrep is True
        assert config.mcp_server_port == 8000
        assert config.mcp_server_host == "localhost"
    
    def test_create_docgen_config_with_llm_providers(self):
        """Test creating DocGen configuration with LLM providers."""
        llm_config = LLMProviderConfig(
            provider="openai",
            model="gpt-4",
            api_key="test-key"
        )
        
        config = DocGenConfig(
            project_path=Path("/test/project"),
            llm_providers=[llm_config],
            default_provider="openai"
        )
        
        assert len(config.llm_providers) == 1
        assert config.llm_providers[0].provider == "openai"
        assert config.llm_providers[0].model == "gpt-4"
        assert config.default_provider == "openai"
    
    def test_docgen_config_yaml_methods(self, temp_dir):
        """Test YAML serialization and deserialization."""
        config_path = temp_dir / "test_config.yaml"
        
        # Create a configuration
        original_config = DocGenConfig(
            project_name="Test Project",
            project_path=Path("/test/project"),
            output_path=Path("./test_docs"),
            default_provider="anthropic",
            include_diagrams=False
        )
        
        # Save to YAML
        original_config.to_yaml(config_path)
        assert config_path.exists()
        
        # Load from YAML
        loaded_config = DocGenConfig.from_yaml(config_path)
        
        assert loaded_config.project_name == "Test Project"
        assert loaded_config.project_path == Path("/test/project")
        assert loaded_config.output_path == Path("./test_docs")
        assert loaded_config.default_provider == "anthropic"
        assert loaded_config.include_diagrams is False
    
    def test_docgen_config_yaml_file_not_found(self, temp_dir):
        """Test loading configuration from non-existent YAML file."""
        config_path = temp_dir / "nonexistent.yaml"
        
        with pytest.raises(FileNotFoundError):
            DocGenConfig.from_yaml(config_path)
