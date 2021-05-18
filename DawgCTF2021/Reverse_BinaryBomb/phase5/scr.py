def func(uParm1):
	if((uParm1 & 1 == 0) or uParm1 == 0 or uParm1 == 1):
		return False
	local_c = 3;
	while (local_c < ((uParm1 + (uParm1 >> 0x1f)) >> 1)):
		if (uParm1 % local_c == 0):
			return False
		local_c = local_c + 2
	return True


resList = []
for i in range(0, 0x1f94):
	if(func(i) == True):
		resList.append(i)

print(resList)

print(len(resList))

# -------------------------------------------
a1 = 2011 # kayla1
a2 = 2017 # harris
a3 = 2027 # ilovemike
a4 = 2029 # valenciaw
