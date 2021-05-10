from pwn import *

def initList():
    f = open("fibs.txt", "r")
    all = f.read()
    fibList = all.split(",")
    return fibList


def GenResponse(a1, a2, a3):
    if (a1 in fibList):
        return a1
    if (a2 in fibList):
        return a2
    if (a3 in fibList):
        return a3


fibList = initList()

conn = remote('umbccd.io', '6000')
data = conn.recvuntil("]\n").decode("utf-8")
print(data)
index1 = data.find("[")
index2 = data.find("]")
args = data[index1+1:index2].strip().split(",")

print(args)
ans = GenResponse(args[0].strip(),args[1].strip(),args[2].strip())
print("^^^^^^^^^^^^^^^^^^^^^^^^")
print(ans)
conn.sendline(ans)
counter = 0

while True:
	counter = counter + 1
	print("step : ", counter)
	if(counter == 100):
		print(conn.recvall())
	data = conn.recvuntil("]\n").decode("utf-8")
	print(data)
	index1 = data.find("[")
	index2 = data.find("]")
	args = data[index1+1:index2].strip().split(",")

	print(args)
	ans = GenResponse(args[0].strip(),args[1].strip(),args[2].strip())
	print("^^^^^^^^^^^^^^^^^^^^^^^^")
	print(ans)
	conn.sendline(ans)