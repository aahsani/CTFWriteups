## JNI

### Challenge Description

Bypass me!   
Format: `Tapar{flag}`   

### Writeup
We are given an apk file. If you install it, you will see a text box and a submit button. We used `jadx` in order to retrieve its code. There is a `checkFlag` function which gets text box content and checks if it is flag or not. 
We searched for `checkFlag` in whole project and found no definition except bellow which has not function body.  
```java
public native boolean checkFlag(String str);
```
There is a ```native``` keyword before this definition. We searched this keyword and found that Java Native Interface or JNI is a concept in java which allows us to use methods defined in another shared library written in some other languages like C or C++. [This](https://www.baeldung.com/jni) link is useful for JNI concept.  
In order to extract lib files of the apk file, we changed `.apk` to `.zip` and extracted it. In lib directory there is some directories and each of them is for a spesific architecture. Inside these directories there is a lib file named libnative.so.  
We used ghidra to decompile the one in x86_64 directory and saw that there is chechFlag function. 
Finally this is the flag:  
```
Tapar{JNI_IS_NOT_Compl3x}
```