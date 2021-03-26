## can_you_c_the_password?

### Challenge Description
Decrypt the password and submit it as the flag!  
  
### Writeup

In this challenge we are given a directory. It wants us to decrypt a password. We first search for `password`:  
```
grep -R -i password Challenge_files
```
In result we see a `cpassword` in `Groups.xml` file. 
  
![cpassword](https://github.com/aahsani/VulnConCTF2020-Writeups/blob/master/Cryptography/can_you_c_the_password%3F/cpassword.png)  

We searched for `cpassword` in `Groups.xml` and find that there is some tool which are able to decrypt `cpassword`.  
One of this tools is [gp3finder](https://bitbucket.org/grimhacker/gpppfinder/downloads/). So we downloaded `gp3finder` and ran it on `cpassword` value.  
  
Here is the flag:  
![flag](https://github.com/aahsani/VulnConCTF2020-Writeups/blob/master/Cryptography/can_you_c_the_password%3F/gp3finder.jpg)  

Flag:  
```
vulncon{s3cur1ty_h4s_3volv3d_s0__much}
```
