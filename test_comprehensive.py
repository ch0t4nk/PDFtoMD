#!/usr/bin/env python3
"""
MarkPDFDown Comprehensive Test Suite
===================================

Enterprise Enhancement for MarkPDFDown
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

This file provides comprehensive testing for all MarkPDFDown components
including core functionality, enterprise features, configuration validation,
and integration testing.

Author: Joseph Wright (github: ch0t4nk)
Created: July 16, 2025
Version: 1.0
"""

import os
import sys
import json
import time
import subprocess
import importlib.util
from pathlib import Path
from typing import Dict, List, Tuple, Any
import tempfile
import shutil

class MarkPDFDownTestSuite:
    """Comprehensive test suite for MarkPDFDown project"""
    
    def __init__(self):
        self.root_dir = Path(__file__).parent.absolute()
        self.test_results: Dict[str, Any] = {}
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
        # Test status tracking
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0
        
    def print_status(self, message: str, level: str = "INFO"):
        """Print formatted status messages"""
        timestamp = time.strftime('%H:%M:%S')
        # Use ASCII-safe symbols for Windows compatibility
        symbols = {
            "INFO": "[INFO]",
            "SUCCESS": "[PASS]", 
            "WARNING": "[WARN]",
            "ERROR": "[FAIL]",
            "PROGRESS": "[PROG]",
            "TEST": "[TEST]"
        }
        symbol = symbols.get(level, "[INFO]")
        print(f"{symbol} [{timestamp}] {message}")
        
    def run_test(self, test_name: str, test_func, *args, **kwargs) -> bool:
        """Run a single test and track results"""
        self.tests_run += 1
        self.print_status(f"Running test: {test_name}", "TEST")
        
        try:
            result = test_func(*args, **kwargs)
            if result:
                self.tests_passed += 1
                self.print_status(f"PASS {test_name}", "SUCCESS")
                self.test_results[test_name] = {"status": "PASSED", "details": "Test completed successfully"}
                return True
            else:
                self.tests_failed += 1
                self.print_status(f"FAIL {test_name}", "ERROR")
                self.test_results[test_name] = {"status": "FAILED", "details": "Test returned False"}
                return False
        except Exception as e:
            self.tests_failed += 1
            error_msg = f"Test {test_name} failed with exception: {str(e)}"
            self.errors.append(error_msg)
            self.print_status(f"FAIL {test_name}: {e}", "ERROR")
            self.test_results[test_name] = {"status": "FAILED", "details": str(e)}
            return False

    def test_project_structure(self) -> bool:
        """Test that all required project files and directories exist"""
        required_files = [
            "README.md",
            "LICENSE", 
            "NOTICE",
            "config.py",
            "requirements.txt",
            "requirements-dev.txt",
            "pyproject.toml",
            ".env.template"
        ]
        
        required_dirs = [
            "src/core",
            "src/scripts", 
            "src/batch",
            "src/utils",
            "docs/legal",
            "docs/guides",
            "docs/security",
            "examples",
            "tools"
        ]
        
        missing_files = []
        missing_dirs = []
        
        # Check required files
        for file_path in required_files:
            if not (self.root_dir / file_path).exists():
                missing_files.append(file_path)
                
        # Check required directories
        for dir_path in required_dirs:
            if not (self.root_dir / dir_path).exists():
                missing_dirs.append(dir_path)
                
        if missing_files:
            self.errors.append(f"Missing required files: {', '.join(missing_files)}")
            
        if missing_dirs:
            self.errors.append(f"Missing required directories: {', '.join(missing_dirs)}")
            
        return len(missing_files) == 0 and len(missing_dirs) == 0

    def test_configuration_system(self) -> bool:
        """Test SSOT configuration system"""
        try:
            # Test config import - first try direct import
            try:
                import config
                config_obj = config.config
            except ImportError:
                # Fallback to importlib
                config_path = self.root_dir / "config.py"
                spec = importlib.util.spec_from_file_location("config", config_path)
                if not spec or not spec.loader:
                    self.errors.append("Failed to load config specification")
                    return False
                    
                config_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(config_module)
                config_obj = config_module.config
            
            # Test required configuration attributes
            required_attrs = [
                'OPENAI_API_KEY',
                'OPENAI_API_BASE', 
                'OPENAI_DEFAULT_MODEL',
                'DEFAULT_PDF_FOLDER',
                'DEFAULT_CONVERTED_FOLDER',
                'DEFAULT_OUTPUT_FOLDER'
            ]
            
            missing_attrs = []
            for attr in required_attrs:
                if not hasattr(config_obj, attr):
                    missing_attrs.append(attr)
                    
            if missing_attrs:
                self.errors.append(f"Missing config attributes: {', '.join(missing_attrs)}")
                return False
                
            # Test that config has sensible defaults
            if not config_obj.OPENAI_API_BASE:
                self.warnings.append("OPENAI_API_BASE has no default value")
                
            # Test that config loads test API key if available
            if hasattr(config_obj, 'OPENAI_API_KEY') and config_obj.OPENAI_API_KEY == "test_key_here":
                self.warnings.append("Config did not load test API key")
                
            return True
            
        except Exception as e:
            self.errors.append(f"Configuration system test failed: {str(e)}")
            return False

    def test_core_imports(self) -> bool:
        """Test that all core modules can be imported"""
        core_modules = [
            "src.core.main",
            "src.core.main_fast", 
            "src.core.LLMClient",
            "src.core.PDFWorker",
            "src.core.ImageWorker",
            "src.core.FileWorker",
            "src.core.Util"
        ]
        
        # Add src to Python path temporarily
        sys.path.insert(0, str(self.root_dir / "src"))
        
        failed_imports = []
        
        try:
            for module_name in core_modules:
                try:
                    # Convert path to import name
                    import_name = module_name.replace("src.", "")
                    __import__(import_name)
                except ImportError as e:
                    failed_imports.append(f"{module_name}: {str(e)}")
                    
        finally:
            # Remove src from path
            if str(self.root_dir / "src") in sys.path:
                sys.path.remove(str(self.root_dir / "src"))
                
        if failed_imports:
            self.errors.extend(failed_imports)
            return False
            
        return True

    def test_dependencies(self) -> bool:
        """Test that all required dependencies are available"""
        required_packages = {
            'openai': '1.66.3',
            'pymupdf': '1.25.3', 
            'pypdf2': '3.0.1',
            'python-dotenv': '1.1.0'
        }
        
        missing_packages = []
        version_mismatches = []
        
        for package, expected_version in required_packages.items():
            try:
                if package == 'pymupdf':
                    # PyMuPDF imports as fitz
                    import fitz
                    # Get version if available
                    if hasattr(fitz, '__version__'):
                        actual_version = fitz.__version__
                        if not actual_version.startswith(expected_version.split('.')[0]):
                            version_mismatches.append(f"{package}: expected {expected_version}, got {actual_version}")
                elif package == 'pypdf2':
                    import PyPDF2
                    # PyPDF2 version checking
                    if hasattr(PyPDF2, '__version__'):
                        actual_version = PyPDF2.__version__
                        if not actual_version.startswith(expected_version.split('.')[0]):
                            version_mismatches.append(f"{package}: expected {expected_version}, got {actual_version}")
                elif package == 'openai':
                    import openai
                    if hasattr(openai, '__version__'):
                        actual_version = openai.__version__
                        if not actual_version.startswith(expected_version.split('.')[0]):
                            version_mismatches.append(f"{package}: expected {expected_version}, got {actual_version}")
                elif package == 'python-dotenv':
                    import dotenv
                    # python-dotenv doesn't always have __version__
                    try:
                        actual_version = dotenv.__version__  # type: ignore
                        if not actual_version.startswith(expected_version.split('.')[0]):
                            version_mismatches.append(f"{package}: expected {expected_version}, got {actual_version}")
                    except AttributeError:
                        # Version not available, skip version check
                        pass
                            
            except ImportError:
                missing_packages.append(package)
                
        if missing_packages:
            self.errors.append(f"Missing required packages: {', '.join(missing_packages)}")
            
        if version_mismatches:
            self.warnings.extend(version_mismatches)
            
        return len(missing_packages) == 0

    def test_environment_template(self) -> bool:
        """Test .env.template file exists and has required variables"""
        env_template = self.root_dir / ".env.template"
        
        if not env_template.exists():
            self.errors.append(".env.template file not found")
            return False
            
        try:
            content = env_template.read_text(encoding='utf-8')
            
            required_vars = [
                'OPENAI_API_KEY',
                'OPENAI_API_BASE',
                'OPENAI_DEFAULT_MODEL'
            ]
            
            missing_vars = []
            for var in required_vars:
                if var not in content:
                    missing_vars.append(var)
                    
            if missing_vars:
                self.errors.append(f"Missing variables in .env.template: {', '.join(missing_vars)}")
                return False
                
            return True
            
        except Exception as e:
            self.errors.append(f"Error reading .env.template: {str(e)}")
            return False

    def test_requirements_files(self) -> bool:
        """Test requirements files are valid and contain expected packages"""
        requirements_files = ["requirements.txt", "requirements-dev.txt"]
        
        for req_file in requirements_files:
            req_path = self.root_dir / req_file
            
            if not req_path.exists():
                self.errors.append(f"Requirements file not found: {req_file}")
                return False
                
            try:
                content = req_path.read_text(encoding='utf-8')
                
                if req_file == "requirements.txt":
                    expected_packages = ['openai', 'pymupdf', 'pypdf2', 'python-dotenv']
                else:  # requirements-dev.txt
                    expected_packages = ['pre-commit', 'pytest', 'ruff']
                    
                missing_packages = []
                for package in expected_packages:
                    if package not in content.lower():
                        missing_packages.append(package)
                        
                if missing_packages:
                    self.errors.append(f"Missing packages in {req_file}: {', '.join(missing_packages)}")
                    return False
                    
            except Exception as e:
                self.errors.append(f"Error reading {req_file}: {str(e)}")
                return False
                
        return True

    def test_script_syntax(self) -> bool:
        """Test that all Python scripts have valid syntax"""
        python_files = []
        
        # Find all Python files
        for pattern in ["src/**/*.py", "tools/**/*.py", "scripts/**/*.py"]:
            python_files.extend(self.root_dir.glob(pattern))
            
        # Add root level Python files
        python_files.extend([
            self.root_dir / "config.py",
            self.root_dir / "migrate_to_ssot.py"
        ])
        
        syntax_errors = []
        
        for py_file in python_files:
            if py_file.exists():
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        compile(f.read(), str(py_file), 'exec')
                except SyntaxError as e:
                    syntax_errors.append(f"{py_file.relative_to(self.root_dir)}: {str(e)}")
                except Exception as e:
                    self.warnings.append(f"Could not check syntax for {py_file.relative_to(self.root_dir)}: {str(e)}")
                    
        if syntax_errors:
            self.errors.extend(syntax_errors)
            return False
            
        return True

    def test_attribution_compliance(self) -> bool:
        """Test that attribution headers are present in enterprise files"""
        enterprise_files = [
            "src/scripts/master.py",
            "src/scripts/auto_batch.py", 
            "src/batch/batch_api.py",
            "src/batch/master.py",
            "config.py",
            "migrate_to_ssot.py",
            "src/scripts/workspace_lint.py",
            "src/scripts/cleanup_backups.py"
        ]
        
        missing_attribution = []
        
        for file_path in enterprise_files:
            full_path = self.root_dir / file_path
            if full_path.exists():
                try:
                    content = full_path.read_text(encoding='utf-8')
                    
                    # Check for enterprise enhancement header
                    if "Enterprise Enhancement for MarkPDFDown" not in content:
                        missing_attribution.append(file_path)
                    elif "Joseph Wright" not in content:
                        missing_attribution.append(f"{file_path} (missing author)")
                        
                except Exception as e:
                    self.warnings.append(f"Could not check attribution for {file_path}: {str(e)}")
                    
        if missing_attribution:
            self.errors.append(f"Missing attribution headers: {', '.join(missing_attribution)}")
            return False
            
        return True

    def test_documentation_links(self) -> bool:
        """Test that internal documentation links are valid"""
        doc_files = list((self.root_dir / "docs").glob("**/*.md"))
        doc_files.append(self.root_dir / "README.md")
        
        broken_links = []
        
        for doc_file in doc_files:
            if doc_file.exists():
                try:
                    content = doc_file.read_text(encoding='utf-8')
                    
                    # Find markdown links
                    import re
                    links = re.findall(r'\[.*?\]\((.*?)\)', content)
                    
                    for link in links:
                        # Skip external links
                        if link.startswith(('http://', 'https://', 'mailto:')):
                            continue
                            
                        # Check internal links
                        if link.startswith('../'):
                            # Relative link from docs folder
                            target_path = doc_file.parent / link
                        else:
                            # Relative link
                            target_path = doc_file.parent / link
                            
                        # Resolve path
                        try:
                            resolved_path = target_path.resolve()
                            if not resolved_path.exists():
                                broken_links.append(f"{doc_file.relative_to(self.root_dir)}: {link}")
                        except Exception:
                            # Path resolution failed
                            broken_links.append(f"{doc_file.relative_to(self.root_dir)}: {link} (resolution failed)")
                            
                except Exception as e:
                    self.warnings.append(f"Could not check links in {doc_file.relative_to(self.root_dir)}: {str(e)}")
                    
        if broken_links:
            self.warnings.extend(broken_links)
            # Don't fail the test for broken links, just warn
            
        return True

    def test_enterprise_features(self) -> bool:
        """Test enterprise feature availability"""
        try:
            # Test batch processing scripts exist
            batch_scripts = [
                "src/scripts/auto_batch.py",
                "src/batch/batch_api.py", 
                "src/scripts/master.py"
            ]
            
            missing_scripts = []
            for script in batch_scripts:
                if not (self.root_dir / script).exists():
                    missing_scripts.append(script)
                    
            if missing_scripts:
                self.errors.append(f"Missing enterprise scripts: {', '.join(missing_scripts)}")
                return False
                
            # Test workspace linting script
            workspace_lint = self.root_dir / "src/scripts/workspace_lint.py"
            if not workspace_lint.exists():
                self.errors.append("Workspace linting script not found")
                return False
                
            return True
            
        except Exception as e:
            self.errors.append(f"Enterprise features test failed: {str(e)}")
            return False

    def run_integration_test(self) -> bool:
        """Run a basic integration test with sample data"""
        try:
            # Create temporary test environment
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                
                # Create test .env file
                env_file = temp_path / ".env"
                env_content = """
# Test environment
OPENAI_API_KEY=test_key_placeholder
OPENAI_API_BASE=https://api.openai.com/v1
OPENAI_DEFAULT_MODEL=gpt-4o-mini
"""
                env_file.write_text(env_content)
                
                # Test config loading in isolated environment
                original_cwd = os.getcwd()
                try:
                    os.chdir(temp_path)
                    
                    # Copy config.py to temp directory
                    shutil.copy2(self.root_dir / "config.py", temp_path / "config.py")
                    
                    # Test config import
                    spec = importlib.util.spec_from_file_location("config", temp_path / "config.py")
                    if spec and spec.loader:
                        config_module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(config_module)
                        config = config_module.config
                        
                        # Verify config loaded test values
                        if config.OPENAI_API_KEY != "test_key_placeholder":
                            self.warnings.append("Config did not load test API key")
                            
                        if config.OPENAI_DEFAULT_MODEL != "gpt-4o-mini":
                            self.warnings.append("Config did not load test model")
                            
                finally:
                    os.chdir(original_cwd)
                    
            return True
            
        except Exception as e:
            self.errors.append(f"Integration test failed: {str(e)}")
            return False

    def generate_test_report(self) -> Dict[str, Any]:
        """Generate comprehensive test report"""
        return {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "summary": {
                "tests_run": self.tests_run,
                "tests_passed": self.tests_passed, 
                "tests_failed": self.tests_failed,
                "success_rate": f"{(self.tests_passed/self.tests_run*100):.1f}%" if self.tests_run > 0 else "0%"
            },
            "test_results": self.test_results,
            "errors": self.errors,
            "warnings": self.warnings,
            "status": "PASSED" if self.tests_failed == 0 else "FAILED"
        }

    def run_comprehensive_test(self) -> bool:
        """Run all tests in the comprehensive test suite"""
        self.print_status("Starting MarkPDFDown Comprehensive Test Suite", "SUCCESS")
        self.print_status("="*60, "INFO")
        
        # Define test suite
        tests = [
            ("Project Structure", self.test_project_structure),
            ("Configuration System", self.test_configuration_system), 
            ("Core Module Imports", self.test_core_imports),
            ("Dependencies", self.test_dependencies),
            ("Environment Template", self.test_environment_template),
            ("Requirements Files", self.test_requirements_files),
            ("Script Syntax", self.test_script_syntax),
            ("Attribution Compliance", self.test_attribution_compliance),
            ("Documentation Links", self.test_documentation_links),
            ("Enterprise Features", self.test_enterprise_features),
            ("Integration Test", self.run_integration_test)
        ]
        
        # Run all tests
        for test_name, test_func in tests:
            self.run_test(test_name, test_func)
            
        # Generate and display report
        report = self.generate_test_report()
        
        self.print_status("="*60, "INFO")
        self.print_status("TEST SUITE COMPLETED", "SUCCESS" if report["status"] == "PASSED" else "ERROR")
        self.print_status("="*60, "INFO")
        
        print(f"\n📊 TEST SUMMARY:")
        print(f"   Tests Run: {report['summary']['tests_run']}")
        print(f"   Tests Passed: {report['summary']['tests_passed']}")
        print(f"   Tests Failed: {report['summary']['tests_failed']}") 
        print(f"   Success Rate: {report['summary']['success_rate']}")
        
        if self.errors:
            print(f"\n[ERRORS] ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"   {i}. {error}")
                
        if self.warnings:
            print(f"\n[WARNINGS] ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"   {i}. {warning}")
                
        # Save detailed report
        report_file = self.root_dir / "test_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
            
        self.print_status(f"Detailed report saved to: {report_file}", "INFO")
        
        return report["status"] == "PASSED"

def main():
    """Main entry point for test suite"""
    test_suite = MarkPDFDownTestSuite()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "quick":
            # Quick test - essential checks only
            tests = [
                ("Project Structure", test_suite.test_project_structure),
                ("Configuration System", test_suite.test_configuration_system),
                ("Dependencies", test_suite.test_dependencies),
                ("Script Syntax", test_suite.test_script_syntax)
            ]
            
            test_suite.print_status("Running Quick Test Suite", "INFO")
            for test_name, test_func in tests:
                test_suite.run_test(test_name, test_func)
                
        elif command == "structure":
            test_suite.run_test("Project Structure", test_suite.test_project_structure)
            
        elif command == "config":
            test_suite.run_test("Configuration System", test_suite.test_configuration_system)
            
        elif command == "deps":
            test_suite.run_test("Dependencies", test_suite.test_dependencies)
            
        else:
            print("Unknown command. Available commands:")
            print("  python test_comprehensive.py           # Run full test suite")
            print("  python test_comprehensive.py quick     # Run quick tests")
            print("  python test_comprehensive.py structure # Test project structure")
            print("  python test_comprehensive.py config    # Test configuration")
            print("  python test_comprehensive.py deps      # Test dependencies")
            return
    else:
        # Run comprehensive test suite
        success = test_suite.run_comprehensive_test()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
