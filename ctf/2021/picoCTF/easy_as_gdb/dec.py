aznh = bytes([0x7a, 0x2e, 0x6e, 0x68, 0x1d, 0x65, 0x16, 0x7c, 0x6d, 0x43, 0x6f, 0x36, 0x3f, 0x62, 0x15, 0x46, 0x43, 0x36, 0x40, 0x37, 0x58, 0x01, 0x58, 0x35, 0x62, 0x6b, 0x53, 0x30, 0x38, 0x17])


def swapper(seq, step):
    if step <= 0:
        return seq
    seq = list(seq)
    for i in range(0, len(seq) - step + 1, step):
        seq[i], seq[i + step - 1] = seq[i + step - 1], seq[i]
    return bytes(seq)


def modify(seq, mode):
    if mode < 0:
        for i in reversed(range(1, len(seq))):
            seq = swapper(seq, i)
    else:
        for i in range(1, len(seq)):
            seq = swapper(seq, i)
    return seq


def shitfuck(seq, idx):
    tmp = []
    for i in range(4):
        cur = idx & ((1 << 8) - 1)
        tmp.append(cur)
        idx >>= 8
    tmp = tmp[::-1]
    return bytes([c ^ tmp[i & 3] for i, c in enumerate(seq)])


def premodify(seq):
    assert len(seq) == 30
    seq += b'\x00\x00'
    for idx in range(180154381, 0xdeadbeef, 2075469):
        seq = shitfuck(seq, idx)
    return seq


def check_input(seq):
    return modify(aznh, -1) == modify(seq, -1)


def main():
    a = input().encode()
    a = premodify(a)[:-2]
    a = modify(a, 1)
    if check_input(a):
        print('Correct')
    else:
        print('Incorrect')
