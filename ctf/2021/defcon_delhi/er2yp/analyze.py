import subprocess

with open('dc_9111.pyc', 'rb') as fp:
    pyc = fp.read()


def pad(s, l):
    s = s[:l].encode()
    return s + (l - len(s)) * b'\x00'


def run(flag, key):
    flag = pad(flag, 28)
    key = pad(key, 7)
    cur = list(pyc)
    for i, b in enumerate(flag):
        cur[i + 162] = b
    for i, b in enumerate(key):
        cur[i + 198] = b
    cur = bytes(cur)
    with open('tmp.pyc', 'wb') as fp:
        fp.write(cur)
    out = subprocess.check_output(['python3.9', 'tmp.pyc'])
    nums = list(map(int, out.decode().strip().split('\n')))
    return nums


for k1 in range(128):
    flag = '\x00' * 27 + chr(k1)
    for k2 in range(128):
        nums = run(flag, chr(k2))
        assert 10 + (k1 ^ k2) == nums[0]
