import binascii
import string

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

c = '2e1209315c05627148004b3b46160a565858560a16463b4b00487162055c3109122e'
c = binascii.unhexlify(c)

for b1, b2 in zip(c, c[::-1]):
	assert b1 == b2

prefix = b'StormCTF{Crypto4:'
suffix = b'}'
p = len(prefix)

for b1, b2 in zip(c, c[::-1]):
	assert b1 == b2

flag = [0] * len(c)
flag[:p] = list(prefix)
flag[-p:] = [b1 ^ b2 for b1, b2 in zip(c[:p], prefix)][::-1]

print(bytes(flag))
