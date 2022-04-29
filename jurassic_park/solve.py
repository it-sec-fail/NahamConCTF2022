#!/usr/share/env python

import requests

print("Give me the port, I give you the flag!")
port=int(input("> "))
url=f"http://challenge.nahamcon.com:{port}/ingen/flag.txt"

response = requests.get(url)
print(response.text)
