from pwn import *
import binascii
from rsa_algos import *

host = 'crypto.chal.csaw.io' 
port = 5008

conn = remote(host, port)

# ================================================
(conn.recvlines(2))
n = int(conn.recvline().decode().strip()[4:])
e = int(conn.recvline().decode().strip()[4:])
c = int(conn.recvline().decode().strip()[4:])
(conn.recvlines(2))

d = wiener_attack(e, n)
m = pow(c, d, n)
m = binascii.unhexlify(hex(m)[2:])
print(m)
conn.sendline(m)


# ================================================
(conn.recvlines(3))
n = int(conn.recvline().decode().strip()[4:])
e = int(conn.recvline().decode().strip()[4:])
c = int(conn.recvline().decode().strip()[4:])
(conn.recvlines(2))

s = isqrt(n)
p, q = None, None
while True:
	if s * (s + 6) == n:
		p, q = s, s + 6
		break
	s -= 1
assert p is not None
d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, n)
m = binascii.unhexlify(hex(m)[2:])
print(m)
conn.sendline(m)


# ================================================

(conn.recvlines(3))
n = int(conn.recvline().decode().strip()[4:])
e = int(conn.recvline().decode().strip()[4:])
c = int(conn.recvline().decode().strip()[4:])
(conn.recvlines(2))

conn.sendline(b'1234')
(conn.recvlines(2))

def oracle(q):
	conn.sendline(b'yes')
	conn.sendline(str(q).encode())
	conn.recvuntil(b'with: ')
	r = int(conn.recvline().strip().decode())
	return r

m = lsb_attack(n, e, c, oracle)
print(m)
conn.sendline(b'no')
conn.sendline(m.encode())

while True:
	print(conn.recvline())


conn.close()