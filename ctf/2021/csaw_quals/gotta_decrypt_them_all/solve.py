import base64
from Crypto.Util.number import long_to_bytes
from pwn import *
import sys

morse_map = [('0', '-----'), ('1', '.----'), ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.')]
morse_inv = {v: k for k, v in morse_map}

normalAlpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rot13Alpha = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'


def find_invpow(x, n):
    high = 1
    while high**n < x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        cur = mid**n
        if low < mid and cur < x:
            low = mid
        elif high > mid and cur > x:
            high = mid
        else:
            return mid
    return mid + 1


def rot13(text):
    return text.translate(str.maketrans(normalAlpha, rot13Alpha))


def decrypt(s):
    words = []
    for w in s.split('/'):
        c = [morse_inv[l] for l in w.split()]
        c = chr(int(''.join(c)))
        words.append(c)
    words = ''.join(words)
    words = base64.b64decode(words)
    params = words.decode().split('\n')
    params = sorted(params)
    n = int(params[0][4:])
    c = int(params[1][4:])
    e = int(params[2][4:])
    m = find_invpow(c, 3)
    m = long_to_bytes(m)
    m = rot13(m.decode())
    print(m)
    return m.encode()


host = 'crypto.chal.csaw.io'
port = 5001
conn = remote(host, port)

for i in range(6):
    conn.recvlines(3)
    s = conn.recvline().decode().strip()
    m = decrypt(s)
    conn.sendline(m)

conn.recvlines(2)
message = conn.recvline().decode().strip()
print(message)
