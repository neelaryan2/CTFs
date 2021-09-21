import os

nxt, char = {}, {}

for file in os.listdir('chall/'):
	with open('chall/' + file, 'r') as fp:
		lines = [l.strip() for l in fp.readlines() if l.strip()]
	nxt[file] = None if len(lines) < 2 else lines[1].replace('Next character is in ', '')
	char[file] = lines[0]

start = '00000000.txt'
flag = ''
v = start

while True:
	flag += char[v]
	if nxt[v] is None: break
	v = nxt[v]

print(flag)