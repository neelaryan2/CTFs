from pwn import *

# conn = remote('20.197.63.174', 3331)
conn = process(['python3', 'game.py'])

def send_replacements(lst):
	global conn
	n = len(lst)
	confirm = [b'y'] * n
	confirm[-1] = b'n'
	for i in range(n):
		conn.sendline(lst[i])
		conn.sendline(confirm[i])

def play_level(lst, level=0):
	global conn
	conn.sendline(b'y')
	send_replacements(lst)
	conn.recvuntil(b'Level passed!\n')

# level 1
play_level([
	b'hacking => CSeC'
], level=1)

# level 2
play_level([
	b'hi => bye',
	b'asc => crash'
], level=2)

# level 3
play_level([
	b'qq => q'
], level=3)

# level 4
play_level([
	b'qq => d', b'qd => d', b'dq => d', b'dd => d',
	b'd => quackquack'
], level=4)

conn.recvuntil(b'Game: ')
flag1 = conn.recvline().strip().decode()
print(flag1)

# level 5
play_level([
	b'*0 => *aR', b'*1 => *bR', 	# init left
	b'R0$ => La$', b'R1$ => Lb$', 	# init right
	b'a0L => aaR', b'a1L => abR', b'b0L => baR', b'b1L => bbR', 	# left turnback 
	b'R0a => Laa', b'R1a => Lba', b'R0b => Lab', b'R1b => Lbb', 	# right turnback
	b'0L => L0', b'1L => L1', 	# move left
	b'R0 => 0R', b'R1 => 1R', 	# move right
	b'L => p', b'aR => p', b'bR => p', 	# base case palindrome 
	b'apa => p', b'bpb => p', 	# palindrome reduction from center
	b'apb => q', b'bpa => q', b'aqa => q', b'bqb => q', b'aqb => q', b'bqa => q', 	# not_palindrome reduction
	b'*p$ => palindrome', b'*q$ => not_palindrome' 	# final answer
], level=5)

conn.recvuntil(b'flag: ')
flag2 = conn.recvline().strip().decode()
print(flag2)

conn.close()
