import itertools
import string

enc = "3E3?6]QHKTHQQBEETTNKZQ]K]?K<KHH<BQ<KQT<QHNT"

def add(st, l, r, off):
	ret = [j for j in st]
	for i in range(l, r + 1):
		ret[i] = st[i] + off
	return ret

def disp(st):
	print(''.join([chr(i) for i in st]))

enc = [ord(i)//3 for i in enc]
enc = [i*4 for i in enc]

enc = add(enc, 0, 7, -3)
enc = add(enc, 9, 15, +5)
enc = add(enc, 17, 24, -7)
enc = add(enc, 25, 34, +13)
enc = add(enc, 38, 42, +13)

offs = [2, 0, 2, 3, 1, 2, 0, 2, 3, 0, 0, 2, 2, 2, 1, 0, 3, 0, 2, 2, 1, 0, 1, 2, 2, 0, 2, 2, 3, 2, 2, 2, 0, 1, 2, 2, 3, 2, 2, 0, 2, 0, 0]

already = []
for i in range(len(offs)):
	enc[i] += offs[i]
	already.append(enc[i])

num = min(5, len(enc) - len(offs))

arr = [list(range(4))] * num
arr = list(itertools.product(*tuple(arr)))

for tup in arr:
	cur = []
	for i in range(num):
		el = enc[i + len(offs)]
		cur.append(el + tup[i])
	print(tup, end=' ')
	disp(already + cur)

