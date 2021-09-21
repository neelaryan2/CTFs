from dec import *
import os

xors = premodify(b'\x00' * 30)[:-2]

a = [c1 ^ c2 for c1, c2 in zip(modify(aznh, -1), xors)]

print(bytes(a))
