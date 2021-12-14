## Variablezzz

### Challenge Description

Too many variables. Idk what to do. Can you help?  

### Writeup

We are given a python file. It generates 4 random numbers and uses them to encode the flag. Since we know the 4 first of the flag (`nite`) we can solve equation bellow and get the random numbers:  
```python
8194393930139798 = a * 1331000 + b * 12100 + c * 110 + d
7130326565974613 = a * 1157625 + b * 11025 + c * 105 + d
9604891888210928 = a * 1560896 + b * 13456 + c * 116 + d
6348662706560873 = a * 1030301 + b * 10201 + c * 101 + d
```
I used online tools and solved it. Now we have the four random numbers and we just need to perform a bruteforce in order to find the flag:  
```python
import string
charlist = string.printable
a = 6096359484
b = 6606845234
c = 1736000027
d = 5669601428
res = ['n','i','t','e'] 
Ciphertext = [11444688343062563, 7335285885849258, 3791814454530873, 926264016764633, 9604891888210928, 5286663580435343, 5801472714696338, 875157765441840, 926264016764633, 2406927753242613, 5980222734708251, 5286663580435343, 2822500611304865, 5626320567751485, 3660106045179536, 2309834531980460, 12010406743573553]

for element in Ciphertext:
    for x in charlist:
        if( (a*pow(ord(x),3)+b*pow(ord(x),2)+c*ord(x)+d) == element):
            res.append(x)
            break

print(''.join(res))
```  
Here is the flag:  
```
nite{jU5t_b45Ic_MaTH}
```
