## Beep38

### Challenge Description

Jack lost a Fortune, Recover his BTC Paper Wallet!  
BTC Wallet: `14fWyKcU5rGT6hFwRdetXuXk83ybr6ocjf`  
Encrypted Private Key: `6PnY51UEH24GQ1WBjNqfqxtVnbRYgH9FfqUhxZyfPYw12T2o6rnPSuwxUg`  
Format: `Tapar{Wallet Password}`  
  
There is a hint: ```rock you! 979k-980k```  
  
### Writeup

We are given a private key and a wallet address of BTC. The challenge asks us to retrive password of this acount. 
There is a hint: ```rock you! 979k-980k```
We searched Bip38 password recovery and found [this](https://github.com/3rdIteration/btcrecover/archive/master.zip) github link which can recover bip38 acount password using just its private key and a password list. We downloaded this repo and used `btcrecover.py` file.  
Base on the hint, we extracted 979000 to 980000 lines of `rockyou.txt` passlist.  
```python
a_file = open("rockyou.txt", 'r', encoding = "ISO-8859-1").read()
print("file read!")
ff = a_file.split("\n")
passList = open("passList.txt", "w")
lines_to_read = range(979000 ,980001)
for i in lines_to_read:
	passList.write(ff[i] + '\n')

```
And we got the password using command bellow:  
```
python3.8 ./btcrecover-master/btcrecover.py --bip38-enc-privkey 6PnY51UEH24GQ1WBjNqfqxtVnbRYgH9FfqUhxZyfPYw12T2o6rnPSuwxUg --passwordlist passList.txt
```

