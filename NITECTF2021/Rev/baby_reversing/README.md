## baby reversing

### Challenge Description

Can you get this program to give up it's password ?  

### Writeup

We arer given an elf file. When we run it, it prints "enter the password to get the flag".  
Let's open it in ghidra. We see there are a lot of variables with some hex values. We can see a leet string `b@by_R3v`. If we enter this string as an input, it prints us `hahaha this password is only HALF right, have fun finding the other half!`.   
Now let's go back to the code. In the code bellow, after the `b@by_R3v` string, you see some hex values. They are the ascii code of the string mentioned before. (`hahaha ...`).  
```c
basic_string((char *)local_d8,(allocator *)"b@by_R3v");
~allocator(&local_a9);
basic_string();
local_a8 = (allocator)0x68; // h
local_a7 = 0x61; // a
local_a6 = 0x68; // h
local_a5 = 0x61; // a 
local_a4 = 0x68; // h
local_a3 = 0x61; // a
```  
I just tried to convert these values to charachter and found two flag like strings. The code bellow is one of them and this one is not the flag.    
```c
  basic_string(iVar1 - 0x118,&local_a8);
  ~allocator(&local_57);
  local_56 = (allocator)0x72; // r
  local_55 = 0x33; // 3
  local_54 = 0x40; // @
  local_53 = 0x6c; // l
  local_52 = 0x5f; // _
  local_51 = 0x62; // b
  local_50 = 0x40; // @
  local_4f = 0x62; // b
  local_4e = 0x79; // y
  local_4d = 0x5f; // _
  local_4c = 0x52; // R
  local_4b = 0x33; // 3
  local_4a = 0x76; // v
```   
The code bellow is the flag:  
```c
  basic_string(iVar1 - 0x138,&local_56);
  ~allocator(&local_49);
  local_48 = (allocator)0x62; //b
  local_47 = 0x61; // a
  local_46 = 0x62; // b
  local_45 = 0x79; // y
  local_44 = 0x5f; // _
  local_43 = 0x72; // r
  local_42 = 0x33; // 3
  local_41 = 0x76; // v
  local_40 = 0x5f; // _
  local_3f = 99;   // c
  local_3e = 0x68; // h
  local_3d = 0x61; // a
  local_3c = 0x6d; // m
  local_3b = 0x70; // p
```
the flag is: `nite{baby_r3v_champ}`