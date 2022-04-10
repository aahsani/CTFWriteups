def onCrystal(data):
	for i in range(0,len(data)):
		data[i] = data[i] ^ 0xFFFFFFFF;
	return data

def onGracious(data):
	for i in range(0,len(data)):
		data[i] = data[i] ^ 0x47; 
	return data

def onCruel(data):
	for i in range(1,len(data)):
		data[i] = data[i] ^ data[i - 1]; 
	return data

blue_data = [-70, 74, -118, -9, 37, 105, 69, -119, 103, -88, 91, 19, -58, -58, -19, -16, 100, 65, 42, 79, 27, -45, -125, -38, 119, 8, -121, -8, 67, 71, -2, 62, -34, 93, 0, -116, 54]
def onPrecious(data):
	for i in range(0,len(data)):
		data[i] = data[i] ^ blue_data[i];
	return data

def onGraceful(data):
	res = []

	for i in range(0,len(data)):
		try:
			res.append(chr(data[i]))
		except Exception as e:
			res.append(chr(data[i] + 4294967296))
	return "".join(res)

# red system
MIN_VALUE = -128
red_data = [104, 65, 111, -41, 119, -19, -59, 19, 118, 102, 92, -35, 70, -92, -49, -33, 61, -74, -17, -90, MIN_VALUE, 31, -86, -94, 67, -55, 16, -67, 91, -113, 63, 41, 81, 49, -75, 103, 79]

crystal = onCrystal(red_data)
gracious = onGracious(crystal)
cruel = onCruel(gracious)
precious = onPrecious(cruel)
flag = onGraceful(precious)
print(flag)

# jctf{b3Tter_th4N_tH3_0r1giN4l_a093c0}