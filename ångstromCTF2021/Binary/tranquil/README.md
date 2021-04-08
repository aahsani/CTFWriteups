## tranquil

### Challenge Description

Finally, inner peace - Master Oogway.  
Connect with nc shell.actf.co 21830, or find it on the shell server at /problems/2021/tranquil.  

Hint: The compiler gives me a warning about gets... I wonder why.  

### Writeup

We are given an executable file with its code. In this code we have a main funcion, a `vuln` function that is called inside `main`. There is also a `win` function that is not used anywhere.  
Indise `vuln` funtion there is a `password` variable which is an array of `char` with 64 elements. A `gets` function gets the input from user. We have to give an input in a way that rewrites return address of `vuln`.  
First we check that when we reach segment fault. When we give 'A'*72 as input to the server we get segment fault. So we have to add `win` address after 72 charachters.  
In order to find `win` address we used `gdb` and `info functions`. Address of `win` is 0x0000000000401196 which is `\x96\x11@\x00` in bytes:  
```python
import pwn
pwn.p32(0x0000000000401196)
```
We add this address after 'A'*72. Then we can get the flag:  
```
python2.7 -c "print 'A'*72 + '\x96\x11@\x00'" | nc shell.actf.co 21830
```
Here is the flag:  
![flag.png](https://github.com/aahsani/CTFWriteups/blob/master/%C3%A5ngstromCTF2021/Binary/tranquil/flag.png)