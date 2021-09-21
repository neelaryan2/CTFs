from pwn import *
from oweiner import attack

host = 'mercury.picoctf.net' 
port = 41508

def get(conn, txt):
	conn.recvuntil(str(txt).encode())
	line = conn.recvline()[:-1]
	return int(line.decode())

def oracle(conn, cipher):
	conn.recvuntil(b'decrypt: ')
	conn.sendline(str(cipher).encode())
	return get(conn, 'go: ')

conn = remote(host, port)

e = get(conn, 'e: ')
n = get(conn, 'n: ')
c = get(conn, 'c: ')

d = attack(e, n)
if d is None:
    raise Exception("Failed")

m = pow(c, d, n)
m = bytearray.fromhex(hex(m)[2:]).decode()
print(m)