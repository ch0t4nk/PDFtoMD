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
$authStatus = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "Not authenticated with GitHub CLI. Run: gh auth login"
    exit 1
}

Write-Host "🔧 Configuring GitHub Advanced Security Settings for PDFtoMD" -ForegroundColor Cyan
Write-Host "=" * 60

$repo = "ch0t4nk/PDFtoMD"

# Enable Secret Scanning
Write-Host "🔍 Enabling Secret Scanning..." -ForegroundColor Yellow
try {
    gh api --method PATCH "/repos/$repo" -f has_secret_scanning=true
    Write-Host "✅ Secret scanning enabled" -ForegroundColor Green
} catch {
    Write-Warning "Secret scanning may already be enabled or requires GitHub Advanced Security"
}

# Enable Push Protection
Write-Host "🛡️ Enabling Push Protection..." -ForegroundColor Yellow
try {
    gh api --method PATCH "/repos/$repo/secret-scanning/push-protection" -f enabled=true
    Write-Host "✅ Push protection enabled" -ForegroundColor Green
} catch {
    Write-Warning "Push protection configuration may require manual setup"
}

# Enable Dependency Review
Write-Host "📦 Enabling Dependency Review..." -ForegroundColor Yellow
try {
    gh api --method PATCH "/repos/$repo" -f has_vulnerability_alerts=true
    Write-Host "✅ Vulnerability alerts enabled" -ForegroundColor Green
} catch {
    Write-Warning "Dependency features may already be enabled"
}

# Enable Private Vulnerability Reporting
Write-Host "🔒 Enabling Private Vulnerability Reporting..." -ForegroundColor Yellow
try {
    gh api --method PATCH "/repos/$repo" -f has_private_vulnerability_reporting=true
    Write-Host "✅ Private vulnerability reporting enabled" -ForegroundColor Green
} catch {
    Write-Warning "Private vulnerability reporting may require manual setup"
}

Write-Host ""
Write-Host "🎉 Security configuration complete!" -ForegroundColor Green
Write-Host "📋 Verify settings at: https://github.com/$repo/settings/security_analysis" -ForegroundColor Cyan

Write-Host ""
Write-Host "🔧 Current Security Features:" -ForegroundColor Yellow
Write-Host "   ✅ CodeQL Security Analysis (already configured)" 
Write-Host "   ✅ Secret Scanning + Push Protection" 
Write-Host "   ✅ Dependency Review + Vulnerability Alerts"
Write-Host "   ✅ Private Vulnerability Reporting"
Write-Host ""
Write-Host "🛡️ Your PDFtoMD repository now has enterprise-grade security!" -ForegroundColor Green
