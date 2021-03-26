## Corruptbattle

### Challenge Description
Can you find my unique blockchain address inside a corrupted and scrambled program, remember the blockchain address is of 42 chars.  
Flag format: vulncon{flag}  
  
### Writeup

You are given an ELF 64 bit file which is corrupted and you can not run it.  
First use `strings`. You see that this file is packed with UPX.95:  
```
Info: This file is packed with the UPX executable packer http://upx.sf.net
Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved.
```  
So we need to download UPX.95 unpacker and unpack this file. You can find different UPX releases [here](https://github.com/upx/upx/releases).  
After unpacking the executale file, now we can use ghidra and decompile it. In main.one function there is some if-else statements which each of them are using some characters. If we concat the, we get a string having 42 chars. 
```
0xE209470e1289D4CE5F23aa7e486228c46C4D99a4
```  
Flag:
```
vulncon{0xE209470e1289D4CE5F23aa7e486228c46C4D99a4}
```