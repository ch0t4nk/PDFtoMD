# 🔒 Security Guide - MarkPDFDown

## 🛡️ Security Overview

MarkPDFDown v3.0+ implements comprehensive security measures to protect your API keys and sensitive information through the Single Source of Truth (SSOT) configuration system.

## 🔑 API Key Security

### ✅ **What We Do Right**

- **🔒 Never hardcode API keys** - All keys stored only in `.env` file
- **📋 Template system** - Share configuration structure safely with `.env.template`
- **🚫 Git exclusion** - `.env` file automatically ignored by git
- **🎯 Centralized management** - All API configuration through SSOT system
- **🧹 History cleanup** - Git history cleaned of any exposed keys

### ❌ **Legacy Security Issues (Fixed)**

- ~~API keys scattered in source code~~ → **Fixed**: Centralized in config.py
- ~~Manual environment variable setup~~ → **Fixed**: Automated SSOT system
- ~~Keys committed to git~~ → **Fixed**: Complete history cleanup
- ~~Hardcoded paths and settings~~ → **Fixed**: All settings centralized

## 🚀 Security Best Practices

### **Initial Setup**
```bash
# ✅ Always use the template

cp.env.template.env

# ✅ Edit.env with your real API key

# OPENAI_API_KEY="sk-your-real-key-here"

# ❌ Never edit source files directly
```
### **Key Rotation**
```bash
# When rotating API keys:

# Revoke old key from OpenAI dashboard

# Generate new key

# Update.env file only

# Test with: python config.py
```
### **Version Control**
```bash
# ✅.env is automatically ignored

git status #.env should not appear

# ❌ Never force-add.env

# git add -f.env # DON'T DO THIS
```
## 🔍 Security Validation

### Test Your Setup
```bash
# Check configuration loads correctly

python config.py

# Verify no API keys in source code

grep -r "sk-proj" src/ tools/ config/

# Should return no results

# Verify.env is gitignored

git check-ignore.env

# Should output:.env
```
### Validate Environment
```bash
# Ensure.env exists and has proper permissions

ls -la.env

# Should show: -rw--- (600 permissions recommended)

# Check for API key pattern

grep "OPENAI_API_KEY".env

# Should show: OPENAI_API_KEY="sk-..."
```
## 🚨 Security Incident Response

### If API Key is Exposed

1. **Immediate Actions:**
 `bash
 # 1. Revoke the exposed key immediately
 # Go to https://platform.openai.com/api-keys

 # 2. Generate new API key

 # 3. Update.env file
 echo 'OPENAI_API_KEY="sk-new-key-here"' >.env

 # 4. Test new configuration
 python config.py
```
2. **Git History Cleanup:**
 `bash
 # If key was committed to git:
 # Use BFG Repo-Cleaner or git filter-branch
 # Contact team for history rewrite procedures
```
3. **Verification:**
 `bash
 # Verify no traces remain
 git log --all -p -S "sk-proj" --since="1 month ago"
 # Should return no results
```
## 📋 Security Checklist

- [ ] `.env` file exists and contains your API key
- [ ] `.env` is listed in `.gitignore`
- [ ] No API keys hardcoded in source files
- [ ] `python config.py` shows "✅ Configured"
- [ ] All tools use SSOT configuration system
- [ ] Old API keys have been revoked
- [ ] Git history contains no exposed keys

## 🤝 Team Security

### For Team Environments

1. **Never share.env files directly**
2. **Use.env.template for onboarding**
3. **Each developer has their own API key**
4. **Regularly rotate API keys**
5. **Monitor API usage for anomalies**

### Example Team Workflow
```bash
# New team member setup:

# Clone repository

git clone https://github.com/ch0t4nk/PDFtoMD.git

# Copy template

cp.env.template.env

# Get personal API key from team lead

# Configure.env with personal key

# Test setup

python config.py

# Never commit.env

# (Already gitignored)
```
## 📞 Support

If you discover a security issue:

1. **DO NOT** open a public issue
2. **DO NOT** commit any fixes that might expose details
3. Contact the maintainers privately
4. Follow responsible disclosure practices

## 🔐 Additional Resources

- [OpenAI API Security Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)
- [Git Security Guidelines](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure)
- [Environment Variable Security](https://12factor.net/config)

- --

- *Remember: Security is everyone's responsibility. When in doubt, ask for help rather than risk exposure.**
