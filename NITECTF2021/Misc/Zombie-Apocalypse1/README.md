## Zombie-Apocalypse 1

### Challenge Description

zombies are coming, seek shelter quickly.  

### Writeup

We are given an image `zombies.jpg`. We tested different stego tools and we could get a file `flag.txt` from this image.  
`steghide extract -sf zombies.jpg`   
Here is the content of the file:  
```
oops, i lied! there's no flag here. however, your effort shall not go to waste:

we're ALWAYS attacked by aliens, and now zombies too?!
good thing there's an official contingency plan in place, but what is it? i hope it isn't a joke though

flag format: all lowercase, no spaces
```  
So this file does not contain the flag. But it is telling us something about `contingency plan`. I googled `zombie contingency plan in place nitectf` and found a pdf file named `
CONPLAN_8888-11.pdf`. This was the flag: `nite{CONPLAN8888}`  