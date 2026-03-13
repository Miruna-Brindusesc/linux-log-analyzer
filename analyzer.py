import argparse
from utils import load_log_file
from parser import find_errors, find_failed_logins, extract_ips


def main():
    parser = argparse.ArgumentParser(description="Linux Log Analyzer")

    parser.add_argument(
        "--file",
        required=True,
        help="Path to log file"
    )

    args = parser.parse_args()

    lines = load_log_file(args.file)

    if not lines:
        return

    errors = find_errors(lines)
    failed_logins = find_failed_logins(lines)
    ip_counts = extract_ips(failed_logins)

    print("\nLog Analysis Report")
    print("-------------------")
    print("Total lines:", len(lines))
    print("Errors:", len(errors))
    print("Failed SSH logins:", len(failed_logins))

    print("\nTop attacking IPs:")

    for ip, count in ip_counts.most_common(5):
        print(f"{ip} -> {count} attempts")


if __name__ == "__main__":
    main()