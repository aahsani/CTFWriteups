initLiat = []
for i in range(ord("!"), ord("~")):
	initLiat.append((((i >> 4) | (i << 4))^100) % 256)

print(len(initLiat))
print(initLiat)

res = []
local_38 = [ord('@'), 0x77,0x23,0x91,0xb0,0x72,0x82,0x77,99,0x31,0xa2,0x72,0x21,0xf2,0x67,0x82,0x91,0x77,0x26,0x91,0,0x33,0x82,0xc4]
for i in local_38:
	try:
		res.append(chr(initLiat.index(i) + 33))
	except Exception as e:
		res.append('~')
	
print("".join(res))