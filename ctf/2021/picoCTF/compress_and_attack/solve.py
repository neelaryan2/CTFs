from pwn import *
import string
from tqdm import tqdm
import collections

domain = string.ascii_lowercase + '_}{'

host = 'mercury.picoctf.net'
port = 57393

p = remote(host, port)


def mode(l):
    c = collections.Counter(l)
    return c.most_common(1)[0][0]


def query(conn, txt):
    conn.recvuntil(b'encrypted: ')
    conn.sendline(txt.encode())
    conn.recvlines(2)
    ret = conn.recvline().decode()
    ret = int(ret.strip())
    return ret


def try_layer(sofar):
    if sofar.endswith('}'):
        print(f'Found candidate : {sofar}')
        return
    print('Current : ', sofar)
    cnts = {}
    for c in domain:
        val = sofar + c
        cur = val * 2 if len(val) > 9 else val * 5
        cnts[val] = query(p, cur)
    m = mode(cnts.values())
    for k, v in cnts.items():
        if v != m:
            try_layer(k)


try_layer('picoCTF{sheriff_you_solved_the_crime}')
