import numpy as np
import copy

bits = [[0], [1], [2], [3], [4], [5, 0], [6, 1], [7, 2, 0], [8, 3, 1], [9, 4, 2], [10, 5, 3], [11, 6, 4], [12, 7, 5, 0], [13, 8, 6, 1], [14, 9, 7, 2], [15, 10, 8, 3], [16, 11, 9, 4], [17, 12, 10, 5], [18, 13, 11, 6], [19, 14, 12, 7], [20, 15, 13, 8], [21, 16, 14, 9], [22, 17, 15, 10], [23, 18, 16, 11], [24, 19, 17, 12], [25, 20, 18, 13], [26, 21, 19, 14], [27, 22, 20, 15], [28, 23, 21, 16], [29, 24, 22, 17], [30, 25, 23, 18], [31, 26, 24, 19]]

def get_bits(n, b):
	ret = []
	for i in range(b):
		ret.append(n & 1)
		n >>= 1
	return ret


def from_bits(arg):
	arr = list(reversed(arg))
	ret = 0
	for b in arr:
		ret = (ret << 1) + b
	return ret


def solve(target):
	count = 0
	for i in range(256):
		tmp = (target - i) & 0xffffffff
		if i == (tmp >> 1) & 0xff:
			count += 1
			new_target = tmp
	assert count == 1
	b = get_bits(new_target, 32)
	for i in range(32):
		for j in range(1, len(bits[i])):
			c = bits[i][j]
			assert c < i
			b[i] ^= b[c]
	ret = ''
	for i in range(0, 32, 8):
		c = from_bits(b[i:i+8][::-1])
		print(c)
		ret += chr(c)
	print(ret)


solve(-231060518)


