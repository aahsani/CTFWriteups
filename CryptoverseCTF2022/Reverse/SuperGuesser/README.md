## Super Guesser
  
### Writeup
Use `uncompyle6` and get the code.  
```python
# uncompyle6 version 3.5.0
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: /home/guesser.py
# Size of source mod 2**32: 682 bytes
import hashlib, re
hashes = [
 'd.0.....f5...5.6.7.1.30.6c.d9..0',
 '1b.8.1.c........09.30.....64aa9.',
 'c.d.1.53..66.4.43bd.......59...8',
 '.d.d.076........eae.3.6.85.a2...']

def main():
    guesses = []
    for i in range(len(hashes)):
        guess = input('Guess: ')
        if not (len(guess) <= 4 or len(guess) >= 6 or re.match('^[a-z]+$', guess)):
            exit('Invalid')
        if not re.match('^' + hashes[i].replace('.', '[0-9a-f]') + '$', hashlib.md5(guess.encode()).hexdigest()):
            exit('Invalid')
        guesses.append(guess)

    print(f"Flag: {guesses[0]}" + '{' + ''.join(guesses[1:]) + '}')


if _name_ == '_main_':
    main()
```   
You just need to bruteforce.  
Here is the script:  
```
import string
import re, hashlib

alphabet = string.printable
# 'd.0.....f5...5.6.7.1.30.6c.d9..0'
hashes = [
 '1b.8.1.c........09.30.....64aa9.',
 'c.d.1.53..66.4.43bd.......59...8',
 '.d.d.076........eae.3.6.85.a2...']

def isequal(inp):
    for i in range(len(hashes)):
        res = re.match('^' + hashes[i].replace('.', '[0-9a-f]') + '$', hashlib.md5(inp.encode()).hexdigest())
        if(res):
            print(inp)
            print(hashes[i])
            print("------------------------------------------")


word_list = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
st = ""
for i1 in alphabet:
    for i2 in alphabet:
        for i3 in alphabet:
            for i4 in alphabet:
                for i5 in alphabet:
                    st = i1 + i2 + i3 + i4 + i5
                    isequal(st)
```  
Here is the result:  
```
hashi
1b.8.1.c........09.30.....64aa9.

snotg
c.d.1.53..66.4.43bd.......59...8

uessy
.d.d.076........eae.3.6.85.a2...
```
Flag:  
```
cvctf{hashisnotguessy}
```
