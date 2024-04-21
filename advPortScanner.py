import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    20: 'FTP Data',
    21: 'FTP Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    139: 'NetBIOS',
    143: 'IMAP',
    443: 'HTTPS',
    445: 'SMB',
    993: 'IMAP SSL',
    995: 'POP3 SSL',
    1433: 'Microsoft SQL Server',
    1521: 'Oracle SQL',
    3306: 'MySQL',
    3389: 'RDP',
    5432: 'PostgreSQL',
    5900: 'VNC',
    8080: 'HTTP-Proxy'
}

def scan_port(ip, port, timeout):
    socket.setdefaulttimeout(timeout)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} ({COMMON_PORTS.get(port, 'Unknown')}) is open on {ip}")
    except Exception as e:
        print(f"Error on port {port} on {ip}: {e}")
    finally:
        s.close()

def main():
    parser = argparse.ArgumentParser(description='Advanced Port Scanner by w01f')
    parser.add_argument('--ips', type=str, required=True, help='Comma-separated list of IP addresses to scan')
    parser.add_argument('--ports', type=str, default="21,22,23,25,53,80,110,143,443,3306,3389,5900,8080", help='Comma-separated port numbers to scan')
    parser.add_argument('--timeout', type=int, default=1, help='Timeout in seconds for each port scan (default: 1)')
    parser.add_argument('--threads', type=int, default=100, help='Number of threads to use (default: 100)')
    args = parser.parse_args()

    ips = args.ips.split(',')
    ports = [int(port) for port in args.ports.split(',')]
    
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for ip in ips:
            for port in ports:
                executor.submit(scan_port, ip, port, args.timeout)

if __name__ == "__main__":
    main()
