## Johnny

### Challenge Description

Company asked its employee to use complex password to make them secure from hackers like you. Its a human tendency to use password related to their personal life which include their name, DOB, work, Company etc generally with special characters like '@'. For example- Bob@RSA, Alice42@RSA@Security, Alice@Security@42. However employees never used same word multiple times in password.  
  
### Writeup

We are given two file. One of them is some more explanations of challenge:  
```
Company asked its employee to use complex password to make them secure from hackers like you. Its a human tendency to use password related to their personal life which include their name, DOB, work, Company etc generally with special characters like '@'. For example- Bob@RSA, Alice42@RSA@Security, Alice@Security@42. However employees never used same word multiple times in password. 
Given this info can you crack the password and prove your skills ? (Keep note of Case-Sensitivity)

Name- John
Age- 37
Company- Ripper
Working Role- Cracker
```  
  
Another file is a `kdbx` file that we can just open it using KeePass. But it has a password. So we have to look for password.  
We have a limited space for bruteforce. There is a tool in Kali named `keepass2john`. This tool helps us to find the password of a `kdbx` file.  
In first step we have to create a new `txt` file which somehow is our `kdbx` file. And then use this `txt` for brutforce.  
Using commands below we create the `txt` file:  
```
root@kali:~/Desktop/Johnny# keepass2john Confidential.kdbx > Keepasshash.txt 
root@kali:~/Desktop/Johnny# cat Keepasshash.txt 
Confidential:$keepass$*2*60000*0*03c738a1a46a44e18a0d98699035caa3daa93ac981657b03902eb2740d54ba5a*2ab9d78d05419b5fad8362e2561c205614e50bc1c3c665d81e16c6b2cf737f6b*c3f1cf401fb955d24e3d781e922cd2f6*a14047c21e99e7fa0bbbd697b084d160e23b5fac5f2ce497f5e20399266fcc0e*151526a611c5328143047fe50a2792da4cf40d88c2536dc13f5151776038de00
```  
  
Then we have to generate another `txt` file containing different kind of passwords. In order to do this I used script below to generate every permutation of password. Each time I changed `data` list and generated new passwords and stored them in `passList.txt` and use this `txt` as password list.  
  
```python: 
def permutation(lst): 
    if len(lst) == 0: 
        return [] 

    if len(lst) == 1: 
        return [lst] 

    l = []

    for i in range(len(lst)): 
       m = lst[i]
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  

data = ["John","37","Cracker","Ripper"]
data = ["John37","Cracker","Ripper"]
#data = ["John","37","Cracker"]
#data = ["John","37","Ripper"]
#data = ["John","Cracker","Ripper"]
#data = ["37","Cracker","Ripper"]
#data = ["John","37"]
#data = ["John","Cracker"]
#data = ["John","Ripper"]
#data = ["37","Cracker"]
#data = ["37","Ripper"]
#data = ["Cracker","Ripper"]
#data = ["John"]
#data = ["37"]
#data = ["Cracker"]
#data = ["Ripper"]

f = open("passList.txt", "w")

for p in permutation(data): 
    s = "@".join(p)
    f.write(s+"\n")
    print s

f.close()
```
Each time we used command below to test passwords:  
```
john --wordlist=passList.txt Keepasshash.txt
```
Finaly we got the correct password:  
![result](https://github.com/aahsani/VulnConCTF2020-Writeups/blob/master/Miscellaneous/Johnny/pass.jpg)

Password is:  
```
John37@Cracker@Ripper
```

Now we can open the `kdbx` file. After openning the file, we see the username is `Programming_Is_Necessary_For Cyber_Right?`. We replaced space character with underline and used it as flag:  
```
vulncon{Programming_Is_Necessary_For_Cyber_Right?}
```
