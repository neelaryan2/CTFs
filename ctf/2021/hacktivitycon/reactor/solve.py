import base64

n = 'U1VTUE5aVFVXDVEBUFoHDlZcAQYDXApTAg8GA1RaBlQCCVMGB0Q='
n = base64.b64decode(n)


def xor(b1, b2):
    return bytes([a1 ^ a2 for a1, a2 in zip(b1, b2)])


def decrypt(pin):
    c = str(pin).rjust(4, '0')
    while len(c) < len(n):
        c += c
    return xor(c.encode(), n)


for i in range(10000):
    cur = decrypt(i)
    if cur[:4] == b'flag':
        print(cur)
