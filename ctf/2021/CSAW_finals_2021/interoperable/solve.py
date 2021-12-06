from pwn import *
import json
from gmpy2 import mpz
from collections import namedtuple

Point = namedtuple("Point", "x y")

host = 'crypto.chal.csaw.io' 
port = 5017

p = remote(host, port)

def send(**kwargs):
    global p
    payload = json.dumps(kwargs).encode()
    p.sendlineafter(b'> ', payload)

G = Point(mpz(0), mpz(0x66485c780e2f83d72433bd5d84a06bb6541c2af31dae871728bf856a174f93f4))
Origin = 'Origin'

send(curve='curve_p256')
send(Gx=hex(G.x)[2:], Gy=hex(G.y)[2:])
send(curve='curve_s256')
send()

p.recvuntil(b'Challenge: ')
Q = eval(p.recvline().strip().decode())
if Q == Origin:
    ans = 0
elif Q == G:
    ans = 1
else:
    ans = 2

send(d=hex(ans)[2:])

recv = p.recvrepeat(5).decode()
print(recv.strip())

p.close()
