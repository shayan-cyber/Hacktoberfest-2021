"""
This is a simple script for get open ports in determinate target.
"""

import sys
import socket


def get_ports(ip_address):
    """
    This is main function responsible for get open ports of target ip.
    """
    ip_address = sys.argv[1]

    for ports in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if sock.connect_ex((ip_address, ports)) == 0:
            print(f"Port {ports} is open!")
            sock.close()
        else:
            print(f"Port {ports} is closed!")
            sock.close()


if __name__ == "__main__":
    get_ports(sys.argv[1])
