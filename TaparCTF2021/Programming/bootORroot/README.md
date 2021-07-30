## bootORroot

### Challenge Description

boot and root means something special! can you decipher it?  
Format: `Tapar{flag}`  

### Writeup

We are given a txt file including "root" or "boot" in each line. If you consider root as 1 and boot as 0, you will have 248 bits or we can say 31 bytes. Each byte represents a printable byte. Put these bytes together.  
```python
f = open("bootORroot.txt", "r").read()
s = f.split("\n")[:-1]

byteList = []
for i in range(0, int(len(s)/8)):
	b = ""
	for j in range(0, 8):
		if(s[i*8 + j] == "root"):
			k = "1"
		else:
			k = "0"
		b = b + k
	
	byteList.append(chr(int(b, 2)))
print("".join(byteList))
```  
Here is the flag:
```
Tapar{b00t_2_r00t_1s_f4ntast1c}
```