import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long, getStrongPrime, inverse
from Crypto.Util.Padding import pad

f = open("chal.py", "rb").read()
c = open("chal.enc", "rb").read()

n = 30004084769852356813752671105440339608383648259855991408799224369989221653141334011858388637782175392790629156827256797420595802457583565986882788667881921499468599322171673433298609987641468458633972069634856384101309327514278697390639738321868622386439249269795058985584353709739777081110979765232599757976759602245965314332404529910828253037394397471102918877473504943490285635862702543408002577628022054766664695619542702081689509713681170425764579507127909155563775027797744930354455708003402706090094588522963730499563711811899945647475596034599946875728770617584380135377604299815872040514361551864698426189453
e = 65537

assert len(f) == 723

streams, es = [], []
for a in range(0, len(f), 256):
    q = f[a:a + 256]
    if len(q) < 256: q = pad(q, 256)
    q = bytes_to_long(q)
    cblock = bytes_to_long(c[a: a + 256])
    stream = q ^ cblock
    streams.append(stream)
    es.append(int(e))
    e = gmpy2.next_prime(e)

inv = inverse(streams[0], n)
m2 = (streams[1] * inv) % n

print(m2)
print(es[0])

# ii = (ii * streams[0]) % n

# print(ii)

# print("len:", len(f))
# p = getStrongPrime(1024)
# q = getStrongPrime(1024)

# n = p * q
# e = 0x10001
# print("n =", n)
# print("e =", e)
# print("# flag length:", len(m))
# m = pad(m, 255)
# m = bytes_to_long(m)

# assert m < n
# stream = pow(m, e, n)
# cipher = b""

# open("chal.enc", "wb").write(cipher)
