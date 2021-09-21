import angr
import claripy
import string


def main():

    base_addr = 0x400000

    proj = angr.Project('./checkpass', main_opts={'base_addr': base_addr}, auto_load_libs=False)

    success_addr = base_addr + 0x62ca

    inp_length = 32
    inp_chars = []
    for c in 'picoCTF{':
        inp_chars.append(claripy.BVV(c.encode()))
    for i in range(32):
        inp_chars.append(claripy.BVS('inp_%d' % i, 8))
    inp_chars.append(claripy.BVV(b'}'))
    inp = claripy.Concat(*inp_chars)

    state = proj.factory.full_init_state(
        args=[proj.filename, inp],
        add_options=angr.options.unicorn,
    )

    invalid = [c for c in range(256) if chr(c) not in string.printable]

    for k in inp_chars[8:-1]:
        for c in invalid:
            state.solver.add(k != c)
        # state.solver.add(k < 128)
        # state.solver.add(k > 32)

    simgr = proj.factory.simulation_manager(state)

    simgr.explore(find=success_addr)

    if (len(simgr.found) > 0):
        for found in simgr.found:
            print(found.posix.dumps(0))
    else:
        print('No solutions found')

    # simgr.run()

    # y = []
    # for x in simgr.deadended:
    #     if b'Invalid' not in x.posix.dumps(1):
    #         print(x.posix.dumps(0), ' : ', x.posix.dumps(1))


if __name__ == '__main__':
    main()
