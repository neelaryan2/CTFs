import os

os.chdir('files')

with open('ea6b505ffded681a256232ed214d4c3b410c8b4f052775eb7e67dcbd5af64e63.pdf.cryptastic', 'rb') as fp:
	flag_enc = fp.read()

with open('9df65cc45479c058ef4a600c1e607fec44d83682db732f077817c58bed47a191.pdf.cryptastic', 'rb') as fp:
	p1_enc = fp.read()

with open('20180212_113048_Jones_C_ADMI2017_Ransomware.pdf', 'rb') as fp:
	p1 = fp.read()


def xor(b1, b2):
	return bytes([a1 ^ a2 for a1, a2 in zip(b1, b2)])


k = len(flag_enc)
flag = xor(xor(p1_enc[:k], flag_enc), p1[:k])

with open('flag.pdf', 'wb') as fp:
	fp.write(flag)