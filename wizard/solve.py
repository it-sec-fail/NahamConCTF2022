#!/usr/share/env python

from pwn import *

host,port = 'challenge.nahamcon.com', 30719

try:
    s = remote(host, port)
    s.recvuntil(b'binary string?')
    binary=s.recvuntil('\n')
    print(binary)
except:
    print("Couldn't connect... sorry")
