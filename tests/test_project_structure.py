"""
Test project structure validation.

This test ensures that the project follows the expected structure
and that all required files and directories exist.

Following TDD principles: This test will FAIL initially (RED phase)
until we create the required project structure (GREEN phase).
"""

import os
import pytest
from pathlib import Path


class TestProjectStructure:
    """Test cases for validating project structure."""
    
    def test_pyproject_toml_exists(self):
        """Test that pyproject.toml exists in the root directory."""
        pyproject_path = Path("pyproject.toml")
        assert pyproject_path.exists(), "pyproject.toml must exist in the root directory"
    
    def test_src_directory_exists(self):
        """Test that src directory exists."""
        src_path = Path("src")
        assert src_path.exists(), "src directory must exist"
        assert src_path.is_dir(), "src must be a directory"
    
    def test_docgen_mcp_package_exists(self):
        """Test that the main package directory exists."""
        package_path = Path("src/docgen_mcp")
        assert package_path.exists(), "src/docgen_mcp directory must exist"
        assert package_path.is_dir(), "src/docgen_mcp must be a directory"
    
    def test_package_init_exists(self):
        """Test that package __init__.py exists."""
        init_path = Path("src/docgen_mcp/__init__.py")
        assert init_path.exists(), "src/docgen_mcp/__init__.py must exist"
    
    def test_tests_directory_structure(self):
        """Test that tests directory has proper structure."""
        tests_path = Path("tests")
        assert tests_path.exists(), "tests directory must exist"
        assert tests_path.is_dir(), "tests must be a directory"
        
        # Test for conftest.py
        conftest_path = Path("tests/conftest.py")
        assert conftest_path.exists(), "tests/conftest.py must exist"
    
    def test_pytest_ini_exists(self):
        """Test that pytest.ini configuration exists."""
        pytest_ini_path = Path("pytest.ini")
        assert pytest_ini_path.exists(), "pytest.ini must exist in the root directory"
    
    def test_precommit_config_exists(self):
        """Test that pre-commit configuration exists."""
        precommit_path = Path(".pre-commit-config.yaml")
        assert precommit_path.exists(), ".pre-commit-config.yaml must exist"
    
    def test_required_directories_exist(self):
        """Test that all required package directories exist."""
        required_dirs = [
            "src/docgen_mcp/llm",
            "src/docgen_mcp/agent", 
            "src/docgen_mcp/analysis",
            "src/docgen_mcp/generation",
            "src/docgen_mcp/vault",
            "src/docgen_mcp/diagrams",
            "src/docgen_mcp/search",
            "src/docgen_mcp/mcp_tools",
            "src/docgen_mcp/plugins",
            "src/docgen_mcp/markdown"
        ]
        
        for dir_path in required_dirs:
            path = Path(dir_path)
            assert path.exists(), f"Directory {dir_path} must exist"
            assert path.is_dir(), f"{dir_path} must be a directory"
            
            # Each directory should have an __init__.py
            init_file = path / "__init__.py"
            assert init_file.exists(), f"{dir_path}/__init__.py must exist"


class TestDevelopmentEnvironment:
    """Test cases for development environment setup."""
    
    def test_uv_available(self):
        """Test that uv package manager is available."""
        import subprocess
        try:
            result = subprocess.run(["uv", "--version"], 
                                  capture_output=True, text=True, check=True)
            assert "uv" in result.stdout.lower(), "uv package manager must be available"
        except (subprocess.CalledProcessError, FileNotFoundError):
            pytest.fail("uv package manager is not installed or not available in PATH")
    
    def test_python_version(self):
        """Test that Python version is 3.11 or higher."""
        import sys
        assert sys.version_info >= (3, 11), "Python 3.11 or higher is required"
    
    @pytest.mark.skip(reason="Virtual environment check not applicable in sandbox")
    def test_virtual_environment_active(self):
        """Test that we're running in a virtual environment."""
        import sys
        # Check if we're in a virtual environment
        in_venv = (hasattr(sys, 'real_prefix') or 
                  (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
        assert in_venv, "Tests should run in a virtual environment"


class TestTDDInfrastructure:
    """Test cases for TDD infrastructure setup."""
    
    def test_pytest_configuration(self):
        """Test that pytest is properly configured."""
        pytest_ini_path = Path("pytest.ini")
        if pytest_ini_path.exists():
            content = pytest_ini_path.read_text()
            assert "[tool:pytest]" in content or "[pytest]" in content, \
                "pytest.ini must contain pytest configuration"
    
    def test_coverage_configuration(self):
        """Test that coverage reporting is configured."""
        # This will be validated once we create the configuration
        pass
    
    def test_test_discovery(self):
        """Test that pytest can discover this test file."""
        # If this test runs, pytest discovery is working
        assert True, "Test discovery is working"
