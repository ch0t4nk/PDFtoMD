#!/usr/bin/env python3
"""
MarkPDFDown SSOT Migration Script
=================================

This script helps migrate existing code to use the new centralized configuration system.
It will update import statements and replace hardcoded values with config references.

Usage:
    python migrate_to_ssot.py [--dry-run] [--backup]
    
Options:
    --dry-run    Show what would be changed without making changes
    --backup     Create backup files before making changes
"""

import re
import argparse
from pathlib import Path
from typing import List, Tuple, Dict

def get_python_files() -> List[Path]:
    """Get all Python files in the project"""
    python_files = []
    
    # Search in main directories
    for directory in ["src", "tools", "config"]:
        if Path(directory).exists():
            python_files.extend(Path(directory).rglob("*.py"))
    
    # Also check root directory Python files
    python_files.extend(Path(".").glob("*.py"))
    
    # Filter out this migration script and config.py
    python_files = [f for f in python_files if f.name not in ["migrate_to_ssot.py", "config.py"]]
    
    return python_files

def analyze_file(file_path: Path) -> Dict[str, List[str]]:
    """Analyze a file for patterns that need updating"""
    issues = {
        "env_access": [],
        "hardcoded_paths": [],
        "missing_config_import": [],
        "old_config_patterns": []
    }
    
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.splitlines()
        
        has_config_import = "from config import" in content or "import config" in content
        
        for i, line in enumerate(lines, 1):
            # Check for direct environment variable access
            if re.search(r'os\.getenv\(["\']OPENAI_', line):
                issues["env_access"].append(f"Line {i}: {line.strip()}")
            
            # Check for hardcoded paths
            if re.search(r'["\']pdfs["\']|["\']outputs["\']|["\']converted["\']|["\']temp["\']', line):
                if not line.strip().startswith("#") and "default" not in line.lower():
                    issues["hardcoded_paths"].append(f"Line {i}: {line.strip()}")
            
            # Check for old config patterns
            if re.search(r'load_dotenv\(\)|from dotenv import load_dotenv', line):
                if not has_config_import:
                    issues["old_config_patterns"].append(f"Line {i}: {line.strip()}")
        
        # Check if file needs config import
        if (issues["env_access"] or issues["hardcoded_paths"]) and not has_config_import:
            issues["missing_config_import"].append("File needs config import")
            
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
    
    return issues

def create_migration_plan(file_path: Path, issues: Dict[str, List[str]]) -> List[Tuple[str, str, str]]:
    """Create a migration plan for a file"""
    migrations = []
    
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Add config import if needed
        if issues["missing_config_import"]:
            # Find where to insert import
            lines = content.splitlines()
            import_insert_line = 0
            
            for i, line in enumerate(lines):
                if line.startswith("import ") or line.startswith("from "):
                    import_insert_line = i + 1
            
            migrations.append((
                "ADD_IMPORT",
                f"After line {import_insert_line}",
                "from config import config"
            ))
        
        # Replace environment variable access
        replacements = {
            r'os\.getenv\(["\']OPENAI_API_KEY["\'][^)]*\)': 'config.OPENAI_API_KEY',
            r'os\.getenv\(["\']OPENAI_API_BASE["\'][^)]*\)': 'config.OPENAI_API_BASE',
            r'os\.getenv\(["\']OPENAI_DEFAULT_MODEL["\'][^)]*\)': 'config.OPENAI_DEFAULT_MODEL',
            r'["\']pdfs["\']': 'str(config.DEFAULT_PDF_FOLDER)',
            r'["\']outputs["\']': 'str(config.DEFAULT_OUTPUT_FOLDER)',
            r'["\']converted["\']': 'str(config.DEFAULT_CONVERTED_FOLDER)',
            r'["\']temp["\']': 'str(config.DEFAULT_TEMP_FOLDER)',
        }
        
        for pattern, replacement in replacements.items():
            if re.search(pattern, content):
                migrations.append((
                    "REPLACE",
                    pattern,
                    replacement
                ))
        
    except Exception as e:
        print(f"Error creating migration plan for {file_path}: {e}")
    
    return migrations

