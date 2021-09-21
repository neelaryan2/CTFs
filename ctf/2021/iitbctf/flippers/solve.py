from pwn import *
import binascii

# IITB{fl1pp1n6_b1t_15_fun}

host = '20.197.63.174'
port = 3334

conn = remote(host, port)
# conn = process(['python3', 'flipper.py'])

payload = b'xxxxxxxxxxxxxxxxcsec_iitc'
idx = 8

conn.recvlines(3)
conn.sendline(b'2')
conn.recvuntil(b': ')
conn.sendline(binascii.hexlify(payload))

s = conn.recvline().strip()
s = [c for c in binascii.unhexlify(s)]
s[idx] ^= ord('c') ^ ord('b')
payload = bytes(s)

conn.recvlines(3)
conn.sendline(b'1')
conn.recvuntil(b': ')
conn.sendline(binascii.hexlify(payload))

print(conn.recvline().strip().decode())
