a_file = open("rockyou.txt", 'r', encoding = "ISO-8859-1").read()
print("file read!")
ff = a_file.split("\n")
passList = open("passList.txt", "w")
lines_to_read = range(979000 ,980001)
for i in lines_to_read:
	passList.write(ff[i] + '\n')

'''
sudo pip3 install ecdsa

python3.8 ./btcrecover-master/btcrecover.py --bip38-enc-privkey 6PnY51UEH24GQ1WBjNqfqxtVnbRYgH9FfqUhxZyfPYw12T2o6rnPSuwxUg --passwordlist passList.txt

'''