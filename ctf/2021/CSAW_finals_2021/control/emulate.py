import sys
from numpy import int32, int8

with open('control.bin', 'rb') as fp:
	code = fp.read()

def ptr(idx):
	chunk = code[4 * idx:4 * idx + 4]
	chunk = int.from_bytes(chunk, byteorder='little')
	return int32(chunk)


memory = [int32(0) for _ in range(0x10000)]
cur_bytes = int32(0)
index = int32(0)
another_index = int32(0)
result = int32(0)
r1, r2 = int32(0), int32(0)
reg1 = int32(0)
reg2 = int32(0)
reg3 = int32(0)
reg4 = int32(0)
reg5 = int32(0)

count = 0

while cur_bytes >= 0:

	cur_bytes = ptr(index)
	count += 1

	if count < 100:
		print(hex(index * 4), hex(cur_bytes))

	if (cur_bytes & 0x40000) != 0:
		result = r1 + r2

	if (cur_bytes & 0x80000) != 0:
		result = r1 * r2

	if (cur_bytes & 0x20000) != 0:
		if r2 <= 0:
			raise Exception('FUCK')
			result = int32(r1 << -int8(r2))
		else:
			result = int32(int32(r1) >> r2)

	if (cur_bytes & 0x100000) != 0:
		result = r1 ^ r2
	
	if (cur_bytes & 0x200000) != 0:
		result = int32(r1 == r2)
	
	if (cur_bytes & 4) != 0:
		another_index = reg1
	
	if (cur_bytes & 0x20) != 0:
		another_index = reg2
	
	if (cur_bytes & 0x100) != 0:
		another_index = reg3
	
	if (cur_bytes & 0x800) != 0:
		another_index = reg4
	
	if (cur_bytes & 0x4000) != 0:
		another_index = reg5
	
	if (cur_bytes & 2) != 0:
		result = reg1
	
	if (cur_bytes & 0x10) != 0:
		result = reg2
	
	if (cur_bytes & 0x80) != 0:
		result = reg3
	
	if (cur_bytes & 0x400) != 0:
		result = reg4
	
	if (cur_bytes & 0x2000) != 0:
		result = reg5
	
	if (cur_bytes & 0x800000) != 0:
		result = memory[another_index]
	
	if (cur_bytes & 0x4000000) != 0:
		result = ptr(index + 1)
	
	if (cur_bytes & 0x8000000) != 0:
		result = ptr(another_index)
	
	if (cur_bytes & 0x2000000) != 0:
		result = int32(ord(sys.stdin.read(1)))
	
	if (cur_bytes & 1) != 0:
		reg1 = result
	
	if (cur_bytes & 8) != 0:
		reg2 = result
	
	if (cur_bytes & 0x40) != 0:
		reg3 = result
	
	if (cur_bytes & 0x200) != 0:
		reg4 = result
	
	if (cur_bytes & 0x1000) != 0:
		reg5 = result
	
	if (cur_bytes & 0x8000) != 0:
		r1 = result
	
	if (cur_bytes & 0x10000) != 0:
		r2 = result
	
	if (cur_bytes & 0x400000) != 0:
		memory[another_index] = result
	
	if (cur_bytes & 0x1000000) != 0:
		print(chr(result), end='', flush=True)
	
	if (cur_bytes & 0x10000000) != 0:
		index += 1
	
	if (cur_bytes & 0x20000000) != 0:
		index += 2
	
	if (cur_bytes & 0x40000000) != 0:
		index = result
