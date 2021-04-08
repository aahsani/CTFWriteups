import os
import zlib

urandomList = []
for i in range(0,255):
	for j in range(0,255):
		urandomList.append((chr(i)+chr(j)).encode())

def keystream2(key):
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
		yield key[index]

enc = open("encOrg", "rb")
encData = enc.read()
enc.close()

for ke in urandomList:
	k = keystream2(ke)
	res = []
	for b in encData:
		kkk = next(k)
		res.append(b ^ kkk)
	for r in res:
		print(chr(r), end='')
	print()
