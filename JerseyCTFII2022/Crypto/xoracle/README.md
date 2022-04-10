## xoracle

### Challenge Description  

Check out my cool new encryption service! It's very secure!  

Connect to 0.cloud.chals.io on port 19305.  

### Writeup
```python
# when we connect to server, here is the decrypted flag:
# 5e13861609acb742700d4dcedb5f1ffc05793688e5f30d45925d3ee6a081d68f5117505d3a8b
# if we give it as input to encrypt multiple times, we see after 2 time we again see it. 
# So dec(s) = enc(enc(s))

flag = "6a6374667b315f746830553968545f31745f7734355f3533437572655f61303762386130317d"

i = 0
res = []
while(i < 76):
	n = flag[i] + flag[i+1]
	i = i + 2
	m = int(n, 16)
	print(chr(m))
	res.append(chr(m))
print("".join(res))

# flag: jctf{1_th0U9hT_1t_w45_53Cure_a07b8a01}
```