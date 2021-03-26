## Sphinx

### Challenge Description

I gave the flag to a friend of mine to protect it, she likes riddles and apparently has a bad temper.  
Go say hi: nc sphinx.razictf.ir 1379  

### Writeup

You are given a server address in this challenge. 
```
nc sphinx.razictf.ir 1379
```
When you connect to this server, it gives you some information about a game. It wants you to answer with 'a', 'b', 'c', or 'd' to questions. It is importatnt to answer fast. Content of questions is some data in base64 format. When you copy this content and decode it, you see a PNG file which have four shapes: circle, triangle, square, and cross. Each question wants you to give location of one of these shapes with 'a', 'b', 'c', or 'd' and you have to answer below 1 second.  
In order to do this game, first we ran it multiple times to get different images. We can have 24 different images at all (We have 4 places with 4 objects, so we can have 4! images). We saved those images and made a key-value dictionary in python script, using MD5 hash of images, which can give us location of a specific shape in a specific image.  
We wrote a script and opened a socket in order to connect to the server. We get server data, decode it to `base64` and get a MD5 hash of it. Using our key-value dictionary, we can find the answer and send it to server.  
After 20 question, it will give you the flag:  
``
RaziCTF{c0ngr4tuL4ti0ns_Y0U_d3f34t3d_THE_SPHINX}
``
