## Follow the Currents

### Challenge Description

Go with the flow...  

### Writeup

We are given a python file which reads flag from a file and applies `xor` on each byte of flag with a vlue generated by `keystream` function. In this function we have a `key` variable that is 2 bytes long. So we see that we can just use bruteforce of each 2 bytes as key and perform xor on results to get the flag.  
```python
def keystream():
	key = os.urandom(2)
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
		yield key[index]
```  
Finnaly we can see one meaningful text containing flag:  
```
are like 30 minutes left before the ctf starts so i have no idea what to put here other than the flag which is actf{low_entropy_keystream}
```  