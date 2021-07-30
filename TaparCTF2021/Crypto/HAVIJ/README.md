## HAVIJ

### Challenge Description

Can You Find The Encryption Key?
Format: Tapar{Encryption-KEY}

### Writeup

We are given a `flag.png.enc` and a python file. This is the python file content: 
```python
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
```  
You see that there is a key with at most 9 charachters and this key is used to be xored with the `flag.png` file. 
We read the 10 first bytes of a valud `.png` file and the first 10 bytes of `flag.png.enc` file. We performed xor on them and got a 10 bytes length key. 

Since we do not know the exact key length, we used 9 different keys and performed xor on `flag.png.len` to see which key gives us a valid picture. And we see that the 9-byte key is the original key.  
![enc9](enc9.png)  
an the flag is:  
```
Tapar{TCTF_0x00}
```  