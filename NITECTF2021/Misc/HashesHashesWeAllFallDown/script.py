import hashlib

script = open('theBeeMovieScript', 'r').read()

l = ['.', '!', '?', '-' , '_', ',', '"']
script = script.translate({ord(x): '' for x in l})

passList2 = script.split()
orgHash = '12f3b9faec781b0e84184a6fa7c44c81416e5b1855633a2a2730295324724efe'

s = set(passList2)
passList1 = list(s)
print(len(passList1))

for pl in passList1:
	salt = 'salt'
	res = hashlib.sha256(salt.encode() + pl.encode()).hexdigest()
	if (res == orgHash):
		print(res)
		print(orgHash)
		print("---------------------------------------")
		print(pl)


# nite{Oinnabon}