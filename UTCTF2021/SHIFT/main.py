import random
from numpy import *
from PIL import Image




s = 'SHIFT.png'
im = Image.open(s)
imarr = array(im)
x, y, z = imarr.shape

img = Image.new('RGB', (y, x), color = 'white')

resImg = array(img)

'''
print(imarr[0])
print("-----------------")
print(imarr[1])
'''
for i in range(0, x):
	s = (x - i)*5
	for ii in range(0,y):
		j = ii + s
		if j < 0:
			j = j + y
		if j >= y:
			j = j % y
		'''
		print("("+str(i)+","+str(ii)+")")
		print("("+str(i)+","+str(j)+")")
		print("-----------------------")
		'''
		resImg[i][ii][0] = imarr[i][j][0]
		resImg[i][ii][1] = imarr[i][j][1]
		resImg[i][ii][2] = imarr[i][j][2]

rress = Image.fromarray(resImg)
rress.show()
print(array(rress).shape)
rress.save('res.png')

# utflag{not_when_i_shift_into_maximum_overdrive}