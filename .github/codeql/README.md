# CodeQL Security Configuration for PDFtoMD

This directory contains the CodeQL security analysis configuration for the PDFtoMD project.

## 🛡️ Security Configuration Overview

### Files Structure
```
.github/codeql/
├── codeql-config.yml          # Main CodeQL configuration
├── python-security-queries.qls # Custom security query suite  
└── README.md                  # This documentation
```

## 🔧 Configuration Details

### `codeql-config.yml`
- **Languages**: Python
- **Query Suites**: security-extended, security-and-quality
- **Paths**: Focused on source code directories
- **Exclusions**: Build artifacts, documentation, temporary files

### `python-security-queries.qls`
- **Injection Attacks**: SQL, code, path injection detection
- **Authentication**: Hardcoded credentials, clear-text logging
- **File Security**: Unsafe shell commands, path traversal
- **Cryptography**: Weak crypto, insecure randomness
- **Web Security**: XSS, URL redirection vulnerabilities
- **Configuration**: URL sanitization, hostname validation

## 🚀 Security Analysis Features

### Automatic Scanning
- **Push Events**: Every commit to master/main/develop
- **Pull Requests**: All incoming PRs analyzed
- **Scheduled**: Weekly scans on Mondays at 2:30 AM UTC
- **Manual**: On-demand workflow dispatch

### Enhanced Security Queries
- **High Priority**: SQL injection, code injection, path injection
- **Medium Priority**: Weak cryptography, insecure randomness
- **Configuration**: URL validation, hostname checking
- **API Security**: Credential management, sensitive data logging

## 📊 Query Categories

### 🔴 Critical (Error Level)
- SQL injection vulnerabilities
- Code injection attacks
- Path traversal vulnerabilities  
- Unsafe deserialization
- Hardcoded credentials
- Incomplete URL sanitization

### 🟡 Warning Level
- Weak cryptographic algorithms
- Insecure random number generation
- Clear-text sensitive data logging
- URL redirection vulnerabilities
- Regex injection possibilities

## 🎯 Security Standards Compliance

### OWASP Top 10 Coverage
- ✅ **A01**: Broken Access Control
- ✅ **A02**: Cryptographic Failures  
- ✅ **A03**: Injection Vulnerabilities
- ✅ **A04**: Insecure Design Patterns
- ✅ **A05**: Security Misconfiguration
- ✅ **A06**: Vulnerable Components
- ✅ **A07**: Authentication Failures
- ✅ **A08**: Software/Data Integrity
- ✅ **A09**: Security Logging Failures
- ✅ **A10**: Server-Side Request Forgery

### Enterprise Security Features
- **API Key Protection**: Prevents hardcoded credentials
- **SSOT Compliance**: Validates configuration security
- **File Security**: Path traversal and injection prevention
- **Input Validation**: Comprehensive sanitization checks

## 🔍 Monitoring and Alerts

### GitHub Security Integration
- **Security Tab**: Results displayed in GitHub Security tab
- **Pull Request Checks**: Automatic PR security validation  
- **Email Notifications**: Security alerts for repository admins
- **SARIF Upload**: Standard security report format

### Custom Alert Configuration
- **High Severity**: Immediate notification
- **Medium Severity**: Daily digest
- **Low Severity**: Weekly summary
- **False Positive Management**: Query filtering configured

## 📈 Performance Optimization

### Scan Efficiency
- **Path Filtering**: Only scan relevant source code
- **Language Focus**: Python-specific optimizations
- **Query Selection**: Targeted security-relevant queries
- **Timeout Management**: 6-hour maximum per analysis

### Resource Management
- **Concurrent Analysis**: Multiple language support ready
- **Cache Optimization**: Database and dependency caching
- **Incremental Scanning**: Only changed files when possible

## 🛠️ Maintenance

### Regular Updates
- **Query Database**: Automatic CodeQL query updates
- **Security Patterns**: Monthly review of new vulnerabilities
- **Configuration Tuning**: Quarterly performance optimization
- **False Positive Review**: Continuous refinement

### Customization Guidelines
1. **Adding Queries**: Update `python-security-queries.qls`
2. **Path Changes**: Modify `codeql-config.yml` paths section
3. **Severity Adjustment**: Update query suite configurations
4. **Language Addition**: Extend matrix in workflow file

## 📚 Resources

- [CodeQL Documentation](https://codeql.github.com/docs/)
- [GitHub Code Scanning](https://docs.github.com/en/code-security/code-scanning)
- [Security Query Reference](https://codeql.github.com/codeql-query-help/)
- [SARIF Format Specification](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)

---

**🔒 Security Notice**: This configuration provides enterprise-grade security analysis. Any modifications should be reviewed by the security team to ensure continued protection against emerging threats.
