import pwn
from pwn import *
import requests
import reverse_geocode
import geocoder

def coordinate_city(co):
	coordinates = co,
	return reverse_geocode.search(coordinates)[0]["city"].lower()

def ip_city(ip):
	print("***")
	print(ip)
	ip = ip.decode()
	return geocoder.ip(ip).city.lower()


target = remote("137.184.215.151", 22606)
target.recvuntil("Question")
target.recvline()
resp = target.recvline()

while True:
	print(resp)
	if(resp.find(b"Coordinate") > -1):
		second = float(resp.split()[-1])
		first = float(resp.split()[-2][:-1])
		res = coordinate_city((first, second))
		payload = res
	if(resp.find(b"IP") > -1):
		addr = resp.split()[-1]
		payload = ip_city(addr)
	print(payload)
	target.sendline(payload.encode())
	print("-----------------------------")
	print(target.recvline())
	print(target.recvline())
	resp = target.recvline()
	payload = ""
	addr = ""
	
# cvctf{4r3_y0u_4_R34L_Ge@r41nB0L7?}