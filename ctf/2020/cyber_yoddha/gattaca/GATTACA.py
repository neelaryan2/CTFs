c = 'GTTAAAGTTTTCGGT{ACGACTTGCCCTACCTCTTTTATAGTGTCAACTAGGTGCGCATCCAGAATAACCACGATAACCTCTATAAAAACTCTGTCAATATTGTCTCGA}'

c = c.replace('{','').replace('}','')

# print(c)

# with open('GATTACA_map.txt', 'r') as fp:
# 	content = fp.readlines()

# conv = {}
# for i in range(len(content)//2):
# 	k, v = content[2*i:2*i+2]
# 	conv[k[:-1]] = v[:-1]

# print(m)

import itertools
a = 'ACGT'
dic = 'abcdefghijklmnopqrstuvwxyz'
dic += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic += '0123456789_.'

print(len(dic))
for cur in itertools.permutations(a):
	arr = ''.join(list(cur))
	arr = list(itertools.product(*tuple([arr]*3)))
	arr = {''.join(list(a)):dic[i] for i, a in enumerate(arr)}
	m = ''
	for i in range(len(c)//3):
		chunk = c[3*i:3*i+3]
		m += arr[chunk]
	m = m[:5]+'{'+m[5:]+'}'
	print(m)	
