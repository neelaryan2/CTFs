import binascii
import base64

with open('GOFASTER.txt', 'r') as fp:
	lines = [l.strip() for l in fp if l.strip()]

for l in lines:
	l = binascii.unhexlify(l).decode()
	if l.startswith('StormCTF{'):
		print(l)
		break
