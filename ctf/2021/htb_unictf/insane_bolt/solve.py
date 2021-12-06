from pwn import *
from copy import deepcopy
from collections import deque

# HTB{w1th_4ll_th353_b0lt5_4nd_g3m5_1ll_cr4ft_th3_b35t_t00ls}

racer = '🤖'
diamond = '💎'
bad = '☠️'

def bfs(grid):
	n, m = len(grid), len(grid[0])

	start, end = None, None
	for x in range(n):
		for y in range(m):
			if grid[x][y] == racer:
				start = (x, y)
			if grid[x][y] == diamond:
				end = (x, y)
	assert None not in [start, end]

	visited = [[False for j in range(m)] for i in range(n)]
	parent = [[-1 for j in range(m)] for i in range(n)]
	found = False
	sx, sy = start
	visited[sx][sy] = True
	parent[sx][sy] = start
	queue = deque([start])

	while queue:
		x, y = queue.popleft()
		if grid[x][y] == diamond:
			found = True
			break
		for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
			if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] != bad and not visited[x2][y2]:
				visited[x2][y2] = True
				parent[x2][y2] = (x, y)
				queue.append((x2, y2))

	assert found

	vx, vy = end
	ans = ''
	while parent[vx][vy] != (vx, vy):
		ux, uy = parent[vx][vy]
		if vx == ux + 1:
			move = 'D'
		elif vx == ux - 1:
			move = 'U'
		elif vy == uy + 1:
			move = 'R'
		elif vy == uy - 1:
			move = 'L'
		ans += move
		vx, vy = ux, uy

	return ans[::-1]


def parse(data):
	lines = data.decode().split('\n')
	lines = [l.split() for l in lines if l]
	lines = [l[1:-1] for l in lines[1:-1]]
	ans = bfs(lines)
	return ans


host = '64.227.38.214'
port = 30853

p = remote(host, port)
p.sendlineafter(b'> ', b'2')

while True:
	data = p.recvuntil(b'> ')[:-2]
	ans = parse(data)
	p.sendline(ans.encode())
	recv = p.recvlines(2)
	have = [int(l.decode().split()[3]) for l in recv]
	print(have, end='\r')
	if have[0] >= 500 and have[1] >= 5000:
		break
print()
print(p.recvall())
p.close()
