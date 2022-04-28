#!/bin/bash

echo "Getting flag from \"Rules\"-Page..."

flag=$(/usr/bin/curl -s https://ctf.nahamcon.com/rules | grep -oE "flag{[0-9a-zA-Z]*}")

echo "Your flag is: ${flag}"
echo "Saving flag in flag.txt as well...!"

echo ${flag} > flag.txt

echo "Thanks for using me - happy to serve..."
