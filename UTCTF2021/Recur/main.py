list = []

def listInitial():
  list.append(3)
  list.append(5)
  counter = 2
  for counter in range(2, 28*28):
    list.append(list[counter-1]*2 + list[counter-2]*3)

def recurrence(iParm1):
  if(iParm1 == 0):
    uVar3 = 3
  else:
    if(iParm1 == 1):
      uVar3 = 5
    else:
      iVar1 = recurrence((iParm1 - 1));
      iVar2 = recurrence((iParm1 - 2));
      uVar3 = iVar2 * 3 + iVar1 * 2;
  return uVar3

def recurrence2(iParm1):
  return list[iParm1]



listInitial()
flag = [0x76, 0x71, 0xc5, 0xa9, 0xe2,0x22, 0xd8,0xb5, 0x73, 0xf1, 0x92, 0x28, 0xb2,0xbf,0x90,0x5a,0x76,0x77,0xfc,0xa6,0xb3,0x21,0x90,0xda,0x6f,0xb5,0xcf,0x38]


local_1c = 0
ok = 2
while local_1c < 28:
  bVar1 = flag[local_1c]
  bVar2 = recurrence2(local_1c*local_1c) % 256;
  #print(bVar1^bVar2)
  #print(bVar1)
  #print(bVar2)
  #print("--------------")
  print((chr(int(bVar1^bVar2))), end='')
  local_1c = local_1c + 1
  pass