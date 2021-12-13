## Hashes Hashes we all fall down

### Challenge Description

Description: We have captured Mr Brute who is a world renowned architect who has built the safest vault in the world which cannot be broken in anyway unless you have the password. He is also one of the biggest bee movie fans ever (His password was probably a word used in the movie). We were able to get the SHA-256 hash of the password from Mr.Brute by using extreme torture methods (Making him watch the bee movie 2398 times). During this torture, he told us that he was told to prepend the password with a salt before hashing it, so he uses 'salt' as a salt cuz salt is salt. He died soon after we released him (Got stung by a bee, obviously). BUT you have the hash. Decrypt the hash so you can break into his vault.  
hash = 12f3b9faec781b0e84184a6fa7c44c81416e5b1855633a2a2730295324724efe  
[Wrap the answer in flag format] Example :- nite{password} NOT nite{salt+password}   

### Writeup

Here is the script:  
```python
import hashlib
script = open('theBeeMovieScript', 'r').read()
l = ['.', '!', '?', '-' , '_', ',', '"']
script = script.translate({ord(x): '' for x in l})

passList2 = script.split()
orgHash = '12f3b9faec781b0e84184a6fa7c44c81416e5b1855633a2a2730295324724efe'

s = set(passList2)
passList1 = list(s)
print(len(passList1))

for pl in passList1:
  salt = 'salt'
  res = hashlib.sha256(salt.encode() + pl.encode()).hexdigest()
  if (res == orgHash):
    print(res)
    print(orgHash)
    print("---------------------------------------")
    print(pl)
```  
flag: `nite{Oinnabon}`  