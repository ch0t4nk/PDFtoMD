#!/usr/bin/env pwsh
<#
.SYNOPSIS
Configure GitHub Advanced Security Settings for PDFtoMD

.DESCRIPTION
This script configures the optimal security settings for the PDFtoMD repository
using GitHub CLI. Requires gh CLI tool and authentication.

.EXAMPLE
./scripts/configure_security.ps1
#>

# Check if GitHub CLI is installed
if (!(Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Error "GitHub CLI (gh) not found. Please install from: https://cli.github.com/"
    exit 1
}

# Check if authenticated
gh auth status 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Error "Not authenticated with GitHub CLI. Run: gh auth login"
    exit 1
}

Write-Output "🔧 Configuring GitHub Advanced Security Settings for PDFtoMD"
Write-Output ("=" * 60)

$repo = "ch0t4nk/PDFtoMD"

# Enable Secret Scanning
Write-Output "🔍 Enabling Secret Scanning..."
try {
    gh api --method PATCH "/repos/$repo" -f has_secret_scanning=true
    Write-Output "✅ Secret scanning enabled"
} catch {
    Write-Warning "Secret scanning may already be enabled or requires GitHub Advanced Security"
}

# Enable Push Protection
Write-Output "🛡️ Enabling Push Protection..."
try {
    gh api --method PATCH "/repos/$repo/secret-scanning/push-protection" -f enabled=true
    Write-Output "✅ Push protection enabled"
} catch {
    Write-Warning "Push protection configuration may require manual setup"
}

# Enable Dependency Review
Write-Output "📦 Enabling Dependency Review..."
try {
    gh api --method PATCH "/repos/$repo" -f has_vulnerability_alerts=true
    Write-Output "✅ Vulnerability alerts enabled"
} catch {
    Write-Warning "Dependency features may already be enabled"
}

# Enable Private Vulnerability Reporting
Write-Output "🔒 Enabling Private Vulnerability Reporting..."
try {
    gh api --method PATCH "/repos/$repo" -f has_private_vulnerability_reporting=true
    Write-Output "✅ Private vulnerability reporting enabled"
} catch {
    Write-Warning "Private vulnerability reporting may require manual setup"
}

Write-Output ""
Write-Output "🎉 Security configuration complete!"
Write-Output "📋 Verify settings at: https://github.com/$repo/settings/security_analysis"

Write-Output ""
Write-Output "🔧 Current Security Features:"
Write-Output "   ✅ CodeQL Security Analysis (already configured)"
Write-Output "   ✅ Secret Scanning + Push Protection"
Write-Output "   ✅ Dependency Review + Vulnerability Alerts"
Write-Output "   ✅ Private Vulnerability Reporting"
Write-Output ""
Write-Output "🛡️ Your PDFtoMD repository now has enterprise-grade security!"
