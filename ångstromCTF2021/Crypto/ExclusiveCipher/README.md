## Exclusive Cipher

### Challenge Description

Clam decided to return to classic cryptography and revisit the XOR cipher! Here's some hex encoded ciphertext:  
```
ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c
```  
The key is 5 bytes long and the flag is somewhere in the message.  

### Writeup

We are given a hex encoded ciphertext.  
```
ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c
```  
We know that the key is 5 bytes long.  
We know the flag format in this challenges is `actf{}`. So we use `actf{` and xor it with each 5 bytes of the input and we store the results in a list to check all resulted keys.  
```python
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
```
Then we used each keys as xor key and finally one of them could give us a meaningful text and flag.  
```
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
```
Here is the flag:  
```
Congratulations on decrypting the message! The flag is actf{who_needs_aes_when_you_have_xor}. Good luck on the other cry
```
