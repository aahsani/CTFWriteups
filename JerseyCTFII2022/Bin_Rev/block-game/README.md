## block-game

### Challenge Description  

There's mining, and there's crafting, but something seems off...  

### Writeup
Use jd-gui. There is a `systems` package with 6 classes. We can find the order of occurance betwen each system using events.  
```java
// Red System : printFlag

DATA = new byte[] { 
      104, 65, 111, -41, 119, -19, -59, 19, 118, 102, 
      92, -35, 70, -92, -49, -33, 61, -74, -17, -90, 
      Byte.MIN_VALUE, 31, -86, -94, 67, -55, 16, -67, 91, -113, 
      63, 41, 81, 49, -75, 103, 79 }
public String printFlag() {
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { IronArrowComponent.class }))
      e.send((Event)new CrystalEvent(DATA)); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { LoneSunComponent.class }))
      e.send((Event)new CrystalEvent(DATA)); 
    return "If all your entities are in order, you should receive your flag shortly...";
  }

// -------------------------------------------------------------  
// orange system: onCrystal

public void onCrystal(CrystalEvent event, EntityRef entity, LoneSunComponent comp) {
    byte[] data = event.getData();
    for (int i = 0; i < data.length; i++)
      data[i] = (byte)(data[i] ^ 0xFFFFFFFF); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { RedHurricaneComponent.class }))
      e.send((Event)new GraciousEvent(data)); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { AnxiousFoxComponent.class }))
      e.send((Event)new GraciousEvent(data)); 
  }
// -------------------------------------------------------------
// yellow system: onGracious

public void onGracious(GraciousEvent event, EntityRef entity, AnxiousFoxComponent comp) {
    byte[] data = event.getData();
    for (int i = 0; i < data.length; i++)
      data[i] = (byte)(data[i] ^ 0x47); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { IronArrowComponent.class }))
      e.send((Event)new CruelEvent(data)); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { EqualAlphaComponent.class }))
      e.send((Event)new CruelEvent(data)); 
  }
// -------------------------------------------------------------------------------------------
// Green system: onCruel

public void onCruel(CruelEvent event, EntityRef entity, IronArrowComponent comp) {
    byte[] data = event.getData();
    for (int i = 1; i < data.length; i++)
      data[i] = (byte)(data[i] ^ data[i - 1]); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { LoneSunComponent.class }))
      e.send((Event)new PreciousEvent(data)); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { EqualAlphaComponent.class }))
      e.send((Event)new PreciousEvent(data)); 
  }
// -------------------------------------------------------------------------------------------
// Blue system
DATA = new byte[] { 
      -70, 74, -118, -9, 37, 105, 69, -119, 103, -88, 
      91, 19, -58, -58, -19, -16, 100, 65, 42, 79, 
      27, -45, -125, -38, 119, 8, -121, -8, 67, 71, 
      -2, 62, -34, 93, 0, -116, 54 };

public void onPrecious(PreciousEvent event, EntityRef entity, EqualAlphaComponent comp) {
    byte[] data = event.getData();
    for (int i = 0; i < data.length; i++)
      data[i] = (byte)(data[i] ^ DATA[i]); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { RedHurricaneComponent.class }))
      e.send((Event)new GracefulEvent(data)); 
    for (EntityRef e : this.entityManager.getEntitiesWith(new Class[] { AnxiousFoxComponent.class }))
      e.send((Event)new GracefulEvent(data)); 
  }
// -------------------------------------------------------------------------------------------
// Purpule system: onGraceful
public void onGraceful(GracefulEvent event, EntityRef entity, RedHurricaneComponent comp) {
    byte[] data = event.getData();
    String flag = new String(data);
    this.console.addMessage(flag);
  }
```
In python we have code bellow.  
```python
def onCrystal(data):
	for i in range(0,len(data)):
		data[i] = data[i] ^ 0xFFFFFFFF;
	return data

def onGracious(data):
	for i in range(0,len(data)):
		data[i] = data[i] ^ 0x47; 
	return data

def onCruel(data):
	for i in range(1,len(data)):
		data[i] = data[i] ^ data[i - 1]; 
	return data

blue_data = [-70, 74, -118, -9, 37, 105, 69, -119, 103, -88, 91, 19, -58, -58, -19, -16, 100, 65, 42, 79, 27, -45, -125, -38, 119, 8, -121, -8, 67, 71, -2, 62, -34, 93, 0, -116, 54]
def onPrecious(data):
	for i in range(0,len(data)):
		data[i] = data[i] ^ blue_data[i];
	return data

def onGraceful(data):
	res = []

	for i in range(0,len(data)):
		try:
			res.append(chr(data[i]))
		except Exception as e:
			res.append(chr(data[i] + 4294967296))
	return "".join(res)

# red system
MIN_VALUE = -128
red_data = [104, 65, 111, -41, 119, -19, -59, 19, 118, 102, 92, -35, 70, -92, -49, -33, 61, -74, -17, -90, MIN_VALUE, 31, -86, -94, 67, -55, 16, -67, 91, -113, 63, 41, 81, 49, -75, 103, 79]

crystal = onCrystal(red_data)
gracious = onGracious(crystal)
cruel = onCruel(gracious)
precious = onPrecious(cruel)
flag = onGraceful(precious)
print(flag)

# jctf{b3Tter_th4N_tH3_0r1giN4l_a093c0}
```