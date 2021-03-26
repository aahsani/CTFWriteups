## Recurzip

### Challenge Description

You download the file, you stay in this challenge, and I show you how deep the file goes. Remember: all I'm offering is the flag. Nothing more.  

### Writeup

In this challenge you are given a zip file. It is extracted without any password. Inside this zip file, there is another zip file which needs a password to be extracted. If you notice to name of the file, you see it is a `base64` string. Decode this string and use it as password. You will see it is correct password.  
Inside this zip file, there is another zip file again with `base64` decoded string. Use it as password, it works.  
We wrote a python script in order to unzip the file recursively.  
Finaly `flag.txt` file will be extracted and here is the flag:  
```
RaziCTF{wh3lp_th4t_w4s_e4sy_en0ugh}
```
