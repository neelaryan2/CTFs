from random import randint
from Crypto.Util.number import long_to_bytes, bytes_to_long
from pwn import *

host = 'crypto.chal.csaw.io'
port = 5006

# conn = process(['python3', 'forgery.py'])
conn = remote(host, port)
conn.recvuntil(b': ')

line = conn.recvline().decode().strip()
p, g, y = tuple(map(int, line.split()))

MASK = 2**1024 - 1
e = randint(1, p - 1)
r = y * pow(g, e, p) % p
s = -r % (p - 1)

m = bytes_to_long(b'Felicity') << 1024
m += (e * s) % (p - 1)
m = hex(m)[2:].encode()

conn.sendlineafter(b'Answer: ', m)
conn.sendlineafter(b'r: ', str(r).encode())
conn.sendlineafter(b's: ', str(s).encode())
conn.recvuntil(b'Arrow!')

conn.recvline()
flag = conn.recvline().strip().decode()
print(flag)
