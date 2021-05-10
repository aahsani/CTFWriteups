def func1(input):
  r = input
  if(input <= 'z' and input >= 'a'):
    if (input < 'n'):
      r = chr(ord(input) + 13)
    else :
      r = chr(ord(input) - 13)

  if(input <= 'Z' and input >= 'A'):    
    if (input < 'N'):
      r = chr(ord(input) + 13)
    else :
      r = chr(ord(input) - 13)
  return r

def func2(input):
  r = input
  if(ord(input) <= 126 and ord(input) >= 33):
    if (ord(input) < 80):
      r = chr(ord(input) + 47)
    else :
      r = chr(ord(input) - 47)
  return r

s = '"' + "_9~Jb0!=A`G!06qfc8" + "'" + '_20uf6`2%7'

k = []
for i in s:
  k.append(func1(func2(i)))
print("".join(k))