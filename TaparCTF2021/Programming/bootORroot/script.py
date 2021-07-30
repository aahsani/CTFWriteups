f = open("bootORroot.txt", "r").read()
s = f.split("\n")[:-1]

byteList = []
for i in range(0, int(len(s)/8)):
	b = ""
	for j in range(0, 8):
		if(s[i*8 + j] == "root"):
			k = "1"
		else:
			k = "0"
		b = b + k
	
	byteList.append(chr(int(b, 2)))
print("".join(byteList))