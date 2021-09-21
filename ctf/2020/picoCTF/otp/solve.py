import angr
import claripy

def main():
    
    base_addr = 0x00400000
    # base_addr = 0x00100000
    # base_addr = 0x0
    
    success_addr = base_addr + 0x9e0
    failure_addr = base_addr + 0x9cd

    proj = angr.Project('./otp', main_opts={'base_addr': base_addr}, auto_load_libs=False)
    
    inp_length = 100
    inp_chars = [claripy.BVS('inp_%d' % i, 8) for i in range(inp_length)]
    inp = claripy.Concat(*inp_chars)
    
    state = proj.factory.full_init_state(
    	args=[proj.filename, inp],
    	add_options=angr.options.unicorn,
    )
    
    for k in inp_chars:
    	state.solver.add(ord('0') <= k)
    	state.solver.add(ord('f') >= k)

    simgr = proj.factory.simulation_manager(state)
    simgr.explore(find=success_addr)

    if (len(simgr.found) > 0):
    	for found in simgr.found:
    		print(found.posix.dumps(0))
    else:
    	print('No solutions found')

if __name__ == '__main__':
    main()
    

