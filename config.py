"""
MarkPDFDown - Single Source of Truth (SSOT) Configuration
==========================================================

This is the centralized configuration system for all MarkPDFDown components.
All API keys, directories, and settings are managed from this single location.

Security Note: Never commit API keys to git. Use environment variables (.env file).

Enterprise Enhancement for MarkPDFDown
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

This file is part of the enterprise enhancement suite for MarkPDFDown,
providing centralized configuration management for enterprise deployments
with secure API key handling and comprehensive settings management.

Author: Joseph Wright (github: ch0t4nk)
Created: July 16, 2025
Version: 1.0
"""

import os
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class MarkPDFDownConfig:
    """Centralized configuration for MarkPDFDown application"""
    
    def __init__(self):
        # Get the root directory (where this config file is located)
        self.ROOT_DIR = Path(__file__).parent.absolute()
        
    # =================================================================================
    # API CONFIGURATION - Single Source of Truth
    # =================================================================================
    
    @property
    def OPENAI_API_KEY(self) -> str:
        """OpenAI API Key - REQUIRED"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not found! Please set it in your .env file:\n"
                "OPENAI_API_KEY=\"sk-your-key-here\""
            )
        return api_key
    
    @property
    def OPENAI_API_BASE(self) -> str:
        """OpenAI API Base URL"""
        return os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    
    @property
    def OPENAI_DEFAULT_MODEL(self) -> str:
        """Default OpenAI Model"""
        return os.getenv("OPENAI_DEFAULT_MODEL", "gpt-4o-mini")
    
    # =================================================================================
    # DIRECTORY CONFIGURATION - Default Paths
    # =================================================================================
    
    @property
    def DEFAULT_PDF_FOLDER(self) -> Path:
        """Default input folder for PDF files"""
        folder = os.getenv("DEFAULT_PDF_FOLDER", "pdfs")
        return self.ROOT_DIR / folder
    
    @property
    def DEFAULT_OUTPUT_FOLDER(self) -> Path:
        """Default output folder for converted files"""
        folder = os.getenv("DEFAULT_OUTPUT_FOLDER", "outputs")
        return self.ROOT_DIR / folder
    
    @property
    def DEFAULT_CONVERTED_FOLDER(self) -> Path:
        """Default folder for converted markdown files"""
        return self.DEFAULT_OUTPUT_FOLDER / "converted"
    
    @property
    def DEFAULT_METADATA_FOLDER(self) -> Path:
        """Default folder for metadata files"""
        return self.DEFAULT_OUTPUT_FOLDER / "metadata"
    
    @property
    def DEFAULT_TEMP_FOLDER(self) -> Path:
        """Default temporary files folder"""
        folder = os.getenv("DEFAULT_TEMP_FOLDER", "temp")
        return self.ROOT_DIR / folder
    
    @property
    def DEFAULT_CONFIG_FOLDER(self) -> Path:
        """Configuration files folder"""
        return self.ROOT_DIR / "config"
    
    # =================================================================================
    # PROCESSING CONFIGURATION
    # =================================================================================
    
    @property
    def TEMPERATURE(self) -> float:
        """AI model temperature (0.0 = deterministic, 1.0 = creative)"""
        return float(os.getenv("TEMPERATURE", "0.05"))
    
    @property
    def MAX_TOKENS(self) -> int:
        """Maximum tokens per request"""
        return int(os.getenv("MAX_TOKENS", "8192"))
    
    @property
    def DPI(self) -> int:
        """Image extraction quality (DPI)"""
        return int(os.getenv("DPI", "200"))
    
    @property
    def TOP_P(self) -> float:
        """Nucleus sampling parameter"""
        return float(os.getenv("OPENAI_TOP_P", "0.9"))
    
    @property
    def REQUEST_TIMEOUT(self) -> int:
        """API request timeout in seconds"""
        return int(os.getenv("OPENAI_REQUEST_TIMEOUT", "60"))
    
    @property
    def RETRY_DELAY(self) -> float:
        """Delay between retries in seconds"""
        return float(os.getenv("OPENAI_RETRY_DELAY", "0.3"))
    
    # =================================================================================
    # BATCH PROCESSING CONFIGURATION
    # =================================================================================
    
    @property
    def CHECK_INTERVAL(self) -> int:
        """Seconds between batch status checks"""
        return int(os.getenv("CHECK_INTERVAL", "30"))
    
    @property
    def MAX_WAIT_TIME(self) -> int:
        """Maximum wait time for batch completion (seconds)"""
        return int(os.getenv("MAX_WAIT_TIME", "3600"))
    
    @property
    def BATCH_SIZE(self) -> int:
        """Number of requests per batch"""
        return int(os.getenv("OPENAI_BATCH_SIZE", "1"))
    
    # =================================================================================
    # COST MANAGEMENT
    # =================================================================================
    
    @property
    def COST_WARNING_THRESHOLD(self) -> float:
        """Cost threshold for warnings (USD)"""
        return float(os.getenv("COST_WARNING_THRESHOLD", "1.00"))
    
    @property
    def COST_ALERT_THRESHOLD(self) -> float:
        """Cost threshold for alerts (USD)"""
        return float(os.getenv("COST_ALERT_THRESHOLD", "5.00"))
    
    # =================================================================================
    # FEATURE FLAGS
    # =================================================================================
    
    @property
    def CREATE_SESSION_FOLDERS(self) -> bool:
        """Create timestamped session folders"""
        return os.getenv("CREATE_SESSION_FOLDERS", "true").lower() == "true"
    
    @property
    def INCLUDE_MASTER_DOCUMENT(self) -> bool:
        """Create combined master document"""
        return os.getenv("INCLUDE_MASTER_DOCUMENT", "true").lower() == "true"
    
    @property
    def DETAILED_COST_REPORTS(self) -> bool:
        """Generate detailed cost analysis"""
        return os.getenv("DETAILED_COST_REPORTS", "true").lower() == "true"
    
    @property
    def AUTO_CLEANUP(self) -> bool:
        """Automatically clean temporary files"""
        return os.getenv("AUTO_CLEANUP", "true").lower() == "true"
    
    @property
    def KEEP_TEMP_IMAGES(self) -> bool:
        """Keep extracted page images after processing"""
        return os.getenv("KEEP_TEMP_IMAGES", "false").lower() == "true"
    
    @property
    def AUTO_LINTING(self) -> bool:
        """Enable automatic linting after conversion"""
        return os.getenv("AUTO_LINTING", "true").lower() == "true"
    
    @property
    def AUTO_METADATA(self) -> bool:
        """Enable automatic metadata enhancement"""
        return os.getenv("AUTO_METADATA", "true").lower() == "true"
    
    # =================================================================================
    # UTILITY METHODS
    # =================================================================================
    
    def ensure_directories(self):
        """Create all default directories if they don't exist"""
        directories = [
            self.DEFAULT_PDF_FOLDER,
            self.DEFAULT_OUTPUT_FOLDER,
            self.DEFAULT_CONVERTED_FOLDER,
            self.DEFAULT_METADATA_FOLDER,
            self.DEFAULT_TEMP_FOLDER,
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def get_openai_client_config(self) -> Dict[str, Any]:
        """Get OpenAI client configuration dict"""
        return {
            "api_key": self.OPENAI_API_KEY,
            "base_url": self.OPENAI_API_BASE,
        }
    
    def get_model_config(self) -> Dict[str, Any]:
        """Get model configuration dict"""
        return {
            "model": self.OPENAI_DEFAULT_MODEL,
            "temperature": self.TEMPERATURE,
            "max_tokens": self.MAX_TOKENS,
            "top_p": self.TOP_P,
        }
    
    def validate_api_key(self) -> bool:
        """Validate that API key is properly configured"""
        try:
            _ = self.OPENAI_API_KEY
            return True
        except ValueError:
            return False
    
    def print_config_summary(self):
        """Print configuration summary (without exposing API key)"""
        print("🔧 MarkPDFDown Configuration Summary")
        print("=" * 50)
        print(f"📁 PDF Folder: {self.DEFAULT_PDF_FOLDER}")
        print(f"📁 Output Folder: {self.DEFAULT_OUTPUT_FOLDER}")
        print(f"📁 Temp Folder: {self.DEFAULT_TEMP_FOLDER}")
        print(f"🤖 Model: {self.OPENAI_DEFAULT_MODEL}")
        print(f"🌡️  Temperature: {self.TEMPERATURE}")
        print(f"🔢 Max Tokens: {self.MAX_TOKENS}")
        print(f"💰 Cost Warning: ${self.COST_WARNING_THRESHOLD}")
        print(f"🚨 Cost Alert: ${self.COST_ALERT_THRESHOLD}")
        print(f"🔑 API Key: {'✅ Configured' if self.validate_api_key() else '❌ Missing'}")
        print(f"🌐 API Base: {self.OPENAI_API_BASE}")
        print("=" * 50)


# =================================================================================
# GLOBAL CONFIGURATION INSTANCE - Import this in other modules
# =================================================================================

# Single global instance - import this in other modules
config = MarkPDFDownConfig()

# Convenience functions for common operations
def get_config() -> MarkPDFDownConfig:
    """Get the global configuration instance"""
    return config

def get_openai_client_config() -> Dict[str, Any]:
    """Get OpenAI client configuration"""
    return config.get_openai_client_config()

def get_model_config() -> Dict[str, Any]:
    """Get model configuration"""
    return config.get_model_config()

def ensure_directories():
    """Ensure all default directories exist"""
    config.ensure_directories()

# =================================================================================
# LEGACY COMPATIBILITY - For backward compatibility with existing code
# =================================================================================

# Legacy constants for backward compatibility
DEFAULT_PDF_FOLDER = str(config.DEFAULT_PDF_FOLDER)
DEFAULT_OUTPUT_FOLDER = str(config.DEFAULT_OUTPUT_FOLDER)
TEMPERATURE = config.TEMPERATURE
MAX_TOKENS = config.MAX_TOKENS
DPI = config.DPI
CHECK_INTERVAL = config.CHECK_INTERVAL
MAX_WAIT_TIME = config.MAX_WAIT_TIME
COST_WARNING_THRESHOLD = config.COST_WARNING_THRESHOLD
COST_ALERT_THRESHOLD = config.COST_ALERT_THRESHOLD

if __name__ == "__main__":
    # Test configuration when run directly
    config.print_config_summary()
    ensure_directories()
    print("\n✅ Configuration test complete!")
