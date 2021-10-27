import sys, os
from binascii import hexlify


def conv(d):
    return int(chr(d), 16)


def load(d):
    d = list(map(conv, d))
    ret = f'ld R{d[3]}, [R{d[1]} R{d[2]}]'
    return ret


def store(d):
    d = list(map(conv, d))
    ret = f'st [R{d[1]} R{d[2]}] R{d[3]}'
    return ret


def arith(d):
    d = list(map(conv, d))
    names = ['add', 'sub', 'mul', 'div', 'mod', 'shl', 'shr', 'and', 'or', 'xor', 'mov']
    name = names[d[1]]
    ret = f'{name} R{d[2]} R{d[3]}'
    return ret


def imm(d):
    i = int(d[-2:].decode(), 16)
    d = list(map(conv, d))
    names = ['add', 'sub', 'mul', 'div', 'mod', 'shl', 'shr', 'and', 'or', 'xor', 'mov']
    name = names[d[1]] + 'i'
    ret = f'{name} R{d[2]} {i}'
    return ret


def cmp(d):
    d = list(map(conv, d))
    ret = f'cmp R{d[1]} R{d[3]}'
    return ret


def cmpi(d):
    i = int(d[2:].decode(), 16)
    d = list(map(conv, d))
    ret = f'cmpi R{d[1]} {i}'
    return ret


def control(d):
    idx = list(map(conv, d[:1]))[0] - 6
    funcs = ['jmp', 'je', 'jne', 'jl', 'jg', 'call']
    i = int(d[-4:].decode(), 16)
    ret = f'{funcs[idx]} {hex(i)}'
    return ret


def dis(data):
    ptr = 0

    funcs = [(load, 4), (store, 4), (arith, 4), (imm, 6), (cmp, 4), (cmpi, 4), (control, 6)]
    while ptr < len(data):
        op = conv(data[ptr])
        func, size = funcs[min(op, len(funcs) - 1)]
        instr = func(data[ptr:ptr + size])
        addr = '0x' + hex(ptr)[2:].rjust(4, '0')
        print(f'{addr}:\t{instr}')
        ptr += size


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python3 {sys.argv[0]} bytecode_file')
        sys.exit(0)

    with open(sys.argv[1], 'rb') as fp:
        data = hexlify(fp.read())

    dis(data)
