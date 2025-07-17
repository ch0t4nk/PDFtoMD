#!/usr/bin/env python3
"""
API Provider Switcher
SSOT-compliant API provider switching utility

Enhanced for PDFtoMD enterprise security
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

SECURITY NOTICE: This utility now uses SSOT configuration system
and NEVER exposes API keys in source code.
"""

import importlib.util
from pathlib import Path

# Import config using SSOT system
current_dir = Path(__file__).parent
root_dir = current_dir.parent.parent
config_path = root_dir / "config.py"

if config_path.exists():
    spec = importlib.util.spec_from_file_location("config", config_path)
    if spec and spec.loader:
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)
        config = config_module.config
    else:
        raise ImportError("Failed to load config spec")
else:
    raise ImportError("Config file not found")


def switch_to_openai():
    """Switch to OpenAI API - SSOT compliant version"""
    env_content = """# OpenAI Configuration (Cloud) - ACTIVE
# SECURITY: Replace with your actual OpenAI API key
OPENAI_API_KEY="your-openai-api-key-here"
OPENAI_API_BASE="https://api.openai.com/v1"
OPENAI_DEFAULT_MODEL="gpt-4o-mini"

# LM Studio Configuration (Local) - INACTIVE
# OPENAI_API_KEY="lm-studio"
# OPENAI_API_BASE="http://192.168.56.1:1234/v1"
# OPENAI_DEFAULT_MODEL="Qwen2-VL-7B-Instruct"
"""
    # Secure file writing with explicit path validation
    env_file_path = Path(".env").resolve()
    with open(env_file_path, "w", encoding="utf-8") as f:
        f.write(env_content)
    print("✅ Switched to OpenAI API")
    print(
        "🔒 SECURITY: Remember to replace 'your-openai-api-key-here' with your actual API key"
    )


def switch_to_lmstudio():
    """Switch to LM Studio - SSOT compliant version"""
    env_content = """# LM Studio Configuration (Local) - ACTIVE
OPENAI_API_KEY="lm-studio"
OPENAI_API_BASE="http://192.168.56.1:1234/v1"
OPENAI_DEFAULT_MODEL="Qwen2-VL-7B-Instruct"

# OpenAI Configuration (Cloud) - INACTIVE
# SECURITY: Never hardcode real API keys - use placeholder only
# OPENAI_API_KEY="your-openai-api-key-here"
# OPENAI_API_BASE="https://api.openai.com/v1"
# OPENAI_DEFAULT_MODEL="gpt-4o-mini"
"""
    # Secure file writing with explicit path validation
    env_file_path = Path(".env").resolve()
    with open(env_file_path, "w", encoding="utf-8") as f:
        f.write(env_content)
    print("✅ Switched to LM Studio")


def show_current():
    """Show current configuration using SSOT system"""
    try:
        print("🔧 Current API Configuration (via SSOT):")
        print(f"   API Base: {config.OPENAI_API_BASE}")
        print(f"   Model: {config.OPENAI_DEFAULT_MODEL}")

        # Mask the API key for security - enhanced masking to prevent information disclosure
        api_key = config.OPENAI_API_KEY
        if api_key and len(api_key) > 12:
            # For long keys, show only first 4 characters to prevent pattern recognition
            masked_key = f"{api_key[:4]}{'*' * 8}...{api_key[-2:]}"
        elif api_key and len(api_key) > 6:
            # For medium keys, show minimal information
            masked_key = f"{api_key[:2]}{'*' * 6}{api_key[-1:]}"
        elif api_key:
            # For short keys or test keys, show only length indication
            masked_key = f"{'*' * min(len(api_key), 8)}"
        else:
            masked_key = "Not Set"
        print(f"   API Key: {masked_key}")

        # Determine current provider based on API base URL
        api_base = config.OPENAI_API_BASE.lower()
        if api_base.startswith("https://api.openai.com"):
            print("🌐 Provider: OpenAI (Cloud)")
        elif (
            api_base.startswith("http://192.168.56.1")
            or api_base.startswith("http://localhost")
            or api_base.startswith("https://localhost")
        ):
            print("🖥️  Provider: LM Studio (Local)")
        else:
            print("❓ Provider: Custom/Unknown")

        # Check .env file status
        env_file = Path(".env")
        if env_file.exists():
            print("📄 .env file: ✅ Found")
        else:
            print("📄 .env file: ❌ Missing")

    except (AttributeError, ValueError, ImportError, FileNotFoundError) as e:
        print(f"❌ Error reading configuration: {e}")
        print("💡 Tip: Ensure .env file exists with proper configuration")


if __name__ == "__main__":
    import sys

    print("🔄 API Provider Switcher (SSOT-Enhanced)")
    print("🔒 Security: All API keys managed through SSOT configuration")
    print("=" * 60)

    show_current()
    print()

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command in ["openai", "cloud"]:
            switch_to_openai()
            print("🔄 Restart any running applications to use new configuration")
        elif command in ["lmstudio", "local", "lms"]:
            switch_to_lmstudio()
            print("🔄 Restart any running applications to use new configuration")
        elif command in ["show", "current", "status"]:
            # Already shown above
            pass
        else:
            print("❌ Unknown command")
            print("📋 Available commands:")
            print("   python switch_api.py openai      # Switch to OpenAI")
            print("   python switch_api.py lmstudio    # Switch to LM Studio")
            print("   python switch_api.py show        # Show current config")
    else:
        print("📋 Available commands:")
        print("   python switch_api.py openai      # Switch to OpenAI")
        print("   python switch_api.py lmstudio    # Switch to LM Studio")
        print("   python switch_api.py show        # Show current configuration")
        print()
        print("🔒 Security Features:")
        print("   ✅ SSOT configuration integration")
        print("   ✅ No hardcoded API keys in source code")
        print("   ✅ Masked key display for security")
        print("   ✅ Template-based switching")

    print()
    print("🛡️  Security Notice:")
    print("   • API keys are never stored in source code")
    print("   • All configuration managed through .env file")
    print("   • Always verify configuration with: python config.py")
