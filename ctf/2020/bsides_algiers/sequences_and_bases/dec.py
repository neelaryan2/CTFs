import string

flag = 'shellmates{'

def base(n, b):
    if n == 0: return '0'
    ret = ''
    while n != 0:
        ret += str(n % b)
        n //= b
    return ret[::-1]

def mymax(s):
    mx = -1
    for c in s:
        mx = max(mx, int(c))
    return mx

def check(p, q):
    s = ''
    for i in range(len(q)):
        s += '0' * int(p[i])
        s += '1' * int(q[i])
    if len(p) != len(q):
        s += '0' * int(p[-1])

    if len(s) % 8 : return False
    f = ''
    for i in range(len(s)//8):
        cur = s[8*i:8*(i+1)]
        ch = chr(int(cur,2))
        if ch not in string.printable:
            return False
        f += ch
    print(f)
    return True
    
if __name__ == "__main__":
    binaryflag=Str2Bin(flag)

    s0,s1= CountSequences(binaryflag)

    s0 = ''.join([str(c) for c in s0])[:-1]
    s1 = ''.join([str(c) for c in s1])[:-1]

    fac = [2, 2, 2, 3, 157, 179, 4339, 1112581, 53693611291973, 94333140093961, 349904234337911801671, 979906911043329098468466567737]
    n = 5654655333396589573009251270272824452868045532409847035578809519921971758405056586087615745288

    for mask in range(1 << len(fac)):
        p, q = 1, 1
        for i in range(len(fac)):
            if (mask >> i) & 1:
                p *= fac[i]
            else:
                q *= fac[i]

        for b1 in range(5, 9):
            p1 = base(p, b1)
            if mymax(p1) != b1-1 or (not p1.startswith(s0)): 
                continue
            for b2 in range(5, 9):
                q1 = base(q, b2)
                if mymax(q1) != b2-1 or (not q1.startswith(s1)): 
                    continue
                if len(p1) - len(q1) in [0, 1]:
                    check(p1, q1)
