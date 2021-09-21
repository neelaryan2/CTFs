import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
enc = 'mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj'

def b16_decode(cipher):
	assert len(cipher) % 2 == 0
	dec = ""
	for i in range(0, len(cipher), 2):
		cur = 0
		for ch in cipher[i:i + 2]:
			cur = 16*cur + ALPHABET.index(ch)
		dec += chr(cur)
	return dec


for k in range(len(ALPHABET)):
	cur = ''
	for ch in enc:
		c = ALPHABET.index(ch)
		c = (c - k + len(ALPHABET)) % len(ALPHABET)
		cur += ALPHABET[c]
	print(b16_decode(cur))


# def shift(c, k):
# 	t1 = ord(c) - LOWERCASE_OFFSET
# 	t2 = ord(k) - LOWERCASE_OFFSET
# 	return ALPHABET[(t1 + t2) % len(ALPHABET)]

# flag = "redacted"
# key = "redacted"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

# b16 = b16_encode(flag)
# enc = ""
# for i, c in enumerate(b16):
# 	enc += shift(c, key[i % len(key)])
# print(enc)
