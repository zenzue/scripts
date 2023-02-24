#!/usr/bin/env python3

import shodan
import argparse
import re
import sys

def get_api_key():
    api_key = ''  # Enter your Shodan API key here
    if not api_key:
        print('[-] Shodan API key not found. Please provide one.')
        sys.exit(1)
    return api_key

def get_subdomains(domain):
    api_key = get_api_key()
    api = shodan.Shodan(api_key)
    query = 'hostname:*.{} -subdomain.{}'.format(domain, domain)
    try:
        results = api.search(query)
        subdomains = set()
        for result in results['matches']:
            domain_name = result['hostnames'][0]
            match = re.search(r'\w+\.' + domain + '$', domain_name)
            if match:
                subdomain = match.group()
                subdomains.add(subdomain)
        return subdomains
    except shodan.exception.APIError as e:
        print('[-] Error: {}'.format(e))
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Shodan subdomain scanner by w01f @xai_yak')
    parser.add_argument('-d', '--domain', required=True, help='Domain to scan for subdomains')
    args = parser.parse_args()

    subdomains = get_subdomains(args.domain)
    for subdomain in subdomains:
        print('[+] Found subdomain: {}'.format(subdomain))

if __name__ == '__main__':
    main()
