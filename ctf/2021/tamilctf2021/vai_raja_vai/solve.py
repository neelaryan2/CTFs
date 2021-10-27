from pwn import *
import subprocess
import sys

host = '3.99.48.161'
port = 8002

offset = sys.argv[1] if (len(sys.argv) > 1) else '1'
out = subprocess.check_output(['./check', offset])
nums = out.strip().split()

p = remote(host, port)
# p = process('./vai_raja_vai_client')

for i, n in enumerate(nums):
	print(i)
	p.sendline(n)
	r = p.recvrepeat(1)
	if b'correct' not in r:
		p.close()
		sys.exit(0)
	print(r)

p.close()