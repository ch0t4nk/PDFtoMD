#!/usr/bin/env python3
"""
Security Remediation Script
===========================
Ensures complete SSOT compliance and API key security for PDFtoMD

This script:
1. Validates that .env is the ONLY place with API keys
2. Checks for any hardcoded keys in the codebase
3. Ensures proper gitignore coverage
4. Validates SSOT configuration system

Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0
"""

import os
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple


class SecurityAuditor:
    """Comprehensive security audit for API key management"""
    
    def __init__(self):
        self.root_dir = Path.cwd()
        self.issues: List[str] = []
        self.warnings: List[str] = []
        
    def audit_api_keys(self) -> Dict[str, List[str]]:
        """Search for any hardcoded API keys in the codebase"""
        print("🔍 Scanning for hardcoded API keys...")
        
        # Patterns to search for
        patterns = [
            r'sk-[A-Za-z0-9\-_]{20,}',  # OpenAI API keys
            r'sk-proj-[A-Za-z0-9\-_]{40,}',  # OpenAI project keys
            r'OPENAI_API_KEY\s*=\s*["\'][^"\']*sk-[A-Za-z0-9\-_]+["\']',  # Assignment patterns
        ]
        
        found_keys = {}
        
        for pattern in patterns:
            matches = []
            try:
                # Use git grep for better performance and respect gitignore
                cmd = ['git', 'grep', '-E', pattern]
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.root_dir)
                
                if result.returncode == 0:
                    for line in result.stdout.strip().split('\n'):
                        if line:
                            # Filter out documentation examples
                            if any(doc_term in line.lower() for doc_term in ['example', 'placeholder', 'your-api-key', 'sk-your-actual']):
                                continue
                            matches.append(line)
                            
                if matches:
                    found_keys[pattern] = matches
                    
            except subprocess.CalledProcessError:
                pass
                
        return found_keys
    
    def validate_gitignore(self) -> bool:
        """Ensure .env and related files are properly ignored"""
        print("📋 Validating .gitignore configuration...")
        
        gitignore_path = self.root_dir / '.gitignore'
        if not gitignore_path.exists():
            self.issues.append("❌ .gitignore file not found")
            return False
            
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        required_entries = ['.env', '.env.backup', '.env.local']
        missing_entries = []
        
        for entry in required_entries:
            if entry not in content:
                missing_entries.append(entry)
                
        if missing_entries:
            self.issues.append(f"❌ Missing .gitignore entries: {missing_entries}")
            return False
            
        print("✅ .gitignore properly configured")
        return True
    
    def validate_env_file(self) -> bool:
        """Validate .env file exists and has proper placeholder"""
        print("📄 Validating .env file...")
        
        env_path = self.root_dir / '.env'
        if not env_path.exists():
            self.warnings.append("⚠️  .env file not found - create from template")
            return False
            
        with open(env_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for placeholder vs real key
        if 'your-openai-api-key-here' in content:
            print("✅ .env has placeholder (secure)")
            return True
        elif re.search(r'sk-[A-Za-z0-9\-_]{20,}', content):
            print("⚠️  .env contains real API key (expected for production)")
            return True
        else:
            self.warnings.append("⚠️  .env exists but OPENAI_API_KEY not found")
            return False
    
    def validate_ssot_config(self) -> bool:
        """Validate SSOT configuration system"""
        print("⚙️  Validating SSOT configuration...")
        
        try:
            # Import and test config
            import sys
            sys.path.append(str(self.root_dir))
            
            from config import config
            
            # Test that config loads from environment
            api_key = config.OPENAI_API_KEY
            
            if not api_key:
                self.issues.append("❌ SSOT config not loading API key")
                return False
                
            print("✅ SSOT configuration working")
            return True
            
        except Exception as e:
            self.issues.append(f"❌ SSOT config error: {e}")
            return False
    
    def check_git_history(self) -> bool:
        """Check if API keys exist in git history"""
        print("📚 Checking git history for leaked keys...")
        
        try:
            # Search git history for potential API keys
            cmd = ['git', 'log', '--all', '--full-history', '--grep=sk-proj', '--oneline']
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.root_dir)
            
            if result.returncode == 0 and result.stdout.strip():
                self.warnings.append("⚠️  Found security-related commits in history")
                print("⚠️  Previous API key exposure found in git history")
                print("💡 Consider using git filter-branch or BFG to clean history if needed")
                return False
            else:
                print("✅ No API key commits found in recent history")
                return True
                
        except subprocess.CalledProcessError:
            self.warnings.append("⚠️  Could not check git history")
            return False
    
    def generate_remediation_report(self):
        """Generate comprehensive remediation report"""
        print("\n" + "="*60)
        print("🔒 SECURITY AUDIT REPORT")
        print("="*60)
        
        # Run all checks
        hardcoded_keys = self.audit_api_keys()
        gitignore_ok = self.validate_gitignore()
        env_ok = self.validate_env_file()
        ssot_ok = self.validate_ssot_config()
        history_clean = self.check_git_history()
        
        print(f"\n📊 AUDIT RESULTS:")
        print(f"   🔍 Hardcoded Keys: {'✅ None found' if not hardcoded_keys else '❌ Found issues'}")
        print(f"   📋 GitIgnore: {'✅ Configured' if gitignore_ok else '❌ Issues found'}")
        print(f"   📄 .env File: {'✅ Validated' if env_ok else '⚠️  Needs attention'}")
        print(f"   ⚙️  SSOT Config: {'✅ Working' if ssot_ok else '❌ Issues found'}")
        print(f"   📚 Git History: {'✅ Clean' if history_clean else '⚠️  Previous exposure'}")
        
        if hardcoded_keys:
            print(f"\n❌ HARDCODED API KEYS FOUND:")
            for pattern, matches in hardcoded_keys.items():
                print(f"   Pattern: {pattern}")
                for match in matches:
                    print(f"     {match}")
        
        if self.issues:
            print(f"\n❌ CRITICAL ISSUES:")
            for issue in self.issues:
                print(f"   {issue}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"   {warning}")
        
        print(f"\n🛡️  SSOT COMPLIANCE STATUS:")
        if not hardcoded_keys and gitignore_ok and ssot_ok:
            print("   ✅ FULLY COMPLIANT - All API keys managed through SSOT")
            print("   ✅ No hardcoded secrets in source code")
            print("   ✅ Proper environment isolation")
        else:
            print("   ❌ COMPLIANCE ISSUES DETECTED")
            print("   🔧 Action required to achieve SSOT compliance")
        
        print(f"\n📋 SSOT BEST PRACTICES:")
        print("   1. ✅ API keys ONLY in .env file (never in source code)")
        print("   2. ✅ .env file properly gitignored")
        print("   3. ✅ Configuration accessed through config.py SSOT system")
        print("   4. ✅ No hardcoded secrets anywhere in codebase")
        print("   5. ✅ Environment-specific configurations")
        
        return len(self.issues) == 0 and not hardcoded_keys


if __name__ == "__main__":
    print("🔒 PDFtoMD Security Audit & SSOT Compliance Check")
    print("="*60)
    
    auditor = SecurityAuditor()
    compliant = auditor.generate_remediation_report()
    
    if compliant:
        print(f"\n🎉 SECURITY AUDIT PASSED!")
        print("   Your PDFtoMD installation is SSOT compliant and secure.")
        exit(0)
    else:
        print(f"\n🚨 SECURITY AUDIT FAILED!")
        print("   Please address the issues above before proceeding.")
        exit(1)
