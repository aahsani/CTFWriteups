## French
  
### Writeup
Use gdb. Put a break point right after `rc4_crypt` execution.  
```
   0x00000000000016e3 <+180>:	mov    esi,0x17
   0x00000000000016e8 <+185>:	mov    rdi,rax
   0x00000000000016eb <+188>:	call   0x1466 <rc4_crypt>
   0x00000000000016f0 <+193>:	mov    DWORD PTR [rbp-0x7c],0x0
   0x00000000000016f7 <+200>:	jmp    0x171c <main+237>
```   
```
gdb-peda$ b* main+193
```  
Run it and just enter input. You see the flag when interrupted.  
Here is the flag:  
```
cvctf{rC4<->3nC0d3d>-<}
```  