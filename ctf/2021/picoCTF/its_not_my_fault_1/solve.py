from pwn import *
import hashlib
import string
import sys
import collections

host = 'mercury.picoctf.net'
port = 56093

p = remote(host, port)

line = p.recvline().decode().split()
pref = line[6][1:-1]
suf = line[-1]

def final_solve():
	p.recvuntil(b'Modulus : ')
	n = int(p.recvline().strip())
	p.recvuntil(b'Clue : ')
	clue = int(p.recvline().strip())
	print(n)
	print(clue)
	p.interactive()


def solve(cur):
	queue = collections.deque([cur])
	while queue:
		cur = queue.popleft()
		user_hash = hashlib.md5(cur.encode())
		if user_hash.hexdigest()[-6:] == suf:
			p.sendline(cur.encode())
			final_solve()
			sys.exit(0)
		for ch in string.digits:
			queue.append(cur + ch)

print(pref, suf)
solve(pref)
