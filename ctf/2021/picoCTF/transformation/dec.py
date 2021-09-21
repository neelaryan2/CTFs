# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

enc = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽'

flag = ''

for t in enc:
	cur = ord(t)
	lo = cur & ((1 << 8) - 1)
	hi = cur >> 8
	flag += chr(hi) + chr(lo)

print(flag)