def apply_migrations(file_path: Path, migrations: List[Tuple[str, str, str]], backup: bool = False) -> bool:
    """Apply migrations to a file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        # Create backup if requested
        if backup:
            backup_path = file_path.with_suffix(f"{file_path.suffix}.backup")
            backup_path.write_text(original_content, encoding='utf-8')
            print(f"  💾 Backup created: {backup_path}")
        
        # Apply migrations
        for migration_type, pattern, replacement in migrations:
            if migration_type == "ADD_IMPORT":
                lines = content.splitlines()
                # Find the right place to add import
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith("import ") or line.startswith("from "):
                        insert_pos = i + 1
                
                lines.insert(insert_pos, replacement)
                content = "\n".join(lines)
                
            elif migration_type == "REPLACE":
                content = re.sub(pattern, replacement, content)
        
        # Write updated content
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            return True
        
    except Exception as e:
        print(f"  ❌ Error applying migrations to {file_path}: {e}")
        return False
    
    return False

def main():
    parser = argparse.ArgumentParser(description="Migrate MarkPDFDown code to use SSOT configuration")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be changed without making changes")
    parser.add_argument("--backup", action="store_true", help="Create backup files before making changes")
    
    args = parser.parse_args()
    
    print("🔧 MarkPDFDown SSOT Migration Tool")
    print("=" * 50)
    
    # Get all Python files
    python_files = get_python_files()
    print(f"📁 Found {len(python_files)} Python files to analyze")
    
    files_to_migrate = []
    total_issues = 0
    
    # Analyze all files
    print("\n🔍 Analyzing files...")
    for file_path in python_files:
        issues = analyze_file(file_path)
        issue_count = sum(len(issue_list) for issue_list in issues.values())
        
        if issue_count > 0:
            files_to_migrate.append((file_path, issues))
            total_issues += issue_count
            print(f"  📄 {file_path}: {issue_count} issues found")
    
    if not files_to_migrate:
        print("\n✅ No migration needed - all files already use SSOT configuration!")
        return
    
    print(f"\n📊 Migration Summary:")
    print(f"  📄 Files to migrate: {len(files_to_migrate)}")
    print(f"  🔧 Total issues: {total_issues}")
    
    # Show detailed analysis
    for file_path, issues in files_to_migrate:
        print(f"\n📄 {file_path}:")
        for issue_type, issue_list in issues.items():
            if issue_list:
                print(f"  🔸 {issue_type}: {len(issue_list)} issues")
                for issue in issue_list[:3]:  # Show first 3 issues
                    print(f"    - {issue}")
                if len(issue_list) > 3:
                    print(f"    - ... and {len(issue_list) - 3} more")
    
    # Apply migrations if not dry run
    if not args.dry_run:
        print(f"\n🚀 Applying migrations...")
        
        migrated_count = 0
        for file_path, issues in files_to_migrate:
            migrations = create_migration_plan(file_path, issues)
            if migrations:
                print(f"  📄 Migrating {file_path}...")
                if apply_migrations(file_path, migrations, args.backup):
                    migrated_count += 1
                    print(f"    ✅ Migration complete")
                else:
                    print(f"    ⚠️  No changes needed")
        
        print(f"\n✅ Migration complete!")
        print(f"  📄 Files migrated: {migrated_count}/{len(files_to_migrate)}")
        
        print(f"\n📋 Next steps:")
        print(f"  1. Test your application to ensure everything works")
        print(f"  2. Remove any unused import statements")
        print(f"  3. Update your .env file with the new template")
        print(f"  4. Run: python config.py  # to test configuration")
        
    else:
        print(f"\n💡 Dry run complete. Run without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
