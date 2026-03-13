
# Linux Log Analyzer

A Python tool that analyzes Linux log files and extracts security-relevant events such as failed SSH logins, errors, and suspicious IPs.

## Features

- Detect failed SSH login attempts
- Count errors in logs
- Identify top attacking IP addresses

## Supported Log Files

This tool works with **text-based log files**. Examples include:

| Log File | Description | Notes |
|----------|------------|-------|
| `/var/log/auth.log` | Authentication events (SSH logins, sudo) | Best for failed login and IP detection |
| `/var/log/secure` | Authentication events on some distros | Same as `auth.log` |
| `/var/log/syslog` | General system messages | Can extract errors and warnings |
| `/var/log/kern.log` | Kernel messages | Useful for system errors |
| `/var/log/apache2/access.log` | Apache access logs | Detect suspicious IPs hitting your website |
| `/var/log/apache2/error.log` | Apache error logs | Count errors and warnings |

**Note**: Some system logs require root permissions to read.

## Usage

```bash
python analyzer.py --file /var/log/auth.log
````

Example output:

```
Log Analysis Report
-------------------
Total lines: 5000
Errors: 23
Failed SSH logins: 42

Top attacking IPs:
192.168.1.10 -> 12 attempts
10.0.0.5 -> 7 attempts
```



