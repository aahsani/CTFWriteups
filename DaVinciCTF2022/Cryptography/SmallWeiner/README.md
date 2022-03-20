## Small Weiner  

### Challenge Description

Someone I hate sent me an insulting message using RSA. Can you retrieve his private key?  
```
m = 0x596f7520686176652073756368206120736d616c6c207765696e65722e2049204841544520594f5521212121
N = 0x26553fbb7e4bd5bd48868a25f24d9cc5975aa8597f82110058e687dfa10dd0114c0d2011fa288dbd9d01c0a70dfa8212d5a218d513bdd8ebed9f75bc299e1461be8a23ed8ade96bc449d409fbbf5a328ee2ad3257e6c55a97641258730f74f4d3938f0df794546791ba2b1518b8d855e83f65f885d67aa000a01687ac605404e7bca681e51e6e195f77eb4785fcda0372e3d0fd90240f736243584677f89da4c6ab54d687897d5afb0801cc151c516b072aaa2d9aa8d39d34c230536cba077beaa88ff8e8940a5ba990cafd0b1326f209873a43a785d0c5477241fb6469b8c27c7d54908467a7525de18b2425901c0de3ed63472831c29818ce6efb0354c61f36b2e61146472e99209d198bc885ced0edb66eab62a968c9b98b49b756c689d69820ca1d97e1232c338084097078265ce79b25c1e37bc777247af3fee2ce7a87a697a120c0428327177cf6e934aa2d18e696474227d361a5c36992788c3b1aa8654b88852e897027d58b21576b25a5ffdcb9fbdc5167eb74f1c9082ae79ca0b89
e = 0xfc2e4d12eb69a42c074d9a0ddc6b84294f1e23d6eaa0ba53e9cb60ec0db203d31bdfb90eaca38189890ad26335ad6107cd234a415bfc73fc1bbd6c5d9da65249eebb57d889f91719cfdbd535ab19d2d317ffdf075870a62c6e05aac16c9b122e1c52d7dbeb2fb683514d0f463b58a4217f2e379e5a62be06e764e043a0eac5ac6af56816af926bcc4cd826ee1cfd4157496dc024042676503cec93de45c3c5e4dd9dcf85406a3cf93a9f784b9eef6e320cd9856aefff48df52127b98da8a0d207f588ce1c58e47419554590b1fa7fa3c38034f93a3a5112b6dd5e78c181abc2d972fbcb058575789c68c03f043bd4bf48d94fa7390c77f9fc033f3f01a5162d31056eb42a07397f3485b25396f93558466fc49ef80adea1e9d6c3d9edf529be5faf014669ae5f8e02433a2474d9c92fcc468d81aa0fd641a5647d55153713783a9e5d66fe70c9c2794325b28f20b751fb49359c4a8487bbfa7efc6270b7fa0ffe277276bba14027596d129fcbdef0a82aba24855bfd2155071b52c11da2d943
```  

### Writeup

We are given `m`, `N`, and `e` and we are asked to find the private key.  
If you pay attention to the challenge name, you can find a hint for solving the challenge. IF you just google it, you will find out `Wiener` is a cryptographic attack against RSA. The attack uses the continued fraction method to expose the private key d when d is small. ([more info](https://en.wikipedia.org/wiki/Wiener%27s_attack))  
I checked two useful tools that perform some attacks. [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) tool performs wiener. I used it but it could not find the private key.  
Another tool is [RSHack](https://github.com/zweisamkeit/RSHack). In order to perform a wiener attack, we should pass `N` and `e` as input. It will perform the attack and give us the private key.  
Here is the private key:    
![wiener](wiener.jpg)   
