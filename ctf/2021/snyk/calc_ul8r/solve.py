from pwn import *
import sympy as sp
import sys

host = '35.211.207.36' 
port = 8000

p = remote(host, port)
p.recvlines(7)

def solve():
	eq = p.recvline().decode().strip()
	if 'SNYK' in eq:
		print(eq)
		p.close()
		sys.exit(0)
	print('Solving', eq)
	sympy_eq = sp.sympify('Eq(' + eq.replace('=', ',') + ')')
	ans = sp.solve(sympy_eq)[0]
	p.sendlineafter(b' = ', str(ans).encode())
	p.recvline()

while True:
	solve()

