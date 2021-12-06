#!/usr/bin/python3

import random
from math import gcd

mod = 256
header = b'\x25\x50\x44\x46'


def decrypt(dt, a, b):
    assert gcd(a, mod) == 1
    a_inv = pow(a, -1, mod)
    res = b''
    for byte in dt:
        dec = ((byte - b) * a_inv) % mod
        res += bytes([dec])
    return res


domain = list(range(1, mod))
cnt = 0

with open('encrypted.bin', 'rb') as fp:
    enc = fp.read()

enc_head = enc[:len(header)]
dec = None

for a in domain:
    if gcd(a, mod) == 1:
        for b in domain:
            dec_head = decrypt(enc_head, a, b)
            if dec_head.startswith(header):
                cnt += 1
                dec = decrypt(enc, a, b)

assert cnt == 1
with open('letter.pdf', 'wb') as fp:
    fp.write(dec)
