ciphertext = b'\x18j|a\x118i7\x1e_}[hK]=\x02\x18\x14{e6E](\x3E\x099VDB};o@W\x7f\x0eY'
ciphertext = bytes([0x18, 0x6a, 0x7c, 0x61, 0x11, 0x38, 0x69, 0x37, 0x1e, 0x5f, 0x7d, 0x5b, 0x68, 0x4b, 0x5d, 0x3d, 0x02, 0x18, 0x14, 0x7b, 0x65, 0x36, 0x45, 0x5d, 0x28, 0x5c, 0x33, 0x45, 0x09, 0x39, 0x56, 0x44, 0x42, 0x7d, 0x3b, 0x6f, 0x40, 0x57, 0x7f, 0x0e, 0x59])

def swap_adjacent(flag):
    n = len(flag)
    ret = b''
    for j in range(0, n - 1, 2):
        ret += bytes([flag[j + 1], flag[j]])
    if n & 1:
        ret += flag[-1:]
    assert len(ret) == n
    return ret

def enc(flag):
    n = len(flag)
    ret = []
    for i, c in enumerate(flag):
        c = flag[i] ^ 20 ^ (i % 10)

        if i > 0:
            c ^= ret[i - 1]
        if i > 2:
            c ^= ret[i - 3]

        if i % 2 == 0:
            c ^= 9
        else:
            c ^= 8

        if i % 3 == 0:
            c ^= 7
        elif i % 3 == 1:
            c ^= 6
        else:
            c ^= 5

        ret.append(c)

    return swap_adjacent(bytes(ret))

def dec(flag):
    flag = swap_adjacent(flag)
    n = len(flag)
    ret = []

    for i in reversed(range(n)):
        c = flag[i] ^ 20 ^ (i % 10)

        if i > 0:
            c ^= flag[i - 1]
        if i > 2:
            c ^= flag[i - 3]

        if i % 2 == 0:
            c ^= 9
        else:
            c ^= 8

        if i % 3 == 0:
            c ^= 7
        elif i % 3 == 1:
            c ^= 6
        else:
            c ^= 5

        ret.append(c)

    return bytes(ret[::-1])
    
print(len(ciphertext))
plaintext = dec(ciphertext)
print(plaintext)
print(enc(plaintext))
print(ciphertext)
# print(len(ciphertext))
# print(dec(ciphertext))