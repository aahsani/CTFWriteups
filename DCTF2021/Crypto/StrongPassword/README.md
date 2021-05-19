## Strong Password

### Challenge Description  
Zip file with a password. I wonder what the password could be?  

### Writeup
I used `JohnTheRipper`. First i installed it using command bellow:  
```
git clone "https://github.com/magnumripper/JohnTheRipper.git" && cd JohnTheRipper/src && ./configure && sudo make -s clean && sudo make -sj4 
```
Then use these commands and it gievs you the password:  
```
john-the-ripper.zip2john strong_password.zip > hash
john-the-ripper hash --wordlist=rockyou.txt
```
The password is `Bo38AkRcE600X8DbK3600`.
Use this password and open the flie. Look for `dctf` string and you got the flag:   
```
dctf{r0cKyoU_f0r_tHe_w1n}
``` 
