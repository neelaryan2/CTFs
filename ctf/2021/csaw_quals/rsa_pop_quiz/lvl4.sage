from sage.all import *
from pwn import *

N = 66806600873427771629347411652427322203467213183928467620436642517746866572639420426999662907161779727143803318137747940845308229418548986825697571084368540258022763263401053141756231197157082989355868947090459755534412071457086520750618855441753631305074936737522122461564582977664405504770234348781971637163
E = 17
d0 = 10372555798558432972245118273972376534234701888796136496411161252375003023786932993001661491540840619534876927165925432759534082359068839217326043977031329
L = 512
C = 28621049604991223848651047160274693014512476205199183462626421095885327651694045582262974636200920071738367731712611222307008924085584098208356021028278281120906585066310591315093805365094839532289613580979563429141161279750334594621646170295486673324396319329852117786811352006783015795020700567344137417268

dlow = d0

x = PolynomialRing(Zmod(N), names='x').gen()

mod = 1 << L
imod = inverse_mod(mod, N)


def solve_quadratic_mod_power2(a, b, c, e):
    roots = {0}
    for cure in range(1, e + 1):
        roots2 = set()
        curmod = 1 << cure
        for xbit in range(2):
            for r in roots:
                v = r + (xbit << (cure - 1))
                if (a * v * v + b * v + c) % curmod == 0:
                    roots2.add(v)
        roots = roots2
    return roots


for k in range(1, E):
    a = k
    b = E * dlow - k * N - k - 1
    c = k * N
    for plow in solve_quadratic_mod_power2(a, b, c, L):
        print("k", k, "plow", plow)
        roots = (x + plow * imod).small_roots(X=2**(215), beta=0.4)
        print("Roots", roots)
        if roots:
            root = int(roots[0])
            kq = root + plow * imod
            q = gcd(N, kq)
            assert 1 < q < N, "Fail"
            p = N / q
            d = inverse_mod(E, (p - 1) * (q - 1))
            msg = pow(C, d, N)
            assert pow(msg, E, N) == C
            print(msg)
            quit()