import angr
import claripy
import string


def main():

    base_addr = 0x00400000
    # base_addr = 0x00100000
    # base_addr = 0x0

    success_addr = base_addr + 0x106d
    failure_addr = base_addr + 0x105f

    invalid = [c for c in range(128) if chr(c) not in string.printable]

    proj = angr.Project('./remote', main_opts={'base_addr': base_addr})

    inp_chars = []
    for c in 'D1v1':
        inp_chars.append(claripy.BVV(c.encode()))
    for i in range(12):
        cur = claripy.BVS('inp_%d' % i, 8)
        inp_chars.append(cur)

    inp_chars.append(claripy.BVV(b'\n'))

    inp = claripy.Concat(*inp_chars)

    state = proj.factory.full_init_state(args=[proj.filename], add_options=angr.options.unicorn, stdin=inp)

    for k in inp_chars[4:-1]:
        state.solver.add(k < 128)
        # for c in invalid:
            # state.solver.add(k != c)
        # state.solver.add(ord('0') <= k)
        # state.solver.add(ord('f') >= k)

    simgr = proj.factory.simulation_manager(state)
    # simgr.run()
    simgr.explore(find=success_addr)

    if (len(simgr.found) > 0):
        for found in simgr.found:
            print(found.posix.dumps(0))
    else:
        print('No solutions found')


if __name__ == '__main__':
    main()
