#!/usr/bin/env python3

import sys
import argparse
import urllib.request
from urllib.error import URLError, HTTPError
import socket

SERVICE_STATUS = {
    'OK': 0,
    'WARNING': 1,
    'CRITICAL': 2,
    'UNKNOWN': 3
}

def main(argv):
    parser = argparse.ArgumentParser(description='Check BP status')
    parser.add_argument('-H', '--host', default='localhost',
                       help='IP or hostname to check. default = localhost')
    parser.add_argument('-p', '--http_port', type=int, default=8888,
                       help='HTTP port number. default = 8888')
    parser.add_argument('-p2', '--p2p_port', type=int, default=9876,
                       help='P2P port number. default = 9876')
    parser.add_argument('-c', '--check_list', help='Comma separated list of checks to perform. Choices: [http,p2p]. If empty, it performs all the checks')
    args = parser.parse_args()
    HOST = args.host
    HTTP_PORT = args.http_port
    P2P_PORT = args.p2p_port
    CHECK_LIST = args.check_list.split(',') if args.check_list else None

    if not CHECK_LIST or 'http' in CHECK_LIST:
        try:
            response = urllib.request.urlopen('http://{}:{}/v1/chain/get_info'.format(HOST, HTTP_PORT))
            j_response = response.read()
        except HTTPError as e:
            print('HTTP CRITICAL: The server couldn\'t fulfill the request. Error code: {}'.format(e.code))
            sys.exit(SERVICE_STATUS['CRITICAL'])
        except URLError as e:
            print('HTTP CRITICAL: Failed to reach server. Reason: {}'.format(e.reason))
            sys.exit(SERVICE_STATUS['CRITICAL'])

    if not CHECK_LIST or 'p2p' in CHECK_LIST:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((HOST, P2P_PORT))
        if result != 0:
            print('P2P CRITICAL: P2P service DOWN')
            sys.exit(SERVICE_STATUS['CRITICAL'])

    print('BP Services OK')
    sys.exit(SERVICE_STATUS['OK'])

if __name__ == "__main__":
    main(sys.argv)
