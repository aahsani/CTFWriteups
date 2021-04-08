## FREE FLAGS!!1!!

### Challenge Description

Clam was browsing armstrongctf.com when suddenly a popup appeared saying "GET YOUR FREE FLAGS HERE!!!" along with a download. Can you fill out the survey for free flags?   
Hint: Check out decompilers like GHIDRA.  

### Writeup
In this challenge we are given and elf file. We dicompiled it using ghidra. There is 3 conditions and 3 `scanf` functions. 
First condition compares user's input with number 31337.  
```c
local_11c == 0x7a69
```
Second condition wants you to give 2 numbers with condition bellow. We calculated equations and find out those numbers are 419 and 723.  
```c
(local_120 + local_124 == 0x476) && (local_120 * local_124 == 0x49f59)
```
Third condition compares user's input with "banana" string.  
So if we put these inputs we get the flag.  
```
actf{what_do_you_mean_bananas_arent_animals}
```