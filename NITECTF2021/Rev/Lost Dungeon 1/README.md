## Lost Dungeon 1

### Challenge Description

Welcome Adventurer! Legend has it that there lies a dungeon filled with powerful beasts which can be tamed to reveal a secret message. The path to the dungeon is long and arduous. No one who has found the dungeon has returned back as once the beasts get to you they never leave. Can you reach the dungeon and tame the beasts?  

### Writeup

We are given a zip file containing files related to a game. When you run the `Game.exe` file, a simple game will show up and you can see that it is created with unity!  
There is a player and you can see that the path to `dungeon` is in up rigth of the map and it is very long!  
Let's try to reverse it's code. In order to reverse a unity game, we can use `dnSpy`. The original code of a unity game is a `dll` file named `Assembly-CSharp.dll`. We can find this file in `Lost Dungeon\Game_Data\Managed`.  
So open this dll with dnSpy. You can see different classes. One of them is `Player` class. There is something about `axis` and we guess maybe it is related to velocity or position! I just multiplied the value of `axisRaw` and `axisRaw2` with 50 and restarted the game!  
You can see the edited function here:   
```c#
private void FixedUpdate()
{
  float axisRaw = Input.GetAxisRaw("Horizontal");
  float axisRaw2 = Input.GetAxisRaw("Vertical");
  this.o(new Vector3(axisRaw * 50f, axisRaw2 *50f, 0f));
}
```  
**How to edit modules in dnSpy?** Right-click on the module and select `Edit Module`. Then you can edit the code the way you want. Press compile and it will compile the code. Finally select `Save Module...` from `File` tab. You can now run the `Game.exe` file and see the changes.  
Now after changing `FixedUpdate` function, you can see that the player's velocity has been increased and with this speed we can reach the dungeon.  
When we reach there, we see the `beasts`! It seems their first position is showing the flag but they are really speedy and are getting closer to the player! So if we could reduce the velocity of the `beasts` then they will move slowly.  
We have to look for `o` function and see where it is used. Maybe it is used in order to set the velocity of the `beasts`.   
Here it is and it is used in three different parts. So we just changed its argument to `new Vector3(0,0,0)` and compiled it.    
```c#
private void FixedUpdate()
  {
    if (Vector3.Distance(this.x.position, this.y) < this.chaseLenght)
    {
      this.v = (Vector3.Distance(this.x.position, this.y) < this.triggerLenght);
      if (this.v)
      {
        if (!this.w)
        {
          this.o(new Vector3(0,0,0));
        }
      }
      else
      {
        this.o(new Vector3(0,0,0));
      }
    }
    else
    {
      this.o(new Vector3(0,0,0));
      this.v = false;
    }
    this.w = false;
    this.bn.OverlapCollider(this.filter, this.ba);
    for (int i = 0; i < this.ba.Length; i++)
    {
      if (!(this.ba[i] == null))
      {
        if (this.ba[i].tag == "Fighter" && this.ba[i].name == "Player")
        {
          this.w = true;
        }
        this.ba[i] = null;
      }
    }
  }
```
Now when we run the game, not only the player is fast, but also the beats are not moving. And we can see the flag!  
`nite{Eb1c_9aM3R}`  