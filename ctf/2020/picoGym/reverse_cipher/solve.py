with open('rev_this') as fp:
	flag = fp.read()
print(flag)
flag = [ch for ch in flag]
for i in range(8, len(flag)-1):
	c = ord(flag[i])
	if i & 1 :
		flag[i] = chr(c + 2)
	else :
		flag[i] = chr(c - 5)
print(''.join(flag))
