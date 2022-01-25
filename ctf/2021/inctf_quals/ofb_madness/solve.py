from pwn import *
import binascii

def query(p, s):
	s = s.hex().encode()
	p.sendlineafter(b'> ', s)
	r = p.recvline().strip()
	r = binascii.unhexlify(r)
	return r

if args.LOCAL:
	p = process(['python3', 'chall.py'])
else:
	host = 'gc1.eng.run'
	port = 30074
	p = remote(host, port)

data = p.recvlines(3)[-1]
data = binascii.unhexlify(data)
iv, enc = data[:16], data[16:]

m1 = b'a' * len(enc)
c1 = query(p, iv + m1)
flag = xor(c1, m1, enc).decode()

log.info(f'Flag: {flag}')

p.close()