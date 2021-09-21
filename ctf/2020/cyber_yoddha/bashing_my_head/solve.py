import socket
import base64
import re, sys
import math as mt 

MAXN = 1000001
spf = [0 for i in range(MAXN)] 
  
def sieve(): 
	spf[1] = 1
	for i in range(2, MAXN): 
		spf[i] = i 
	for i in range(4, MAXN, 2): 
		spf[i] = 2
	for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
		if (spf[i] == i): 
			for j in range(i * i, MAXN, i):  
				if (spf[j] == j): 
					spf[j] = i 
  
def factorization(x): 
	ret = {}
	try:
		while (x != 1): 
			pr = spf[x]
			if pr not in ret.keys():
				ret[pr] = 0
			ret[pr] += 1
			x //= pr
		return ret
	except:
		print(len(spf)-1)
		print(x)
		sys.exit(0) 

def isprime(x):
	try:
		return int(spf[x] == x)
	except KeyError:
		print(len(spf)-1)
		print(x)
		sys.exit(0) 

def totient(n):
	if n == 0: return 1
	tot = 1
	for p, exp in factorization(n).items():
		tot *= (p - 1)  *  p ** (exp - 1)
	return tot

def gcd(a, b):
	if a == b: return a
	while b > 0: a, b = b, a % b
	return a

sieve()

ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

host = 'cyberyoddha.baycyber.net'
port = 10006

def recvuntil(conn, s):
	so_far = b''
	while so_far[-len(s):] != s:
		b = conn.recv(1)
		if len(b) == 0:
			raise EOFError
		so_far += b
	return so_far

def get(conn, before):
	recvuntil(conn, before.encode())
	ret = recvuntil(conn, b'\x1b[34m')[4:-5]
	return int(base64.b64decode(ret).decode())

def last_time(conn):
	s = conn.recv(4096)
	s = ansi_escape.sub('', s.decode())
	print(s)
	sys.exit(0)


def main():
	p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p.connect((host, port))

	for i in range(20):
		print(i)
		# q0
		n = get(p, 'decrypt this: ')
		p.send(str(n).encode())

		# q1
		n = get(p, 'equal ')
		ans = 'ny'[int(isprime(n))]
		p.send(ans.encode()+b'\n')

		# q2
		n = get(p, 'n is ')
		factors = sorted(list(factorization(n).keys()))
		if len(factors) == 1: factors.append(factors[0])
		p1, p2 = factors
		p.send(str(p1).encode()+b'\n')
		p.send(str(p2).encode()+b'\n')

		# q3
		n = get(p, 'equal ')
		ans = 'ny'[int(isprime(n))]
		p.send(ans.encode()+b'\n')

		# q4
		n = get(p, 'n is ')
		p.send(str(totient(n)).encode()+b'\n')

		# q5
		phi = get(p, 'to be ')
		e = get(p, 'e is ')
		ans = 'ny'[int(gcd(phi, e) == 1)]
		p.send(ans.encode()+b'\n')

	last_time(p)


main()