# Binary Bomb  
Welcome to the CyberDawgs Binary Bomb challenge series! The "bbomb" binary contains a series of mini reversing challenges broken into 9 phases. Each phase becomes incresingly more difficult, but it is not required to solve a phase to move onto the next. Simply press enter for a phase's input to skip it. Additionally, known phase solutions can be stored in a file named "flags.txt". See the binary's welcome message for the format and requirements. When submitting to this scoreboard, wrap the phase's solution in DawgCTF{}. Happy reversing!  

## BBomb - Phase 1  
### Challenge Description   
Starting off easy... reversing (things) is fun!  

### Writeup  
Just reverse it, flag is in `phase1` function.  
```
DawgCTF{Gn1r7s_3h7_Gn15Rev3R}
```   
  
## BBomb - Phase 2  
### Challenge Description   
Can you help me find my lost key so I can read my string?  

### Writeup  
Just `xor` each byte with 5.  
```python
a = "Dk52m6WZw@s6w0dIZh@2m5a"
res = []
for i in a:
	res.append(chr(ord(i) ^ 5))
print("".join(res))
```
Flag:  
```
DawgCTF{An07h3R_rEv3r5aL_mE7h0d}
```   
  
## BBomb - Phase 3  
### Challenge Description   
Reflections? Rotations? Translations? This is starting to sound like geometry...  

### Writeup  
Read the code and rewrite `func3_1` and `func3_2` functions.  
[scr.py](phase3/scr.py)
Flag:  
```
DawgCTF{D0uBl3_Cyc1iC_rO74tI0n_S7r1nGs}
```
  
## BBomb - Phase 4  
### Challenge Description   
This is the phase you have been waiting for... one may say it's the golden stage!  
Let's switch things up! Numerical inputs map to line numbers in rockyou.txt, and each word is separated by a `_` (if the phase's solution is 4 5, the flag would be DawgCTF{password_iloveyou})  

### Writeup  
Read the code.   
[scr.py](phase4/scr.py)
Flag:  
```
DawgCTF{abc123_qwerty_anthony_123123}
```
  
## BBomb - Phase 5  
### Challenge Description   
Are you really, really ready and excited for this stage?  
(Flag uses the same rockyou.txt format as BBomb Phase 4)  
Update: No input numberis below 2010 and each number increasingly larger than the previous  

### Writeup  
Read the code. You see a `func5` that check if a number satisfies some cases. So we listed all numbers satisfying `func5` and looked for 4 number greater than 2011 that sum of them is equal to 8084.  
```python
a1 = 2011 # kayla1
a2 = 2017 # harris
a3 = 2027 # ilovemike
a4 = 2029 # valencia
```   
Flag:  
```
DawgCTF{kayla1_harris_ilovemike_valencia}
```
  
## BBomb - Phase 6  
### Challenge Description   
Oh no... I lost the key to my string again :(  

### Writeup  
Read the code and rewrite it :)  
Flag:  
```
DawgCTF{B1t_Man1pUlaTi0n_1$_Fun}
```
  
## BBomb - Phase 7  
### Challenge Description   
At least we can say our code is reusable.  
(Flag uses the same rockyou.txt format as BBomb Phase 4)  

### Writeup  
Read the code and rewrite it :) I just rewrote the code in python and checked all 3 numbers satisfying cases.    
Flag:  
```
DawgCTF{iloveme_123abc_batman}
```