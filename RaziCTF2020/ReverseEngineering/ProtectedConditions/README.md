## Protection Conditions

### Challenge Description

This guy protected his dice program with a weird serial number. Can you crack it?  

### Writeup

In this challenge an exe file is given. Open it in IDA Pro. Look for "Enter Serial Number" string part. You can see a lot of if statements that they compare each charachter of input with a variable. If you put these variables together in specific order, you can find flag:  
```
RaziCTF{Protected_Source_Code_dccef51a}
```
