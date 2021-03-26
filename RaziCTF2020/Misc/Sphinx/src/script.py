import sys
import socket
import time
import base64
import hashlib

hostname = "sphinx.razictf.ir"
port = 1379
tripledict = {
'03957033230393e9cf31dde82f24510fcircle':'d',
'03957033230393e9cf31dde82f24510fsquare':'b',
'03957033230393e9cf31dde82f24510fcross':'c',
'03957033230393e9cf31dde82f24510ftriangle':'a',
'13869da00347be4148369ca491aaf410circle':'c',
'13869da00347be4148369ca491aaf410square':'b',
'13869da00347be4148369ca491aaf410cross':'d',
'13869da00347be4148369ca491aaf410triangle':'a',
'1800174024830a8d63dfc05bda922f2ecircle':'d',
'1800174024830a8d63dfc05bda922f2esquare':'c',
'1800174024830a8d63dfc05bda922f2ecross':'a',
'1800174024830a8d63dfc05bda922f2etriangle':'b',
'1e89e436d78591c18c86523ee9d1e386circle':'d',
'1e89e436d78591c18c86523ee9d1e386square':'c',
'1e89e436d78591c18c86523ee9d1e386cross':'b',
'1e89e436d78591c18c86523ee9d1e386triangle':'a',
'27c46ec954b39a17eb645f37056f544dcircle':'d',
'27c46ec954b39a17eb645f37056f544dsquare':'a',
'27c46ec954b39a17eb645f37056f544dcross':'b',
'27c46ec954b39a17eb645f37056f544dtriangle':'c',
'37a27061d5c12b152ec6c8fd8df0312ccircle':'a',
'37a27061d5c12b152ec6c8fd8df0312csquare':'b',
'37a27061d5c12b152ec6c8fd8df0312ccross':'c',
'37a27061d5c12b152ec6c8fd8df0312ctriangle':'d',
'37b13d67143be16881819e2e18ff5809circle':'c',
'37b13d67143be16881819e2e18ff5809square':'b',
'37b13d67143be16881819e2e18ff5809cross':'a',
'37b13d67143be16881819e2e18ff5809triangle':'d',
'38864f22a3f82db183e1c222ef6919aecircle':'a',
'38864f22a3f82db183e1c222ef6919aesquare':'d',
'38864f22a3f82db183e1c222ef6919aecross':'c',
'38864f22a3f82db183e1c222ef6919aetriangle':'b',
'39ec64e351da868b32f7c6e6357c7671circle':'b',
'39ec64e351da868b32f7c6e6357c7671square':'a',
'39ec64e351da868b32f7c6e6357c7671cross':'c',
'39ec64e351da868b32f7c6e6357c7671triangle':'d',
'3ff6df550e34fd4d35fbe5f2cb846e27circle':'c',
'3ff6df550e34fd4d35fbe5f2cb846e27square':'a',
'3ff6df550e34fd4d35fbe5f2cb846e27cross':'d',
'3ff6df550e34fd4d35fbe5f2cb846e27triangle':'b',
'4dec0d35ad2f4413cace303f489f54c8circle':'a',
'4dec0d35ad2f4413cace303f489f54c8square':'c',
'4dec0d35ad2f4413cace303f489f54c8cross':'d',
'4dec0d35ad2f4413cace303f489f54c8triangle':'b',
'4e1647f7155ebd72d729f1c02c7bff98circle':'d',
'4e1647f7155ebd72d729f1c02c7bff98square':'a',
'4e1647f7155ebd72d729f1c02c7bff98cross':'c',
'4e1647f7155ebd72d729f1c02c7bff98triangle':'b',
'4f8cf498fdcf9458cbcad21c649d1feecircle':'a',
'4f8cf498fdcf9458cbcad21c649d1feesquare':'b',
'4f8cf498fdcf9458cbcad21c649d1feecross':'d',
'4f8cf498fdcf9458cbcad21c649d1feetriangle':'c',
'53e766e8aefe0d0a5f823ef3618c8ab4circle':'b',
'53e766e8aefe0d0a5f823ef3618c8ab4square':'a',
'53e766e8aefe0d0a5f823ef3618c8ab4cross':'d',
'53e766e8aefe0d0a5f823ef3618c8ab4triangle':'c',
'69e1371dd44d50614d8b46017d0418bacircle':'b',
'69e1371dd44d50614d8b46017d0418basquare':'d',
'69e1371dd44d50614d8b46017d0418bacross':'c',
'69e1371dd44d50614d8b46017d0418batriangle':'a',
'9a3196111cfd8c1d6a3417161a4c08eccircle':'d',
'9a3196111cfd8c1d6a3417161a4c08ecsquare':'b',
'9a3196111cfd8c1d6a3417161a4c08eccross':'a',
'9a3196111cfd8c1d6a3417161a4c08ectriangle':'c',
'a71d03961aca2445c9592b48a7f6c191circle':'c',
'a71d03961aca2445c9592b48a7f6c191square':'d',
'a71d03961aca2445c9592b48a7f6c191cross':'a',
'a71d03961aca2445c9592b48a7f6c191triangle':'b',
'ae2db12ef5b3b1894cc8e29f3c431952circle':'a',
'ae2db12ef5b3b1894cc8e29f3c431952square':'c',
'ae2db12ef5b3b1894cc8e29f3c431952cross':'b',
'ae2db12ef5b3b1894cc8e29f3c431952triangle':'d',
'dd3fa4637609e866331bbc58e42d1bcdcircle':'b',
'dd3fa4637609e866331bbc58e42d1bcdsquare':'d',
'dd3fa4637609e866331bbc58e42d1bcdcross':'a',
'dd3fa4637609e866331bbc58e42d1bcdtriangle':'c',
'f718c90c57bdd76f5fe8b48e089e05aacircle':'a',
'f718c90c57bdd76f5fe8b48e089e05aasquare':'d',
'f718c90c57bdd76f5fe8b48e089e05aacross':'b',
'f718c90c57bdd76f5fe8b48e089e05aatriangle':'c',
'd4f4621e1da73264f282f7aba93439decircle':'b',
'd4f4621e1da73264f282f7aba93439desquare':'c',
'd4f4621e1da73264f282f7aba93439decross':'d',
'd4f4621e1da73264f282f7aba93439detriangle':'a',
'1b3563757350d1408be64dae69728191circle':'c',
'1b3563757350d1408be64dae69728191square':'a',
'1b3563757350d1408be64dae69728191cross':'b',
'1b3563757350d1408be64dae69728191triangle':'d',
'e8c71d8c57a29fe7eb58ba796dfafc57circle':'b',
'e8c71d8c57a29fe7eb58ba796dfafc57square':'c',
'e8c71d8c57a29fe7eb58ba796dfafc57cross':'a',
'e8c71d8c57a29fe7eb58ba796dfafc57triangle':'d',
'd69fecfb545f508ecb6973deb57b0bd6circle':'c',
'd69fecfb545f508ecb6973deb57b0bd6square':'d',
'd69fecfb545f508ecb6973deb57b0bd6cross':'b',
'd69fecfb545f508ecb6973deb57b0bd6triangle':'a'
}


