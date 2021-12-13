## Lost Dungeon 2

### Challenge Description

Welcome Adventurer! There is a portal that teleports you to other levels but unfortunately only wizards can use it. Can you figure out how to make the portal work and get to the hidden level "level0"?  

The files are the same as that of Lost Dungeon 1   

### Writeup

There is something about `portal` and `wizard`! There is a `Portal` class and it checks if the `name` is `Wizard` one of the scenes should be loaded. First we can patch the if condition.  
In the description we can see that it is told to us to enter level0. Let's explore the scenes. We can write them inside a file and see the scenes names. There is 4 scenes: `level0`, `level0`, `Dungeon1`, `Dungeon2`. I tested each of them and understood that we have to load a level0 scene which means the first (zero) or the second index (one). Here is the changed method:  
```c#
protected override void b(Collider2D a)
{
	if (a.name != "Wizard")
	{
		GameManager.instance.SaveState();
		SceneManager.LoadScene(this.sceneNames[0]);
	}
}
```  
We ran `Game.exe` after the previousely mentioned changes and the map changed. NPC's are telling us something about `spawning` and `respawning`. If we look at the `GameManager` class, there is two methods using `SpawnPoint` and `RespawnPoint`. After analyzing these two methods, we see that the one which uses `RespawnPoint` is not used anywhere. So we changed `SpawnPoint` to `RespawnPoint` and ran the game again.  
So we could see the flag!  
`nite{L3vel_100_Maf1a_b055}`