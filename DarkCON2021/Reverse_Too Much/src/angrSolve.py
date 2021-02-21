import angr
import claripy


success = 0x1046dd
fail = 0x1046eb

FLAG_LEN = 200
STDIN_FD = 0

base_addr = 0x100000 # To match addresses to Ghidra

proj = angr.Project("./rev", main_opts={'base_addr': base_addr}) 

flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(FLAG_LEN)]

flag = claripy.Concat( *flag_chars + [claripy.BVV('\n', 8)])
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