def GenResponse(PNG_Base64, Question):
    PNG_Decoded = base64.b64decode(PNG_Base64)
    result = hashlib.md5(PNG_Decoded).hexdigest()
    if Question.find("cross") != -1:
        #print(tripledict[result+"cross"])
        return tripledict[result+"cross"]
    elif Question.find("square") != -1:
        #print(tripledict[result+"square"])
        return tripledict[result+"square"]
    elif Question.find("circle") != -1:
        #print(tripledict[result+"circle"])
        return tripledict[result+"circle"]
    elif Question.find("triangle") != -1:
        #print(tripledict[result+"triangle"])
        return tripledict[result+"triangle"]

def netcat(hn, p, content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hn, p))
    res = ""
    data = sock.recv(1024)
    res += data.decode()

    print(res)

    sock.sendall(content.encode())
    while True:
        res = "";
        while True:
            data2 = sock.recv(1024)
            if(data2.decode().find('portrait?') != -1 or data2.decode().find('RaziCTF') != -1):
                res += data2.decode()
                break
            res += data2.decode()
        print(res)

        
        resArr = res.split("\n")
        if(len(resArr) < 2):
            sock.close()
            break
        response = GenResponse(resArr[0], resArr[1])
        sock.sendall(response.encode())
        print(response)
    print(res)

content = "yes"
netcat(hostname, port, content)

