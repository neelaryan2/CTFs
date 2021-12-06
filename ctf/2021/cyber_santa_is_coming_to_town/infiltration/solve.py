from pwn import *

host = '138.68.136.191'
port = 32099

p = remote(host, port)

v1 = p.recv(32)
rev_v1 = bytes(reversed(v1))
p.send(rev_v1)

v2 = p.recv(32)
xor_v2 = xor(v2, rev_v1)
p.send(xor_v2)

flag = p.recv(32)[1:].decode()
log.info(f'Flag: {flag}')

p.close()
