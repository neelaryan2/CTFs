with open('chall.png', 'rb') as fp:
	data = fp.read()

header = data[:8]
data = data[8:]

newfile = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'

while data:
	length = int.from_bytes(data[:4], 'big')
	ctype = data[4:8]
	cdata = data[8:8 + length]
	crc = data[8 + length: 12 + length]

	old_ctype = ctype
	ctype = list(ctype)
	ctype[1], ctype[2] = ctype[2], ctype[1]
	ctype = bytes(ctype).upper()

	chunk = data[:12 + length].replace(old_ctype, ctype)
	newfile += chunk
	data = data[12 + length:]

	print(old_ctype, ctype, length)


with open('new.png', 'wb') as fp:
	fp.write(newfile)