## PredictMe

### Challenge Description

Predict my number!?  
```
nc challs.taparctf.ir 9008
```
Format: `Tapar{flag}`  
Hint: 32Bit Random Number Generator!  

### Writeup
We are given a server address in this challenge (nothing else!). When we connect to this server first of all it print `mersenne number` or something like that! So we looked for a way in order to crack this generator. We found [this](https://github.com/tna0y/Python-random-module-cracker) github link which is a python library to crack this random number generator.  
Install this lib and use it. In order to use this cracker we have to first collect 624 number generated with this method and cracker will guess the next one. So we wrote a script and collected 624 numbers and then we could guess th 625th generated number.  
Here is the script:  
```python
# https://github.com/tna0y/Python-random-module-cracker
# pip2 install randcrack

from pwn import *
import pwn
import random, time
from randcrack import RandCrack

def responseGenerator():
	random.seed(time.time())
	rc = RandCrack()
	for i in numList:
		rc.submit(i)
	return str(rc.predict_randrange(0, 4294967295))

conn = remote('challs.taparctf.ir', '9008')
res = conn.recvuntil("Enter Number: ")
conn.sendline("1")
numList = []

counter = 0
while True:
	print(counter)
	res = conn.recvuntil("Enter Number: ")
	s = res.split(" ")[3]
	# print(int(s))
	numList.append(int(s))
	if(len(numList) == 624):
		print("reach 624!!!!")
		g = responseGenerator()
		print(g)
		conn.sendline(g)
		print(conn.recvline())
		exit()
	# print(numList)
	conn.sendline("1")
	counter = counter + 1
```
After 625 interactions we get the flag:  
```
Tapar{I_v3_f0und_4n_el1te_hack3r}
```  