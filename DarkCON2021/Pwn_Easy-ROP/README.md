## EasyROP

### Challenge Description

Welcome to the world of pwn!!! This should be a good entry level warmup challenge !! Enjoy getting the shell  

connection : nc 65.1.92.179 49153  


### Writeup

In this challenge, we are given an elf file and e server address.  
If you reverse the code, you see this program wants 64 byte input from user. When you pass inputs with different number of charachters, you see it faces segment falut in 72 charachters and more. So we need just generate a shellcode and attach it to this 72 charachers and send it to executable.  
I used ropgadget in order to generate shellcode of getting bash from this executable.You can use command below to get the python code of shellcode generation.   
```
ROPgadget --ropchain --binary easy-rop
```  
This gives you python code in stdout. Store it in a `.py` file. Then generate you pwntools script in order to interact with given executable. In this script first we run that `.py` from ropgadget, and attach the result to `'a'*72`. Then we send this payload as input to our executable. We see it gives use the shell. 
Result of runnig the code on server:  
![flag](https://github.com/aahsani/CTFWriteups/blob/master/DarkCON2021/Pwn_Easy-ROP/src/result.png)


