#!/usr/bin/env python3
from os import urandom
from random import randint
from pwn import xor

new = open("new.png", "wb")
enc10 = open("org_flag.png.enc", "rb").read(10)
kp = open("name.png", "rb").read(10)
fkey = xor(enc10, kp).decode()

print(fkey)
c = 1
k = ""
enc = open("org_flag.png.enc", "rb").read()
for i in fkey:
	res = open("enc" + str(c) + ".png", "wb")
	k = k + i
	key = bytes(k, 'utf-8')
	res.write(xor(enc, key))
	c = c+1

# res: Tapar{TCTF_0x00}