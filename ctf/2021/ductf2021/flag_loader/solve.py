from pwn import *
import sys
from z3_solve import *

host = 'pwn-2021.duc.tf'
port = 31919

# p = process(['./flag_loader'])
p = remote(host, port)

p.recvuntil(b'letters: ')

payload, wait1 = check1()
payload = bytes(payload)

p.send(payload)
p.recvuntil(b' = ')

c2 = int(p.recvline().decode().strip())
x, y, wait2 = check2(c2)

p.sendline(f'{x} {y}'.encode())
p.recvuntil(b' = ')

c3 = int(p.recvline().decode().strip())
ans, wait3 = check3(c3)
payload = ' '.join([str(t) for t in ans])
p.sendline(payload.encode())

print('Final Wait:', (wait1 * wait2 * wait3) & 0xffffffff)

p.interactive()
# print(p.recvall())

p.close()
