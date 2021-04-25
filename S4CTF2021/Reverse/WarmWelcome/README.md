## Warm Welcome

### Challenge Description

We have prepared a very warm welcome for you!  

### Writeup

We are given and elf file. Open it with ghidra and find main function. There we see some conditions that if all the conditions are satisfied it means you have the flag.  
```c
sprintf(local_91,"%d",4);
  sprintf(local_93,"%d",0);
  local_8f = 'T';
  local_8e = 0x68;
  local_8d = 0x33;
  local_8c = 0x5f;
  local_8b = 0x46;
  local_8a = 0x31;
  if ((((((((local_88 == 'S') && (local_87 == '4')) && (local_86 == 'C')) &&
         ((local_85 == 'T' && (local_84 == 'F')))) && (local_83 == '{')) &&
       (((local_55 == '}' && (iVar1 = strncmp(acStack118,"We1c0m3_fr0m_S4LAB",0x12), iVar1 == 0)) &&
        ((local_82 == 'A' && (((local_81 == '_' && (local_80 == 'v')) && (local_7b == 0x6d726157))))
        )))) && ((iVar1 = strncmp(acStack93,&local_8f,6), iVar1 == 0 && (local_64 == 0x6a6e655f))))
     && ((local_7f == 0x5f797233 &&
         (((local_77 == local_5e && (local_77 == '_')) &&
          ((local_56 == 'g' &&
           (((local_5f == 'y' && (local_57 == local_91[0])) && (local_60 == local_93[0])))))))))) {
    puts("\rOh Wow you are ready for fun!! :)\n");
    return 0;
  }
```
You can use `pwn.p32` in order to see string representation of the hex numbers. Just put them together in specific order.  
Here is the flag:  
```
S4CTF{A_v3ry_Warm_We1c0m3_fr0m_S4LAB_enj0y_Th3_F14g}
```
