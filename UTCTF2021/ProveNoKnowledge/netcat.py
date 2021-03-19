import socket

h = "crypto.utctf.live"
p = 4354

def inverse(a, b):
    up, vp = a, b
    x, y = 1, 0
    while vp > 0:
        q = up // vp
        t = y
        y = x - y * q
        x = t
        t = vp
        vp = up % vp
        up = t
    while x < 0:
        x = x + b
    return x

def nc(hn, p):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hn, p))
    data = sock.recv(1024)
    res = ""
    data = sock.recv(1024)
    res += data.decode()
    elements = res.split("\n")
    g = int(elements[1].split(" ")[1])
    p = int(elements[2].split(" ")[1])
    y = elements[3].split(" ")[1]
    print("^^^^^^^^^^^^^^^")
    x = ""
    data = sock.recv(1024)
    y += data.decode().split('\n')[0]
    y = int(y)
    #print(y)
    #print(p)
    print('************************')

    r = 0
    c = (g**r) % p
    sock.sendall((str(c)+'\n').encode())
    res = ""
    print(sock.recv(1024))
    sock.sendall((str(r)+'\n').encode())
    print(sock.recv(1024))



    list = ['r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x','r','x']
    print(len(list))


    counter = 1
    while True:
        print("counte --> " + str(counter))
        if list[counter] == 'r':
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
        if list[counter] == 'x':
            # (x + r) mod (p - 1)
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
            pass

        counter = counter + 1
        print("-------------")


nc(h, p)
