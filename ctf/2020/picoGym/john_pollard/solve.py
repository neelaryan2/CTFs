from OpenSSL.crypto import load_certificate
from OpenSSL.crypto import FILETYPE_PEM

certfile = 'cert'
with open(certfile, 'rb') as fp:
    cert = load_certificate(FILETYPE_PEM, fp.read())

n = cert.get_pubkey().to_cryptography_key().public_numbers().n
e = cert.get_pubkey().to_cryptography_key().public_numbers().e

def gcd(x, y): 
    while y : 
        x, y = y, x % y 
    return x 

def pollard_rho(n):
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x, y = f(x), f(f(y))
        d = gcd(abs(x - y), n)
    if d != n: return d

p = pollard_rho(n)
q = n // p
assert p * q == n
print(f'picoCTF{{{q},{p}}}')