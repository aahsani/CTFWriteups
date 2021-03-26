## HashMe

### Challenge Description
I hash I xor what else can I do?  
Flag format: vulncon{flag}  
  
### Writeup

In this challenge you are given an ELF 32 bit.  
Make it executable and run it. You see that it wants you to enter input. 
Decompile this file using ghidra and trace it. The max length for an input can be 32 characters.  
While tracing the code, we see there is a print for success and a print for failure. 
Here we use angr framework in order to solve this challenge. In angr we should use success and failure addresses as `find` and `avoid` addresses for a simulation manager to explore state.  
We use coded below for `FLAG_LEN = 32` , `FLAG_LEN = 31`, `FLAG_LEN = 30` , ... until `FLAG_LEN = 13` which gave us the flag.  

```python:
import angr
import claripy

FLAG_LEN = 13

success = 0x115fc
fail = 0x11610
base_addr = 0x10000

STDIN_FD = 0

proj = angr.Project("./HashMe.bin", main_opts={'base_addr': base_addr}) 

flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(FLAG_LEN)]

flag = claripy.Concat( *flag_chars + [claripy.BVV("\n", 8)])
#flag = claripy.Concat( *flag_chars )

state = proj.factory.full_init_state(stdin=flag)

for k in flag_chars:
    state.solver.add(k >= ord('!'))
    state.solver.add(k <= ord('~'))

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=success, avoid=fail)

print("---------------------")
print(len(simgr.found))

if (len(simgr.found) > 0):
    for found in simgr.found:
        print(found.posix.dumps(STDIN_FD))
```  
Code result: 
```
r3ver5em4s7er
```  
Flag:
```
vulncon{r3ver5em4s7er}
```