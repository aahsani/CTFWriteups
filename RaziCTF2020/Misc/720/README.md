## 720

### Challenge Description:

These files belong to Lucius. I found them in his flash drive, but I could not open them.  
Can you figure out how to open them? Please avoid opening any unnecessary and dangerous files.  

### Writeup

In this challenge we have a zip file. After extracting this file, we see there is some other files. We use `binwalk` tool for each. Two of them have some other files, but just `printui.dll` has a file named `The Flag You Need.txt`. So extract these files using command below:  
```
binwalk -D=".*" printui.dll
```
There is a `98F4` zip file. Extract it. You have the `The Flag You Need.txt` file.   
Flag:  
```
RaziCTF{5pl17_4nd_j01n}
```
