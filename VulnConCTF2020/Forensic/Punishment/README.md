## Punishment

### Challenge Description

Mr.BEAN was working on his school assignment, But unfortunately, his Lil Sister deleted that assignment file. As Mr.BEAN failed to submit the assignment on time, He will be punished heavily. Anyway, He has an exclusive excuse, but he needs to prove his innocence anyhow! Can you extract the date/time his assignment was deleted?  
  
Flag Format: vulncon{yyyy/mm/dd_hh:mm:ss_UTC}  
  
### Writeup

In this challenge we are given a `chall.txt` file which contains some hex values seperated whit `,`. We used script below and concatenated them. 
```python:
f = open("chall.txt", "r")
fc = f.read()
fc = fc.replace(' ', '')
res = ""
for i in fc.split("\n"):
    for j in i.split(","):
        res = res + j[2:4]
print(res)
```
We converted result to ASCII and saw that the first part of the file is `PK` which means we have a zip file. So we saved it as a zip file.  
We extracted this zip file and got a file named `$I4A67FE.docx`. Files having `$` as their first character of name, are files related to Recycle Bin.  
We can recover these kind of files using [$I Parse](https://df-stream.com/recycle-bin-i-parser/). After recovery we got these data:  
![recovered data](https://github.com/aahsani/VulnConCTF2020-Writeups/blob/master/Forensic/Punishment/res.jpg)  
  
  
Flag:
```
vulncon{2020/11/04_21:01:14_UTC}
```
