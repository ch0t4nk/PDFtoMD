#!/usr/bin/env python3
"""
GitHub Secret Scanning Alert Resolution
======================================
Helps resolve the OpenAI API key exposure alert
"""

import json
import re
import subprocess
import sys


def redact_sensitive_info(text):
    """Redact sensitive information from text for safe logging"""
    # Redact OpenAI API keys (sk-proj-xxx, sk-xxx patterns)
    text = re.sub(r"sk-proj-[A-Za-z0-9_-]+", "[REDACTED_API_KEY]", text)
    text = re.sub(r"sk-[A-Za-z0-9_-]+", "[REDACTED_API_KEY]", text)

    # Redact GitHub tokens (ghp_xxx patterns)
    text = re.sub(r"ghp_[A-Za-z0-9_-]+", "[REDACTED_GITHUB_TOKEN]", text)

    # Redact other common secret patterns
    text = re.sub(r"[A-Za-z0-9+/=]{40,}", "[REDACTED_SECRET]", text)

    return text


def check_github_cli():
    """Check if GitHub CLI is available"""
    try:
        result = subprocess.run(["gh", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def get_secret_alerts():
    """Get current secret scanning alerts"""
    try:
        result = subprocess.run(
            ["gh", "api", "/repos/ch0t4nk/PDFtoMD/secret-scanning/alerts"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        return []
    except Exception as e:
        print(f"Error getting alerts: {e}")
        return []


def resolve_alert(alert_number, resolution="revoked"):
    """Resolve a secret scanning alert"""
    try:
        data = {
            "state": "resolved",
            "resolution": resolution,
            "resolution_comment": "API key has been revoked and replaced. Codebase cleaned of all hardcoded secrets.",
        }

        result = subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "PATCH",
                f"/repos/ch0t4nk/PDFtoMD/secret-scanning/alerts/{alert_number}",
                "--input",
                "-",
            ],
            input=json.dumps(data),
            text=True,
            capture_output=True,
        )

        return result.returncode == 0, result.stderr
    except Exception as e:
        return False, str(e)


def main():
    print("🔒 GitHub Secret Scanning Alert Resolution")
    print("=" * 50)

    if not check_github_cli():
        print("❌ GitHub CLI not found. Please install: https://cli.github.com/")
        return False

    print("📡 Checking current secret scanning alerts...")
    alerts = get_secret_alerts()

    if not alerts:
        print("✅ No active secret scanning alerts found!")
        return True

    print(f"📋 Found {len(alerts)} alert(s):")
    for alert in alerts:
        # Redact sensitive info from alert data before logging
        secret_type = redact_sensitive_info(
            alert.get("secret_type_display_name", "Unknown")
        )
        created_at = redact_sensitive_info(alert.get("created_at", "Unknown"))
        file_path = redact_sensitive_info(
            alert.get("first_location_detected", {}).get("path", "Unknown")
        )
        line_num = alert.get("first_location_detected", {}).get("start_line", "Unknown")

        print(f"   Alert #{alert['number']}: {secret_type}")
        print(f"   State: {alert['state']}")
        print(f"   Created: {created_at}")
        print(f"   File: {file_path}")
        print(f"   Line: {line_num}")
        print()

    print("🚨 CRITICAL: Before resolving alerts, ensure you have:")
    print("   1. ✅ REVOKED the exposed API key in OpenAI dashboard")
    print("   2. ✅ Generated a NEW API key")
    print("   3. ✅ Updated your .env file with the new key")
    print("   4. ✅ Verified no hardcoded keys remain in codebase")
    print()

    response = input("Have you completed ALL the above steps? (yes/no): ")
    if response.lower() != "yes":
        print("⚠️  Please complete the security steps first!")
        print("📋 Instructions:")
        print("   1. Go to: https://platform.openai.com/account/api-keys")
        print("   2. DELETE the exposed key: [REDACTED_FOR_SECURITY]")
        print("   3. Generate a NEW API key")
        print('   4. Update .env file: OPENAI_API_KEY="[YOUR_NEW_KEY_HERE]"')
        print("   5. Run this script again")
        return False

    print("🔧 Resolving alerts...")
    for alert in alerts:
        if alert["state"] == "open":
            success, error = resolve_alert(alert["number"])
            if success:
                print(f"✅ Resolved alert #{alert['number']}")
            else:
                # Redact sensitive info from error messages
                safe_error = redact_sensitive_info(error) if error else "Unknown error"
                print(f"❌ Failed to resolve alert #{alert['number']}: {safe_error}")
                return False

    print("🎉 All alerts resolved!")
    print(
        "🔄 GitHub will re-scan and the alerts should disappear within a few minutes."
    )
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
