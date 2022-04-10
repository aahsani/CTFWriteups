## bank-clients

### Challenge Description  

While in Rome, a few heisters spotted a computer in the dumpster outside of a bank and took it. After brute forcing the computer credentials and getting in with "admin/password", there was a password-protected client database discovered. A Desktop sticky note had the following information: "To fellow bank employee - a way to remember each database PIN is that it is 4-digits ranging between 1000 and 9999". It appears the sticky note was auto-translating from another language as well - let's turn that off. Are you able to assist the heisters from here?  
Hint: After scrolling down, there was additional text on the Desktop sticky note that says "wyptbt lza zlwalt". These bank employees should be removed from the payroll immediately...  

### Writeup
We are given a kdbg file and we should crack the password.  
Use Caesar Cipher to decrypt `wyptbt lza zlwalt`. Result is `Prtmm et septem`. This means `first is seven`. So we guess the password is a number between 7000 and 8000.  
We need to generate passlist containing 7000 to 8000.  
Then we use `keepass2john`:  
```
keepass2john SecretDB.kdbx > Keepasshash.txt
john --wordlist=passList.txt KeepassHash.txt
```
Password is: `7182`  
Now we can open it and see the flag.  
