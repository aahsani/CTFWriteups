f = open("fibs.txt", "r")
fibList = f.read().split(",")

print(fibList[0:11])

print("ptr1:")
print(fibList.index(str(0x7b * 55)))

print("ptr2:")
print(fibList.index(str(0x3b18 * 55)))

print("ptr3:")
print(fibList.index(str(0x1c640d * 55)))