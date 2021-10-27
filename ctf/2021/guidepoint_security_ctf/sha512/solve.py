import hashlib
from binascii import hexlify, unhexlify

with open('secret.tc', 'rb') as fp:
	data = fp.read()

chunks = [data[i:i + 64] for i in range(0, len(data), 64)]
hashes = [hexlify(b).decode() for b in chunks]

hashset = set(hashes)

# for a in range(256):
# 	for b in range(256):
# 		for c in range(256):
# 			s = bytes([a, b, c])
# 			m = hashlib.sha512()
# 			m.update(s)
# 			h = m.hexdigest()
# 			if h in hashset:
# 				print(s)
