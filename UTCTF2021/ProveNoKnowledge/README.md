## Prove No Knowledge

### Challenge Description
I've been trying to authenticate to this service, but I'm lacking enough information.  
`nc crypto.utctf.live 4354`


### Writeup
We are given a server in this challenge. When you connect to this server, it interacts you with a Zero-knowledge protocol. You can see this protocl steps [here](https://en.wikipedia.org/wiki/Zero-knowledge_proof).  
This protocl is repeated 256 times. In the first round it asks you r, in second round asks you (x+r) mod (p-1), in third round it wants r,...   
We know when we are asked for r and (x+r) mod (p-1), so we can authenticate without knowing x!  
Answering to r:  
```
r = 0
c = (g**r) % p
sock.sendall((str(c)+'\n').encode())
res = ""
data = sock.recv(1024)
print(data)
sock.sendall((str(r)+'\n').encode())
res += data.decode()
if res == 'Authentication failed!\n':
    return
```  
Answering to (x+r) mod (p-1):  
```
r = 0
cc = (g**r * inverse(y,p)) % p
sock.sendall((str(cc)+'\n').encode())
res = ""
data = sock.recv(1024)
print(data)
sock.sendall((str(r)+'\n').encode())
data = sock.recv(1024)
res += data.decode()
print(res)
if res == 'Authentication failed!\n':
    return
```  
You can see whole script in `netcat.py` file.  
The flag:  
