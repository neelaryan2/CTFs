import string
import itertools
from tqdm import tqdm

domain = set([ord(c) for c in 'abcdef0123456789'])
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

c = 'eljodmjdjcnfcdmgbleojbgngojkkdpimebgeigpdkjpmgngpfpgelemjoglghjd'
c = [ALPHABET.index(ch) for ch in c]

candidates = None


def possibles():
    global candidates
    n, alph = len(c), len(ALPHABET)
    candidates = [[] for i in range(n // 2)]
    for i in range(0, n, 2):
        for k1 in range(alph):
            for k2 in range(alph):
                a1 = (c[i] - k1 + alph) % alph
                a1 = a1 * 16 + (c[i + 1] - k2 + alph) % alph
                if a1 in domain:
                    candidates[i // 2].append((k1, k2))


def decrypt(key):
    ptr, n = 0, len(c)
    alph = len(ALPHABET)
    for i in range(n):
        c[i] = (c[i] - key[ptr] + alph) % alph
        ptr = (ptr + 1) % len(key)
    plain = ''
    for i in range(0, n, 2):
        cur = c[i] * alph + c[i + 1]
        if cur not in domain:
            return
        plain += chr(cur)
    print(plain)


possibles()

for l in range(1, 15):
    tmp = []
    for cand in candidates:
        tmp.append(set([cc[0] for cc in cand]))
        tmp.append(set([cc[1] for cc in cand]))

    for i in range(l):
        cur = set(tmp[i])
        for j in range(i + l, len(c), l):
            cur = cur.intersection(tmp[j])
        tmp[i] = list(cur)

    for key in itertools.product(*tmp[:l]):
        decrypt(key)
