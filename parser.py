import re
from collections import Counter


def find_errors(lines):
    return [line for line in lines if "error" in line.lower()]


def find_failed_logins(lines):
    return [line for line in lines if "Failed password" in line]


def extract_ips(lines):
    ips = []

    for line in lines:
        match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
        if match:
            ips.append(match.group())

    return Counter(ips)