from binascii import unhexlify

c = '551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b'
k = '236625611d392070281d3971731d3922251d3923201d3922751d392423702f1d'

ch = ord('A')
c = unhexlify(c)
k = unhexlify(k)

flag = ''
for t1, t2 in zip(k, c):
    flag += chr(t1 ^ t2 ^ ch)

print('picoCTF{' + flag + '}')
