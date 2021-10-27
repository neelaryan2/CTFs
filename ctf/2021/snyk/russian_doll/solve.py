import os
import xxtea
import binascii
import base64
import itertools
import string

def pad(m):
    return m + chr(16 - len(m) % 16) * (16 - len(m) % 16)

# The flag is SDZcVdXvZHhKkxopTPYbTvmxTHwFZyyvnutAwsjijXwDqeOg XXTEA encrypted. Password hint: xxxx.

enc = b'SDZcVdXvZHhKkxopTPYbTvmxTHwFZyyvnutAwsjijXwDqeOg'
enc = base64.b64decode(enc)

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_}{'
# charset = string.printable

for c in itertools.product(charset, repeat=4):
    try:
        k = ''.join(c)
        key = k.encode().rjust(16, b'\x00')
        dec = xxtea.decrypt(enc, key)
        print(k, '=>', dec.decode('ascii'))
    except Exception as e:
        pass
