"""
Pytest configuration and fixtures for DocGen MCP tests.

This file contains shared fixtures and configuration for all tests
in the DocGen MCP project.
"""

import os
import sys
import tempfile
from pathlib import Path
from typing import Generator

import pytest

# Add src to Python path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def sample_codebase(temp_dir: Path) -> Path:
    """Create a sample codebase for testing."""
    # Create a simple Python project structure
    (temp_dir / "src").mkdir()
    (temp_dir / "src" / "myproject").mkdir()
    
    # Create some sample Python files
    (temp_dir / "src" / "myproject" / "__init__.py").write_text(
        '"""Sample project for testing."""\n__version__ = "1.0.0"\n'
    )
    
    (temp_dir / "src" / "myproject" / "main.py").write_text(
        '''"""Main module."""

def main():
    """Main function."""
    print("Hello, World!")

if __name__ == "__main__":
    main()
'''
    )
    
    (temp_dir / "README.md").write_text("# Sample Project\n\nThis is a test project.\n")
    
    return temp_dir


@pytest.fixture
def mock_llm_response():
    """Mock LLM response for testing."""
    return {
        "content": "This is a mock response from the LLM.",
        "usage": {"prompt_tokens": 10, "completion_tokens": 8, "total_tokens": 18},
        "model": "mock-model",
    }


# Test markers
pytest_plugins = []

# Configure test environment
os.environ["TESTING"] = "1"
