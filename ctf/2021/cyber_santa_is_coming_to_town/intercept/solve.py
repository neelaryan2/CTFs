import binascii
import string

with open('data', 'rb') as fp:
	data = fp.read()

packets = [
	'5b2fedd48019',
	'd4fe6223f1d1984638a9',
	'521ac5877a24eed19b0c0ae9f16d4c02cc86773bfaa8924a',
	'cc075e8ce920774e',
	'59eabc3f3626ded46621d3b0ca441afce552274bd6da1f2a'
]
packets = [binascii.unhexlify(t) for t in packets]

def encrypt(s):
	state = 0
	mask = 0xff
	enc = []
	for b in s:
		a = b ^ ((state + 19) & mask)
		state += 55
		enc.append(a)
	return bytes(enc)


def decrypt(enc):
	res = []
	for i in range(len(enc)):
		choices = []
		for ch in range(256):
			cur = bytes(res + [ch])
			cur = encrypt(cur)
			if enc.startswith(cur):
				choices.append(ch)
		assert len(choices) == 1
		res.append(choices[0])
		char = chr(res[-1])
	# 	if char in string.printable:
	# 		print(char, end='')
	# print()

	return bytes(res)

idx = [0]

for i, p in enumerate(packets):
	if i in idx: continue
	cur = b''
	# for j in idx:
	# 	cur += packets[j]
	cur += p
	cur = decrypt(cur)
	print(i, cur)

