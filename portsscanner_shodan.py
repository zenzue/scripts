import shodan

SHODAN_API_KEY = "<YOUR_SHODAN_API_KEY>"

def scan_ports(ip):
    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        results = api.scan(ip, ports="1-65535")
        data = api.host(ip)
        print(f"IP: {ip}")
        print(f"Organization: {data.get('org', 'N/A')}")
        print(f"Operating System: {data.get('os', 'N/A')}")
        print(f"Open Ports: {', '.join([str(port) for port in results['ports']])}")
    except shodan.APIError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Scan open ports of an IP address using Shodan by w01f @xai_yak')
    parser.add_argument('ip', help='IP address to scan')
    
    args = parser.parse_args()
    scan_ports(args.ip)

