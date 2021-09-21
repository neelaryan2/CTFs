from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
import string
from typing import Tuple, Iterator, Iterable, Optional


def isqrt(n: int) -> int:
    # ref: https://en.wikipedia.org/wiki/Integer_square_root
    if n == 0:
        return 0

    # ref: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Rough_estimation
    x = 2**((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def is_perfect_square(n: int) -> bool:
    # ref: https://hnw.hatenablog.com/entry/20140503
    sq_mod256 = (1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
    if sq_mod256[n & 0xff] == 0:
        return False

    mt = ((9, (1, 1, 0, 0, 1, 0, 0, 1, 0)), (5, (1, 1, 0, 0, 1)), (7, (1, 1, 1, 0, 1, 0, 0)), (13, (1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1)), (17, (1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1)))
    a = n % (9 * 5 * 7 * 13 * 17)
    if any(t[a % m] == 0 for m, t in mt):
        return False

    return isqrt(n)**2 == n


def rational_to_contfrac(x: int, y: int) -> Iterator[int]:
    # ref: https://en.wikipedia.org/wiki/Euclidean_algorithm#Continued_fractions
    while y:
        a = x // y
        yield a
        x, y = y, x - a * y


def contfrac_to_rational_iter(contfrac: Iterable[int]) -> Iterator[Tuple[int, int]]:
    # ref: https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf (6)
    n0, d0 = 0, 1
    n1, d1 = 1, 0
    for q in contfrac:
        n = q * n1 + n0
        d = q * d1 + d0
        yield n, d
        n0, d0 = n1, d1
        n1, d1 = n, d


def convergents_from_contfrac(contfrac: Iterable[int]) -> Iterator[Tuple[int, int]]:
    # ref: https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf Section.3
    n_, d_ = 1, 0
    for i, (n, d) in enumerate(contfrac_to_rational_iter(contfrac)):
        if i % 2 == 0:
            yield n + n_, d + d_
        else:
            yield n, d
        n_, d_ = n, d


def wiener_attack(e: int, n: int) -> Optional[int]:
    # ref: https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf Section.4
    f_ = rational_to_contfrac(e, n)
    for k, dg in convergents_from_contfrac(f_):
        edg = e * dg
        phi = edg // k

        x = n - phi + 1
        if x % 2 == 0 and is_perfect_square((x // 2)**2 - n):
            g = edg - phi * k
            return dg // g
    return None


def lsb_attack(n, e, c, oracle):
    lo, hi, i = 0, n, 1
    while lo < hi - 1:
        query = (c * pow(2, i * e, n)) % n
        r = oracle(query)
        mid = 1 + (lo + hi - 1) // 2
        if r == 1:
            lo = mid
        elif r == 0:
            hi = mid
        else:
            raise Exception('BAD')
        i += 1
        print(abs(lo - hi))
    ans = long_to_bytes(lo)[:-1]
    for s in string.printable:
        cur_ans = ans + s.encode()
        cur = bytes_to_long(cur_ans)
        if c == pow(cur, e, n):
            return cur_ans.decode()
    return None


def floorSqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e
    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

def halfdPartialKeyRecoveryAttack(n, e, d0):
    d0BitSize = d0.bit_length()
    nBitSize = n.bit_length()
    if (d0BitSize < nBitSize // 2):
        raise Exception("Not enough bits of d0")
    test = pow(3, e, n)
    test2 = pow(5, e, n)
    for k in range(1, e):
        d = ((k * n + 1) // e)
        d >>= d0BitSize
        d <<= d0BitSize
        d |= d0
        # if (e * d) % k != 1:
        #     continue
        if pow(test, d, n) != 3 or pow(test2, d, n) != 5:
            continue
        totientN = (e * d - 1) // k
        b = totientN - n - 1
        discriminant = b * b - 4 * n
        root = floorSqrt(discriminant)
        if (root * root != discriminant):
            continue
        p = (-b + root) // 2
        q = n // p
        assert p * q == n
        print(p, q)
        return
    return None


if __name__ == '__main__':
    n = 66806600873427771629347411652427322203467213183928467620436642517746866572639420426999662907161779727143803318137747940845308229418548986825697571084368540258022763263401053141756231197157082989355868947090459755534412071457086520750618855441753631305074936737522122461564582977664405504770234348781971637163
    d0 = 10372555798558432972245118273972376534234701888796136496411161252375003023786932993001661491540840619534876927165925432759534082359068839217326043977031329
    e = 17
    c = 28621049604991223848651047160274693014512476205199183462626421095885327651694045582262974636200920071738367731712611222307008924085584098208356021028278281120906585066310591315093805365094839532289613580979563429141161279750334594621646170295486673324396319329852117786811352006783015795020700567344137417268

    halfdPartialKeyRecoveryAttack(n, e, d0)
    # p_ = getPrime(512)
    # q_ = getPrime(512)

    # n_ = p_ * q_
    # e_ = 65537
    # d_ = pow(e_, -1, (p_ - 1) * (q_ - 1))

    # m_ = bytes_to_long(b'this_is_a_fake_flag_fuck_this')
    # c_ = pow(m_, e_, n_)

    # def oracle_(query):
    #     t = pow(query, d_, n_)
    #     return t & 1

    # print(lsb_attack(n_, e_, c_, oracle_))