## Labyrevnt

### Challenge Description

You find yourself at a labyrinth. Can you find the way through it?  

settings `Service: nc labyrevnt-01.play.midnightsunctf.se 29285`  

### Writeup

In this challenge you are given a server address and its corresponding elf file. When you decompile it using something like `IDA Pro` you see there is a main function which runs `walk_start()` function. If the result is `0` it prints `You failed!` else it gives you the flag. So we have to check when we can get a non-zero result.  
There is almost 3100 functions in this elf file! We checked some of these functions and saw that they all get a charachter as input and call another function based on what this charachter is. Code bellow is `walk_start()` function:  
```c
undefined8 walk_start(void){
  char cVar1;
  undefined8 uVar2;
  cVar1 = get_input();
  if (cVar1 == 'a') {
    uVar2 = walk_SCoNpoMsAQRnDEnm();
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}
```
Between all those functions, You see there is a `walk_end()` function which returns `1`. So we have to look for a path from `main` to `walk_end`. There is almost 3100 functions here and it is hard finding this path by hand!  
We loaded elf file in `IDA Pro` and found `walk_end()` function. When you rigth-click on it, one of the options is `Proximity Browser`. When you use this view it shows the function with parents that can call it or children that can be called in it.   
We can find the path between two functions that has beed loaded in this `Proximity Browser` in `IDA Pro`. So right click on screen and select `Add node by name` and then add `main`. Then again rigth click on `main` and select `Find path`. A window opens up and you can search for `walk_end` function and find the path between these two. To see the path, again rigth click on screen and select this path to see the details. It will show you list of functions in the path. We copied them and pasted somewhere. It gave us almost 197 functions. We checked from `main` to the end that which charachter is needed in each function to call the next function of the list. So we collected all charachters and put them together (You can see this list in `FunctionsPath.txt` file). If you send these characters in order, you get the flag.  
We used pwntools in order to interact with the server. Here is the code:  
```python
from pwn import *
io = remote('labyrevnt-01.play.midnightsunctf.se',29285)
answer = 'a\nB\nI\nk\ns\nN\nP\nZ\nl\nf\nM\nn\nl\nu\nF\nM\nR\nq\nt\nN\nO\nA\nk\nd\nW\nf\nu\nM\nu\nT\nI\nI\nC\nG\nG\nW\nv\nh\nb\nW\nY\nw\nM\nl\nb\nd\nl\nC\nG\nz\nn\nV\nN\nV\nz\nA\ns\nH\nj\ny\nn\nO\nj\nH\nu\nu\nu\nv\nM\nk\nO\nm\nL\nM\nh\nY\nV\ne\nE\nW\nK\nj\nG\nL\nh\nm\nh\nL\nx\ny\nv\nt\nv\nx\np\nz\nG\nC\nW\nu\ni\nb\nx\nD\nh\nG\nz\nE\nm\nA\nf\nk\ne\np\nZ\nD\nI\nN\nx\nd\nH\nT\nQ\nk\nK\nr\ni\nr\nk\nJ\nN\nn\nm\ny\nV\nR\nw\ne\nE\nj\nB\no\nE\nA\nw\ng\nT\nV\nE\nE\nk\nE\nV\nd\nR\nj\nz\nA\nF\nc\nx\nZ\nr\nd\nS\nY\nb\nP\nQ\ns\nt\nu\nI\nL\ns\nI\nj\nO\nS\nW\ng\nL\nL\nL\nX\nv\nk\nC\nA\nQ\nV\ny\nY\nq\nJ\nx\na'
io.send(answer)
print(io.recvline())
print(io.recvline())
print(io.recvline())
```
And here is the flag:  
```
midnight{y0u_w3r3_l05t_f0r_4_wh1l3_bu7_y0u_f1n411y_g0t_0ut}
```