a = "Dk52m6WZw@s6w0dIZh@2m5a"
res = []
for i in a:
	res.append(chr(ord(i) ^ 5))
print("".join(res))