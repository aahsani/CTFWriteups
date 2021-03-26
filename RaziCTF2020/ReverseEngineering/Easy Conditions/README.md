## Easy Conditions

### Challenge Description  
This guy protected his music program with a serial number. Can you crack it?

### Writeup  
In this challenge an exe file is given. First run this esecutable. It wants you to enter a serial number. So look for "Enter Serial Number" string in code.  
In main funtcion there is a string that is compared to input string. If input string is equal to "1337-1337-1337-1337", it will give you the flag.
```
RaziCTF{your_fl4g_is_this_cute_flag}
```
