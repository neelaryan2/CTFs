import time
from Crypto.Cipher import AES
import sys

c = [0xa8, 0x37, 0xf4, 0xc7, 0x52, 0x3c, 0x28, 0x11, 0x69, 0x76, 0xec, 0x98, 0xd, 0x12, 0x92, 0xda, 0xc8, 0x48, 0xbc, 0x2, 0xfa, 0xfa, 0xd2, 0x7b, 0x9c, 0x47, 0xdb, 0x82, 0x69, 0xcf, 0xb0, 0x8f]
iv = list(range(1, 17))

c = bytes(c)
iv = bytes(iv)

def check(t):
    key = str(t).encode().ljust(16, b'\x00')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    m = cipher.decrypt(c)
    if m.startswith(b'DO{'):
        print(m)
        sys.exit(0)
    return False

offset = int(sys.argv[1]) if len(sys.argv) > 1 else 200
day = 86400
current = round(time.time())
current -= offset * day

for d in range(100):
    for i in range(day):
        check(current)
        current -= 1
    print('done', offset + d)

