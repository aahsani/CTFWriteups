## Pixelify

### Challenge Description

Pixels don't reveal secrets, or do they?
Hint : The original file name is inject.bin


### Writeup

In this challenge, we are given a python file and an image named `inject.png`.  
First we have to reverse the python code in a way we can decode `inject.png` file. We get a file which has not regular headers that we have seen before!  
There is a hint in challeneg description which points to `inject.bin`. If you search for `inject.bin` files, you see there is a tool named `ducktoolkit`. Which can be installed or can be used online using link below:  
```
https://ducktoolkit.com/
```  
I used [online decoder](https://ducktoolkit.com/decode) of this tool and decoded the result file.  
After decoding, you see that flag is decoded content!  
