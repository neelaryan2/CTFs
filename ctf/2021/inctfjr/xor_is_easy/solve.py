from itertools import cycle
import os

def xor(a,b):
    return bytes([i^j for i,j in zip(a,cycle(b))])


def generatekey(sz) :
    return os.urandom(sz)


def encrypt(m) :
    return xor("Message : " + m + ":e.o.m" ,generatekey(28))

pref = b"Message : shaktictf{X"
suf = b"}:e.o.m"

c = open("cipher.txt","rb").read()
mid = bytes(c[len(pref):-len(suf)])
p = pref + mid + suf
k = xor(c, p)

# for i in range(0, len(k), 28):
#     print([t for t in k[i:i+28]])

left = 28 - len(pref) - len(suf)
key1 = k[:len(pref)] + bytes(c[len(pref):len(pref) + left]) + k[-len(suf):]
key2 = k[:len(pref)] + bytes(c[28+len(pref):28+len(pref) + left]) + k[-len(suf):]

print(xor(c,key1)[:28] + xor(c,key2)[28:])