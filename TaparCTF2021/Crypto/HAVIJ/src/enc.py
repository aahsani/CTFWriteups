#!/usr/bin/env python3
from os import urandom
from random import randint
from pwn import xor

# Org file content was this part:

input_img = open("flag.png", "rb").read()
outpout_img = open("flag.png.enc", "wb")

key = bytes('FLAG', 'utf-8')
if len(key) < 10:
    outpout_img.write(xor(input_img, key))
else:
    print('Key is too long!')