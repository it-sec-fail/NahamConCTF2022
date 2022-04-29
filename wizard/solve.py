#!/usr/share/env python

from pwn import *
import binascii
import base64
import struct
import time

host,port = 'challenge.nahamcon.com', 31997

p = log.progress('Working')

try:
    s = remote(host, port)

    p.status('First question - binary to ascii...')
    s.recvuntil(b'binary string?')
    binary_string=s.recv().split()
    binary_string=binary_string[0].decode('utf-8')
    hex_s=hex(int(binary_string,2))
    ascii_text=bytes.fromhex(hex_s[2:]).decode("utf-8")
    s.sendline(bytes(ascii_text,'latin1'))
    time.sleep(1)
    p.status('First question - done!')
    time.sleep(1)

    p.status('Second question - hex to ascii...')
    time.sleep(1)
    s.recvuntil(b'hex string?')
    string=s.recv().split()
    string=string[0].decode('utf-8')
    ascii_text=bytes.fromhex(string).decode('utf-8')
    s.sendline(bytes(ascii_text,'latin1'))
    p.status('Second question - done!')
    time.sleep(1)

    p.status('Third question - octal to ascii')
    time.sleep(1)
    s.recvuntil(b'octal string?')
    string=s.recv().split()
    string=string[8].decode('utf-8')
    string=hex(int(string,8))
    ascii_text=bytes.fromhex(string[2:]).decode('utf-8')
    s.sendline(bytes(ascii_text,'latin1'))
    p.status('Third question - done!')
    time.sleep(1)

    p.status('Fourth question - int to ascii')
    time.sleep(1)
    s.recvuntil(b'this integer?')
    string=s.recv().split()
    string=string[6].decode('utf-8')
    string=hex(int(string))
    ascii_text=bytes.fromhex(string[2:]).decode('utf-8')
    s.sendline(bytes(ascii_text,'latin1'))
    p.status('Fourth question - done!')
    time.sleep(1)

    p.status('Fifth question - decoding base64 string...')
    time.sleep(1)
    s.recvuntil(b'Base64 string?')
    string=s.recv().split()
    string=string[0].decode('utf-8')
    ascii_text=base64.b64decode(string)
    s.sendline(ascii_text)
    p.status('Fifth questions - done!')
    time.sleep(1)

    p.status('Sixth questions - converting little to big endian and calculate ascii text...')
    time.sleep(1)
    s.recvuntil(b'hex string?')
    string=s.recv().split()
    string=string[0].decode('utf-8')
    string=binascii.unhexlify(string)
    ascii_text=string[::-1]
    s.sendline(ascii_text)
    p.status('Sixth questions - done!')
    time.sleep(1)

    p.status('Getting flag...')
    time.sleep(1)
    s.recvuntil(b'witts: ')
    string=s.recvuntil(b"}").decode('utf-8')
    p.success('Got the flag for you!')
    time.sleep(1)
except:
    print('Could not connect to target... something went wrong. Sorry!')

print("\n\n\t"+string+"\n\n")

