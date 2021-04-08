import socket

h = "shell.actf.co"
p = 21700


resultList = []

def bar(a1, a2, a3, a4):
    # a4 = a1 + a2 * (a3 + 1)
    # a1 = a4 - a2 * (a3 + 1)
    # a2 = (a4 - a1)/(a3 + 1)
    # a3 = (a4 - a1)/ a2 - 1

    if(a4 == None):
        return a1 + a2 * (a3 + 1)
    if(a1 == None):
        return a4 - a2 * (a3 + 1)
    if(a2 == None):
        return int((a4 - a1)/(a3 + 1))
    if(a3 == None):
        return int((a4 - a1)/ a2 - 1)

def foo(a1, a2, a3):
    # a3 = a1 ^ (a2 + 1) ^ 0x539u
    # a1 = a3 ^ (a2 + 1) ^ 0x539u
    # a2 = (a1 ^ a3 ^ 0x539u) - 1
    if(a3 == None):
        return a1 ^ (a2 + 1) ^ 0x539
    if(a1 == None):
        return a3 ^ (a2 + 1) ^ 0x539
    if(a2 == None):
        return (a1 ^ a3 ^ 0x539) - 1


def nc(hn, p):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hn, p))
    data = sock.recv(1024)
    counter = 0

    while True:
        counter = counter + 1
        res = ""
        data = sock.recv(1024)
        res = data.decode().strip()
        print(res)

        if("bar" in res):
            args = res[res.find("bar")+4:]
            args1 = args.split(",")
            try:
                a1 = int(args1[0].strip())
            except Exception as e:
                a1 = None
            try:
                a2 = int(args1[1].strip())
            except Exception as e:
                a2 = None
            try:
                a3 = int(args1[2].split(")")[0].strip())
            except Exception as e:
                a3 = None
            try:
                a4 = int(args1[2].split("=")[1].strip())
            except Exception as e:
                a4 = None

            res = bar(a1, a2, a3, a4)

        elif ("foo" in res):
            args = res[res.find("foo")+4:]
            args1 = args.split(",")
            try:
                a1 = int(args1[0].strip())
            except Exception as e:
                a1 = None
            try:
                a2 = int(args1[1].split(")")[0].strip())
            except Exception as e:
                a2 = None
            try:
                a3 = int(args1[1].split("=")[1].strip())
            except Exception as e:
                a3 = None
            
            res = foo(a1, a2, a3)
        print("---------------")
        print(res)
        sock.sendall((str(res)+'\n').encode())
        if counter > 50:
            resultList.append(res)
        
        data = sock.recv(1024)
        res = data.decode().strip()
        print(res)

        if counter > 200:
            return

nc(h, p)
print(resultList)