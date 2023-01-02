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


'''
hashi
1b.8.1.c........09.30.....64aa9.
------------------------------------------
snotg
c.d.1.53..66.4.43bd.......59...8
------------------------------------------
uessy
.d.d.076........eae.3.6.85.a2...
------------------------------------------
'''