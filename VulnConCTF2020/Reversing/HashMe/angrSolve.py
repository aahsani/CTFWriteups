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
