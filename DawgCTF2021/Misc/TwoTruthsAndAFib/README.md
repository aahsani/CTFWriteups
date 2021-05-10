## TwoTruthsAndAFib

### Challenge Description  
Can you catch the fibber? `nc umbccd.io 6000`  

### Writeup
We are given a server address. When you connect to this server, it gives you 3 numbers. One of them will be a fibonacci number and two of them will not. You have to check which one is a fib number and send it as the answer. After passing 100 steps it will give you the flag. 
First we generated fib numbers and stored them in a file. Then we interacted with the server and after 100 steps we reached the flag.  
```
DawgCTF{jU$T_l1k3_w3lc0me_w33k}
```