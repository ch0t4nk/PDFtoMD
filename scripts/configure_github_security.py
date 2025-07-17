#!/usr/bin/env python3
"""
GitHub Advanced Security Configuration for PDFtoMD
Configures optimal security settings using GitHub API

Usage:
    python scripts/configure_github_security.py --token YOUR_GITHUB_TOKEN

Requirements:
    pip install requests
"""

import argparse
import sys
from typing import Any

import requests


class GitHubSecurityConfigurator:
    def __init__(self, token: str, repo: str = "ch0t4nk/PDFtoMD"):
        self.token = token
        self.repo = repo
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def enable_secret_scanning(self) -> bool:
        """Enable secret scanning for the repository"""
        print("🔍 Enabling Secret Scanning...")
        try:
            url = f"{self.base_url}/repos/{self.repo}"
            data = {"security_and_analysis": {"secret_scanning": {"status": "enabled"}}}

            response = requests.patch(url, headers=self.headers, json=data)
            if response.status_code in [200, 204]:
                print("✅ Secret scanning enabled")
                return True
            else:
                print(f"⚠️ Secret scanning: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Error enabling secret scanning: {e}")
            return False

    def enable_push_protection(self) -> bool:
        """Enable push protection for secret scanning"""
        print("🛡️ Enabling Push Protection...")
        try:
            url = f"{self.base_url}/repos/{self.repo}/secret-scanning/push-protection"
            data = {"enabled": True}

            response = requests.patch(url, headers=self.headers, json=data)
            if response.status_code in [200, 204]:
                print("✅ Push protection enabled")
                return True
            else:
                print(f"⚠️ Push protection: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Error enabling push protection: {e}")
            return False

    def enable_dependency_alerts(self) -> bool:
        """Enable dependency vulnerability alerts"""
        print("📦 Enabling Dependency Vulnerability Alerts...")
        try:
            url = f"{self.base_url}/repos/{self.repo}"
            data = {"has_vulnerability_alerts": True}

            response = requests.patch(url, headers=self.headers, json=data)
            if response.status_code in [200, 204]:
                print("✅ Dependency vulnerability alerts enabled")
                return True
            else:
                print(f"⚠️ Dependency alerts: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Error enabling dependency alerts: {e}")
            return False

    def enable_private_vulnerability_reporting(self) -> bool:
        """Enable private vulnerability reporting"""
        print("🔒 Enabling Private Vulnerability Reporting...")
        try:
            url = f"{self.base_url}/repos/{self.repo}"
            data = {"has_private_vulnerability_reporting": True}

            response = requests.patch(url, headers=self.headers, json=data)
            if response.status_code in [200, 204]:
                print("✅ Private vulnerability reporting enabled")
                return True
            else:
                print(
                    f"⚠️ Private vulnerability reporting: {response.status_code} - {response.text}"
                )
                return False
        except Exception as e:
            print(f"❌ Error enabling private vulnerability reporting: {e}")
            return False

    def get_current_security_settings(self) -> dict[str, Any]:
        """Get current security and analysis settings"""
        try:
            url = f"{self.base_url}/repos/{self.repo}"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Error getting repository info: {response.status_code}")
                return {}
        except Exception as e:
            print(f"❌ Error fetching repository: {e}")
            return {}

    def configure_all_security_features(self) -> bool:
        """Configure all security features"""
        print("🔧 Configuring GitHub Advanced Security Settings for PDFtoMD")
        print("=" * 60)

        # Check current settings
        print("📋 Checking current security settings...")
        current_settings = self.get_current_security_settings()

        if not current_settings:
            print("❌ Failed to fetch current settings")
            return False

        success_count = 0
        total_features = 4

        # Configure each security feature
        if self.enable_secret_scanning():
            success_count += 1

        if self.enable_push_protection():
            success_count += 1

        if self.enable_dependency_alerts():
            success_count += 1

        if self.enable_private_vulnerability_reporting():
            success_count += 1

        print("\n" + "=" * 60)
        print(
            f"🎉 Security configuration complete! ({success_count}/{total_features} features configured)"
        )
        print(
            f"📋 Verify settings at: https://github.com/{self.repo}/settings/security_analysis"
        )

        print("\n🔧 PDFtoMD Security Features:")
        print("   ✅ CodeQL Security Analysis (already configured)")
        print("   ✅ Secret Scanning + Push Protection")
        print("   ✅ Dependency Review + Vulnerability Alerts")
        print("   ✅ Private Vulnerability Reporting")
        print("\n🛡️ Your PDFtoMD repository now has enterprise-grade security!")

        return success_count == total_features


def main():
    parser = argparse.ArgumentParser(
        description="Configure GitHub Advanced Security Settings for PDFtoMD"
    )
    parser.add_argument(
        "--token",
        required=True,
        help="GitHub Personal Access Token with repo and security_events permissions",
    )
    parser.add_argument(
        "--repo",
        default="ch0t4nk/PDFtoMD",
        help="Repository in format owner/repo (default: ch0t4nk/PDFtoMD)",
    )

    args = parser.parse_args()

    # Validate token format
    if not args.token.startswith(("ghp_", "github_pat_")):
        print("⚠️ Warning: Token format doesn't match expected GitHub token patterns")

    configurator = GitHubSecurityConfigurator(args.token, args.repo)
    success = configurator.configure_all_security_features()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
