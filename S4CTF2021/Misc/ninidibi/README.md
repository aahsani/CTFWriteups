## ninidibi

### Challenge Description

let's shuffle it!  

### Writeup
When you open this file with 010Editor you see that the header of file is `format 3`. This is a part of `sqlite` file format. The whole format is `Sqlite format 3`. So we completed the header and opened the file with sqlite browser. We see two tables. `flag` and `order`. All ascii numbers of flag is stored in `flag` table. And their order is stored in `order` table. We just put them together and we could get the flag.  
```python
flag = [115, 33, 84, 98, 65, 95, 123, 108, 95, 80, 95, 95, 95, 95, 95, 102, 104, 98, 70, 33, 104, 87, 51, 82, 108, 52, 95, 98, 102, 75, 89, 66, 67, 53, 67, 82, 97, 105, 83, 97, 125, 114, 110, 48, 83, 77, 33, 97, 48, 55, 85, 95, 95, 52]
index = [27, 52, 3, 41, 26, 24, 5, 47, 33, 39, 45, 29, 40, 22, 10, 13, 49, 46, 4, 50, 44, 34, 16, 36, 42, 1, 23, 8, 30, 28, 9, 6, 20, 18, 2, 32, 43, 19, 0, 35, 53, 15, 17, 14, 21, 37, 51, 48, 31, 25, 38, 11, 12, 7]
realflag = [str(chr(0))] * len(flag)
for i in range(0,len(flag)):
	realflag[index[i]] = str(chr(flag[i]))
print("".join(realflag))
```
Here is the flag:  
```
S4CTF{B4bY___f0r3n5iCS___7AsK_f0R_WaRMUP_blah_blah!!!}
```
