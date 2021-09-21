from pwn import *
from tqdm import tqdm

host = 'mercury.picoctf.net' 
port = 33780

def get(conn, txt):
	conn.recvuntil(str(txt).encode())
	line = conn.recvline()[:-1]
	return int(line.decode())

def oracle(conn, cipher):
	conn.recvuntil(b'decrypt: ')
	conn.sendline(str(cipher).encode())
	return get(conn, 'go: ')

conn = remote(host, port)

n = get(conn, 'n: ')
e = get(conn, 'e: ')
c = get(conn, 'ciphertext: ')

x = pow(2, e, n)
y = (x * c) % n
u = oracle(conn, y)
inv = (n + 1) // 2
m = (inv * u) % n

# print(m)
m = bytearray.fromhex(hex(m)[2:]).decode()
print(m)