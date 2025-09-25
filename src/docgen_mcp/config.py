"""
Configuration management for DocGen MCP.

This module handles all configuration aspects including:
- YAML configuration file parsing
- Environment variable handling
- LLM provider configurations
- Plugin configurations
- Validation and defaults
"""

from typing import Any, Dict, List, Optional
from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class LLMProviderConfig(BaseModel):
    """Configuration for LLM providers."""
    
    provider: str = Field(..., description="LLM provider name")
    model: str = Field(..., description="Model name")
    api_key: Optional[str] = Field(None, description="API key for the provider")
    base_url: Optional[str] = Field(None, description="Base URL for API")
    temperature: float = Field(0.7, description="Temperature for generation")
    max_tokens: int = Field(4000, description="Maximum tokens for generation")
    timeout: int = Field(60, description="Request timeout in seconds")


class DocGenConfig(BaseSettings):
    """Main configuration class for DocGen MCP."""
    
    # Project settings
    project_name: str = Field("DocGen Project", description="Name of the project")
    project_path: Path = Field(Path.cwd(), description="Path to the project to document")
    output_path: Path = Field("./docs", description="Output path for documentation")
    
    # LLM settings
    llm_providers: List[LLMProviderConfig] = Field(
        default_factory=list, description="List of LLM provider configurations"
    )
    default_provider: str = Field("openai", description="Default LLM provider")
    
    # Documentation settings
    include_diagrams: bool = Field(True, description="Generate Mermaid diagrams")
    include_search: bool = Field(True, description="Include search functionality")
    include_wikilinks: bool = Field(True, description="Use Obsidian-style wikilinks")
    
    # Analysis settings
    use_tree_sitter: bool = Field(True, description="Use tree-sitter for code analysis")
    use_ctags: bool = Field(True, description="Use universal ctags for analysis")
    use_ripgrep: bool = Field(True, description="Use ripgrep for search")
    
    # Plugin settings
    enabled_plugins: List[str] = Field(
        default_factory=list, description="List of enabled plugins"
    )
    
    # MCP settings
    mcp_server_port: int = Field(8000, description="MCP server port")
    mcp_server_host: str = Field("localhost", description="MCP server host")
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        
    @classmethod
    def from_yaml(cls, config_path: Path) -> "DocGenConfig":
        """Load configuration from YAML file."""
        import yaml
        
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
            
        with open(config_path, "r") as f:
            config_data = yaml.safe_load(f)
        
        # Convert string paths back to Path objects
        def convert_to_paths(obj):
            if isinstance(obj, dict):
                result = {}
                for k, v in obj.items():
                    if k in ['project_path', 'output_path'] and isinstance(v, str):
                        result[k] = Path(v)
                    else:
                        result[k] = convert_to_paths(v)
                return result
            elif isinstance(obj, list):
                return [convert_to_paths(item) for item in obj]
            else:
                return obj
        
        config_data = convert_to_paths(config_data)
        return cls(**config_data)
    
    def to_yaml(self, config_path: Path) -> None:
        """Save configuration to YAML file."""
        import yaml
        
        config_data = self.model_dump()
        
        # Convert Path objects to strings for YAML serialization
        def convert_paths(obj):
            if isinstance(obj, dict):
                return {k: convert_paths(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_paths(item) for item in obj]
            elif isinstance(obj, Path):
                return str(obj)
            else:
                return obj
        
        config_data = convert_paths(config_data)
        
        with open(config_path, "w") as f:
            yaml.dump(config_data, f, default_flow_style=False, indent=2)
