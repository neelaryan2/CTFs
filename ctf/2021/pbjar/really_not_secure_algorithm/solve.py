from Crypto.Util.number import long_to_bytes

p = 194522226411154500868209046072773892801
q = 288543888189520095825105581859098503663
e = 65537
c = 2680665419605434578386620658057993903866911471752759293737529277281335077856

n = p * q
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)
m = pow(c, d, n)

print(long_to_bytes(m))