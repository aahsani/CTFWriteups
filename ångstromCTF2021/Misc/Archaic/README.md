## Archaic

### Challenge Description

The archaeological team at ångstromCTF has uncovered an archive from over 100 years ago! Can you read the contents?  
Hint: What is a .tar.gz file?  


### Writeup

We are given a `.tar.gz` file. If we extract the content using 7z, we get another `tar` file which has a `flag.txt` file.  
Here is the flag:  
```
actf{thou_hast_uncovered_ye_ol_fleg}
```