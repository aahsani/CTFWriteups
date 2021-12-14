## Erased

### Challenge Description

Saw my drive bloated with images and unecessary files, decided to wipe it. Turns out I removed some important files. I went and recovered them but seems like I still can't find the file or should I say the file contents.  
Challenge Files - https://mega.nz/file/MohmjaQI#IQLuCkv49EJuUH9jlBBXgMB8wmKam0Li4uYy8NC60sU  

Wrap with flag format nite{} and replace " - " with " _ "  

### Writeup

we are given a zip file containing several files. We used `file *` in order to see each file's type. One of them is an ASCII text and it is containing comething like morse code!  
```
____. ._ _... __... ._. ..... __...
-
__... ._ ._._ _____ .._ ____. ._ .__
-
____. .....
-
._.. _.. ._
```
When we decode it, we see something meaningless and it is not the flag.   
We reversed the code and it worked! 
```
.____ _. ..._ ...__ ._. ..... ...__
-
...__ _. _._. _____ _.. .____ _. __.
-
.____ .....
-
.._. .._ _.
```  
After decoding we get `1NV3R53-3NC0D1NG-15-FUN`. Here is the flag: `nite{1NV3R53_3NC0D1NG_15_FUN}`  