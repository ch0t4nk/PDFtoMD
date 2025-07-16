#!/usr/bin/env python3
"""
API Provider Switcher
Easily switch between LM Studio and OpenAI
"""

def switch_to_openai():
    """Switch to OpenAI API"""
    env_content = """# OpenAI Configuration (Cloud) - ACTIVE
OPENAI_API_KEY="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"
OPENAI_API_BASE="https://api.openai.com/v1"
OPENAI_DEFAULT_MODEL="gpt-4o-mini"

# LM Studio Configuration (Local) - INACTIVE
# OPENAI_API_KEY="lm-studio"
# OPENAI_API_BASE="http://192.168.56.1:1234/v1"
# OPENAI_DEFAULT_MODEL="Qwen2-VL-7B-Instruct"
"""
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    print("✅ Switched to OpenAI API")

def switch_to_lmstudio():
    """Switch to LM Studio"""
    env_content = """# LM Studio Configuration (Local) - ACTIVE
OPENAI_API_KEY="lm-studio"
OPENAI_API_BASE="http://192.168.56.1:1234/v1"
OPENAI_DEFAULT_MODEL="Qwen2-VL-7B-Instruct"

# OpenAI Configuration (Cloud) - INACTIVE
# OPENAI_API_KEY="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"
# OPENAI_API_BASE="https://api.openai.com/v1"
# OPENAI_DEFAULT_MODEL="gpt-4o-mini"
"""
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    print("✅ Switched to LM Studio")

def show_current():
    """Show current configuration"""
    try:
        with open('.env', 'r', encoding='utf-8') as f:
            content = f.read()

        if 'OPENAI_API_KEY="sk-' in content and not content.startswith('#'):
            print("🌐 Currently using: OpenAI API (Cloud)")
        elif 'OPENAI_API_KEY="lm-studio"' in content and not content.startswith('#'):
            print("🖥️  Currently using: LM Studio (Local)")
        else:
            print("❓ Configuration unclear")

    except FileNotFoundError:
        print("❌ No .env file found")

if __name__ == "__main__":
    import sys

    print("🔄 API Provider Switcher")
    print("=" * 30)

    show_current()
    print()

    if len(sys.argv) > 1:
        if sys.argv[1].lower() in ['openai', 'cloud']:
            switch_to_openai()
        elif sys.argv[1].lower() in ['lmstudio', 'local', 'lms']:
            switch_to_lmstudio()
        else:
            print("Usage: python switch_api.py [openai|lmstudio]")
    else:
        print("Available commands:")
        print("  python switch_api.py openai    # Switch to OpenAI")
        print("  python switch_api.py lmstudio  # Switch to LM Studio")
