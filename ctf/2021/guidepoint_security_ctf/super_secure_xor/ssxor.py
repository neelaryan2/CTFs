import binascii
flag = 'StormCTF{Crypto4:blahblahblah}'
flag_rev = list(flag[::-1])

stuff = zip(flag, flag_rev)
x = lambda x, y: chr(ord(x) ^ ord(y))

out = list()
out += [x(s[0], s[1]) for s in stuff]

final = [str(b, 'ascii') for b in [binascii.hexlify(bytes(x, 'utf-8')) for x in out]]
print(''.join(final))

stuff = zip(flag_rev, out)
out = list()
out += [x(s[0], s[1]) for s in stuff]
print(''.join(out))