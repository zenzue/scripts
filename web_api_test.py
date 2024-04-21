import subprocess
import argparse
import os

def run_locust_test(url, users, spawn_rate, test_duration):
    """Runs a Locust load test."""
    command = f"locust -f locustfile.py --headless -u {users} -r {spawn_rate} --run-time {test_duration} --host {url}"
    subprocess.run(command, shell=True)

def run_rate_limit_test(url, request_count):
    """Performs a burst of requests to test rate limiting."""
    import requests
    responses = [requests.get(url) for _ in range(request_count)]
    rate_limit_exceeded = sum(1 for response in responses if response.status_code == 429)
    print(f"Rate Limit Test Result: {rate_limit_exceeded} rate limit responses out of {request_count}")

def run_vulnerability_scan(url):
    """Runs a vulnerability scan using OWASP ZAP."""
    zap_path = "/path/to/zap.sh"
    command = f"{zap_path} -cmd -quickurl {url} -quickout zap_report.xml"
    subprocess.run(command, shell=True)
    print("Vulnerability Scan Complete: See zap_report.xml for details.")

def main():
    parser = argparse.ArgumentParser(description='Advanced Strength Test for Web and API Servers')
    parser.add_argument('--url', required=True, help='URL to test')
    parser.add_argument('--locust_users', type=int, default=100, help='Number of simulated users for load testing')
    parser.add_argument('--locust_spawn_rate', type=int, default=10, help='Rate to spawn users')
    parser.add_argument('--test_duration', type=str, default="1m", help='Duration for the load test (e.g., 1m, 10m)')
    parser.add_argument('--rate_test_count', type=int, default=100, help='Number of requests for rate limit testing')
    args = parser.parse_args()

    print("Starting Load Test with Locust...")
    run_locust_test(args.url, args.locust_users, args.locust_spawn_rate, args.test_duration)

    print("Starting Rate Limit Test...")
    run_rate_limit_test(args.url, args.rate_test_count)

    print("Starting Vulnerability Scan with OWASP ZAP...")
    run_vulnerability_scan(args.url)

if __name__ == "__main__":
    main()

# python advanced_strength_test.py --url http://example.com --locust_users 500 --locust_spawn_rate 20 --test_duration 10m --rate_test_count 200
# https://github.com/zaproxy/zaproxy

