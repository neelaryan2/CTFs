import sys
from numpy import int32, int8

with open('control.bin', 'rb') as fp:
	code = fp.read()

def ptr(idx):
	if 4 * idx >= len(code):
		sys.exit(0)
	chunk = code[4 * idx:4 * idx + 4]
	chunk = int.from_bytes(chunk, byteorder='little')
	return int32(chunk)

def custom_print(s, **kwargs):
	print(hex(4 * index), ':', s, **kwargs)


index = 0
while True:

	cur_bytes = ptr(index)

	if (cur_bytes & 0x40000) != 0:
		custom_print('add  r1 r2')

	if (cur_bytes & 0x80000) != 0:
		custom_print('mul  r1 r2')

	if (cur_bytes & 0x20000) != 0:
		custom_print('shr  r1 r2')

	if (cur_bytes & 0x100000) != 0:
		custom_print('xor  r1 r2')
	
	if (cur_bytes & 0x200000) != 0:
		custom_print('test  r1 r2')
	
	if (cur_bytes & 4) != 0:
		custom_print('mov  reg1 another_index')
	
	if (cur_bytes & 0x20) != 0:
		custom_print('mov  reg2 another_index')
	
	if (cur_bytes & 0x100) != 0:
		custom_print('mov  reg3 another_index')
	
	if (cur_bytes & 0x800) != 0:
		custom_print('mov  reg4 another_index')
	
	if (cur_bytes & 0x4000) != 0:
		custom_print('mov  reg5 another_index')
	
	if (cur_bytes & 2) != 0:
		custom_print('ld  reg1')
	
	if (cur_bytes & 0x10) != 0:
		custom_print('ld  reg2')
	
	if (cur_bytes & 0x80) != 0:
		custom_print('ld  reg3')
	
	if (cur_bytes & 0x400) != 0:
		custom_print('ld  reg4')
	
	if (cur_bytes & 0x2000) != 0:
		custom_print('ld  reg5')
	
	if (cur_bytes & 0x800000) != 0:
		custom_print('load [another_index]')
	
	if (cur_bytes & 0x4000000) != 0:
		custom_print('read [rip + 1]')
	
	if (cur_bytes & 0x8000000) != 0:
		custom_print('read [another_index]')
	
	if (cur_bytes & 0x2000000) != 0:
		custom_print('getchar')
	
	if (cur_bytes & 1) != 0:
		custom_print('st  reg1')
	
	if (cur_bytes & 8) != 0:
		custom_print('st  reg2')
	
	if (cur_bytes & 0x40) != 0:
		custom_print('st  reg3')
	
	if (cur_bytes & 0x200) != 0:
		custom_print('st  reg4')
	
	if (cur_bytes & 0x1000) != 0:
		custom_print('st  reg5')
	
	if (cur_bytes & 0x8000) != 0:
		custom_print('st  r1')
	
	if (cur_bytes & 0x10000) != 0:
		custom_print('st  r2')
	
	if (cur_bytes & 0x400000) != 0:
		custom_print('store  [another_index]')
	
	if (cur_bytes & 0x1000000) != 0:
		custom_print('putchar')
	
	if (cur_bytes & 0x10000000) != 0:
		custom_print('inc rip')
	
	if (cur_bytes & 0x20000000) != 0:
		custom_print('inc rip')
		custom_print('inc rip')
	
	if (cur_bytes & 0x40000000) != 0:
		custom_print('jmp')

	index += 1
