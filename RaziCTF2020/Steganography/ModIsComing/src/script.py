import random
from numpy import *
from PIL import Image
from functools import reduce

charset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_','{','}']



def f1(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * f3(p, n_i) * p
    return sum % prod


def f2(a, b): 
    if b == 0: 
        return a 
    else: 
        return f2(b, a%b) 


def f3(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def encrypt(s):
    c_p = []
    for i in range(10,21):
        for j in range(i+1,21):
            if f2(i,j) == 1:
                c_p.append([i,j])
    rand = random.randint(0,36)
    print([len(s), len(s)*3])
    k = f1(c_p[rand], [len(s), len(s)*3])
    
    while k == 0:
        rand = random.randint(0,len(c_p))
        k = f1(c_p[rand], [len(s), len(s)*3])
    
    img = Image.new('RGB', (len(s)*3, len(s)), color = 'white')
    img.show()
    
    image = array(img)
    
    x, y, z = image.shape
    
    print(x)
    print(y)
    print(z)
    
    for a in range (0, x):
        for b in range (0, y):
            p = image[a, b]          
            p[0] = ((k-10) * ord(s[a])) % 251
            p[1] = (k * ord(s[a])) % 251
            p[2] = ((k+10) * ord(s[a])) % 251
            
            
            image[a][b] = p
    enc = Image.fromarray(image)
    enc.save('enc.png')

def findChar(p0,p1,p2,n):

    for ch in charset:
        pp1 = (10 * ord(ch) + p0) % n
        pp2 = (10 * ord(ch) + p1) % n
        if ((pp1 == p1 or (pp1 + n) == p1) and (pp2 == p2 or (pp2 + n == p2))):
            return ch
    return "#"
    

def decrypt(s):
    im = Image.open(s)
    #print(array(im))
    imarr = array(im)
    x, y, z = imarr.shape
    res = ""
    for i in range(0, x):
        ch = findChar(imarr[i][0][0], imarr[i][0][1], imarr[i][0][2], 251)
        res += ch
            
    print (res)
    

#f = open("secretmsg.txt", "r")
#encrypt("abcd")
decrypt("enc.png")
