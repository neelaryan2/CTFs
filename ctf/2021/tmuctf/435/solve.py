import binascii
import hashlib
import sys
from aes import AES
import string
import itertools
from tqdm import tqdm

CHARSET = string.printable

outp = b'9**********b4381646*****01********************8b9***0485******************************0**ab3a*cc5e**********18a********5383e7f**************1b3*******9f43fd66341f3ef3fab2bbfc838b9ef71867c3bcbb'
key = b'*XhN2*8d%8Slp3*v'
key_len = len(key)


def pad(message):
    padding = bytes((key_len - len(message) % key_len) * chr(key_len - len(message) % key_len), encoding='utf-8')
    return message + padding


def xor(arg1, arg2):
    assert len(arg1) == len(arg2)
    return bytes([a ^ b for a, b in zip(arg1, arg2)])


def check(actual, pred):
    pred = binascii.hexlify(pred)
    assert len(actual) == len(pred)
    for a, p in zip(actual, pred):
        if a != ord('*') and a != p:
            return False
    return True


def try_key(new_key):
    suf = hashlib.sha256(new_key).hexdigest()
    suf_hash = binascii.unhexlify(suf)[:10]

    message = b'CBC (Cipher Blocker Chaining) is an advanced form of block cipher encryption'
    message = pad(message + suf_hash)

    aes = AES(new_key)

    last_cipher = binascii.unhexlify(outp[-2 * key_len:])
    num_blocks = len(outp) // (2 * key_len)

    for i in reversed(range(num_blocks)):
        lo = key_len * i
        hi = key_len * (i + 1)
        actual = outp[2 * lo:2 * hi]
        if not check(actual, last_cipher):
            return False
        last_cipher = xor(message[lo:hi], aes.decrypt_block(last_cipher))

    print('IV:', last_cipher)
    print('Key:', new_key)
    return True


hidden_idx = [e[0] for e in enumerate(key) if e[1] == ord('*')]
total = pow(len(CHARSET), len(hidden_idx))

for hiddens in tqdm(itertools.product(CHARSET, repeat=len(hidden_idx)), total=total):
    new_key = list(key)
    for i, h in zip(hidden_idx, hiddens):
        new_key[i] = ord(h)
    new_key = bytes(new_key)

    if try_key(new_key):
        sys.exit(0)
