#!/usr/bin/env python3
"""
GitHub Secret Scanning Alert Resolution
======================================
Helps resolve the OpenAI API key exposure alert
"""

import subprocess
import json
import sys
from pathlib import Path

def check_github_cli():
    """Check if GitHub CLI is available"""
    try:
        result = subprocess.run(['gh', '--version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def get_secret_alerts():
    """Get current secret scanning alerts"""
    try:
        result = subprocess.run(
            ['gh', 'api', '/repos/ch0t4nk/PDFtoMD/secret-scanning/alerts'],
            capture_output=True, text=True
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
            "resolution_comment": "API key has been revoked and replaced. Codebase cleaned of all hardcoded secrets."
        }
        
        result = subprocess.run([
            'gh', 'api', '--method', 'PATCH',
            f'/repos/ch0t4nk/PDFtoMD/secret-scanning/alerts/{alert_number}',
            '--input', '-'
        ], input=json.dumps(data), text=True, capture_output=True)
        
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
        print(f"   Alert #{alert['number']}: {alert['secret_type_display_name']}")
        print(f"   State: {alert['state']}")
        print(f"   Created: {alert['created_at']}")
        print(f"   File: {alert['first_location_detected']['path']}")
        print(f"   Line: {alert['first_location_detected']['start_line']}")
        print()
    
    print("🚨 CRITICAL: Before resolving alerts, ensure you have:")
    print("   1. ✅ REVOKED the exposed API key in OpenAI dashboard")
    print("   2. ✅ Generated a NEW API key")
    print("   3. ✅ Updated your .env file with the new key")
    print("   4. ✅ Verified no hardcoded keys remain in codebase")
    print()
    
    response = input("Have you completed ALL the above steps? (yes/no): ")
    if response.lower() != 'yes':
        print("⚠️  Please complete the security steps first!")
        print("📋 Instructions:")
        print("   1. Go to: https://platform.openai.com/account/api-keys")
        print("   2. DELETE the exposed key: sk-proj-h7PUbN7JHwjcaXbU1Du...")
        print("   3. Generate a NEW API key")
        print("   4. Update .env file: OPENAI_API_KEY=\"your-new-key-here\"")
        print("   5. Run this script again")
        return False
    
    print("🔧 Resolving alerts...")
    for alert in alerts:
        if alert['state'] == 'open':
            success, error = resolve_alert(alert['number'])
            if success:
                print(f"✅ Resolved alert #{alert['number']}")
            else:
                print(f"❌ Failed to resolve alert #{alert['number']}: {error}")
                return False
    
    print("🎉 All alerts resolved!")
    print("🔄 GitHub will re-scan and the alerts should disappear within a few minutes.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
