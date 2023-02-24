import shodan
import argparse

def scan_port(ip_address, port):
    try:
        api_key = "YOUR_SHODAN_API_KEY"
        api = shodan.Shodan(api_key)
        results = api.search('ip:' + ip_address)
        for result in results['matches']:
            host_ip = result['ip_str']
            print("Scanning port {} on host {}".format(port, host_ip))
            try:
                shodan_data = api.host(host_ip)
                if 'ports' in shodan_data:
                    if port in shodan_data['ports']:
                        print("Port {} is open on host {}".format(port, host_ip))
            except:
                pass
    except shodan.APIError as e:
        print('Error: {}'.format(e))

def main():
    parser = argparse.ArgumentParser(description='Advanced Port Scanner with Shodan by w01f @xai_yak')
    parser.add_argument('-i', '--ip', help='IP Address to scan', required=True)
    parser.add_argument('-p', '--port', help='Port to scan', required=True)
    args = parser.parse_args()
    scan_port(args.ip, int(args.port))

if __name__ == '__main__':
    main()
