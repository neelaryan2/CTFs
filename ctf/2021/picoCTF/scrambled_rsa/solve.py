from pwn import *
import string

domain = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_}{'

host = 'mercury.picoctf.net'
port = 50075

p = remote(host, port)


def get(w):
    p.recvuntil(w.encode())
    return p.recvline().strip().decode()


def query(q):
    p.sendline(q.encode())
    return get('go: ')


flag = get('flag: ')

mem = {}
pref = ''
idx = 0
found = True

while found:
    found = False
    print('Iteration :', idx, end=' ')
    for c in domain:
        cur = query(pref + c)
        for k, v in mem.items():
            assert v in cur
            cur = cur.replace(v, '')
        if cur in flag:
            pref += c
            mem[(idx, c)] = cur
            idx += 1
            found = True
            flag = flag.replace(cur, '')
            print('FOUND :', c, 'SOFAR :', pref)
            break

print('FINAL :', pref)
