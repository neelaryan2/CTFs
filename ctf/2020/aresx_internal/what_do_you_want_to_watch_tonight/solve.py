import hashlib, sys

target = 'e9542c34b5e18df5404994e6650d79a8484755d3c394a36b1da522c4b5e94eb22c43543b6c4df486201528f967e4cb04'

with open('episodes.txt', 'r') as fp:
	names = fp.readlines()

final = []

for episode in names:
	name = episode.split()
	if len(name) > 1 : continue
	name = name[0].lower()
	for i in range(100):
		cur = str(i)
		if i < 10 :	cur = '0' + cur
		final.append(name + cur)

for cur in final:
	hashed = hashlib.sha3_384(cur.encode()).hexdigest()
	if hashed == target :
		print(cur)
		sys.exit()


