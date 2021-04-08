ci = 'ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c'
ciphertext = bytes.fromhex(ci)

key = "actf{"
key = bytes(key, 'ascii')

keyList = []
counter = 0
data = ciphertext
while counter < len(ci) - 5:
	res = ""
	try:
		res = res + chr(data[counter] ^ key[0])
		res = res + chr(data[counter+1] ^ key[1])
		res = res + chr(data[counter+2] ^ key[2])
		res = res + chr(data[counter+3] ^ key[3])
		res = res + chr(data[counter+4] ^ key[4])
	except Exception as e:
		break
	keyList.append(res)
	counter = counter + 1


data = ciphertext
for k in keyList:
	#k = bytes(k, 'ascii')
	counter = 0
	res = ''
	while counter < len(data) - 5:
		res = res + chr(data[counter] ^ ord(k[0]))
		res = res + chr(data[counter+1] ^ ord(k[1]))
		res = res + chr(data[counter+2] ^ ord(k[2]))
		res = res + chr(data[counter+3] ^ ord(k[3]))
		res = res + chr(data[counter+4] ^ ord(k[4]))
		counter = counter + 5
	print(res)