
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
for i in range(0, 0x1fd):
	if(func(i) == True):
		resList.append(i)

print(resList)
print(len(resList))


all509sum = []
for i in resList:
	for j in resList: 
		if( i != j):
			k = 509 - (i + j)
			try:
				if(resList.index(k) >= 0 and i > 100 and j > 100 and k > 100):
					p = []
					p.append(i);p.append(j);p.append(k)
					c = 0
					for m in all509sum:
						if (m[0] == i and m[1] == j and m[2] == k) or (m[0] == i and m[1] == k and m[2] == j) or (m[0] == j and m[1] == j and m[2] == k) or (m[0] == j and m[1] == k and m[2] == j) or (m[0] == k and m[1] == i and m[2] == j) or (m[0] == k and m[1] == j and m[2] == i):
							c = c + 1
					if( c == 0 ):
						all509sum.append(p)
			except Exception as e:
				pass

print(len(all509sum))

f = open("rock_550.txt", "r")
l = f.read().split("\n")
f.close()

for i in all509sum:
	print("DawgCTF{" + str(l[i[0]-1]) + "_" + str(l[i[1]-1]) + "_" + str(l[i[2]-1]) + "}")
	print("----------------------------------")

# i just tested all 125 and reached at bellow:
# final result: "DawgCTF{iloveme_123abc_batman}"