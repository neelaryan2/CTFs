

# This file was *autogenerated* from the file lvl4.sage
from sage.all_cmdline import *   # import sage library

_sage_const_66806600873427771629347411652427322203467213183928467620436642517746866572639420426999662907161779727143803318137747940845308229418548986825697571084368540258022763263401053141756231197157082989355868947090459755534412071457086520750618855441753631305074936737522122461564582977664405504770234348781971637163 = Integer(66806600873427771629347411652427322203467213183928467620436642517746866572639420426999662907161779727143803318137747940845308229418548986825697571084368540258022763263401053141756231197157082989355868947090459755534412071457086520750618855441753631305074936737522122461564582977664405504770234348781971637163); _sage_const_17 = Integer(17); _sage_const_10372555798558432972245118273972376534234701888796136496411161252375003023786932993001661491540840619534876927165925432759534082359068839217326043977031329 = Integer(10372555798558432972245118273972376534234701888796136496411161252375003023786932993001661491540840619534876927165925432759534082359068839217326043977031329); _sage_const_512 = Integer(512); _sage_const_28621049604991223848651047160274693014512476205199183462626421095885327651694045582262974636200920071738367731712611222307008924085584098208356021028278281120906585066310591315093805365094839532289613580979563429141161279750334594621646170295486673324396319329852117786811352006783015795020700567344137417268 = Integer(28621049604991223848651047160274693014512476205199183462626421095885327651694045582262974636200920071738367731712611222307008924085584098208356021028278281120906585066310591315093805365094839532289613580979563429141161279750334594621646170295486673324396319329852117786811352006783015795020700567344137417268); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_215 = Integer(215); _sage_const_0p4 = RealNumber('0.4')
from sage.all import *
 
N = _sage_const_66806600873427771629347411652427322203467213183928467620436642517746866572639420426999662907161779727143803318137747940845308229418548986825697571084368540258022763263401053141756231197157082989355868947090459755534412071457086520750618855441753631305074936737522122461564582977664405504770234348781971637163 
E = _sage_const_17 
d0 = _sage_const_10372555798558432972245118273972376534234701888796136496411161252375003023786932993001661491540840619534876927165925432759534082359068839217326043977031329 
L = _sage_const_512 
C = _sage_const_28621049604991223848651047160274693014512476205199183462626421095885327651694045582262974636200920071738367731712611222307008924085584098208356021028278281120906585066310591315093805365094839532289613580979563429141161279750334594621646170295486673324396319329852117786811352006783015795020700567344137417268 

dlow = d0
 
x = PolynomialRing(Zmod(N), names='x').gen()
 
mod = _sage_const_1  << L
imod = inverse_mod(mod, N)
 
def solve_quadratic_mod_power2(a, b, c, e):
    roots = {_sage_const_0 }
    for cure in range(_sage_const_1 , e + _sage_const_1 ):
        roots2 = set()
        curmod = _sage_const_1  << cure
        for xbit in range(_sage_const_2 ):
            for r in roots:
                v = r + (xbit << (cure - _sage_const_1 ))
                if (a*v*v + b*v + c) % curmod == _sage_const_0 :
                    roots2.add(v)
        roots = roots2
    return roots
 
 
for k in range(_sage_const_1 , E):
    a = k
    b = E*dlow - k*N - k - _sage_const_1 
    c = k*N
    for plow in solve_quadratic_mod_power2(a, b, c, L):
        print("k", k, "plow", plow)
        roots = (x + plow * imod).small_roots(X=_sage_const_2 **(_sage_const_215 ), beta=_sage_const_0p4 )
        print("Roots", roots)
        if roots:
            root = int(roots[_sage_const_0 ])
            kq = root + plow * imod
            q = gcd(N, kq)
            assert _sage_const_1  < q < N, "Fail"
            p = N / q
            d = inverse_mod(E, (p - _sage_const_1 ) * (q - _sage_const_1 ))
            msg = pow(C, d, N)
            # convert to str
            assert pow(msg, E, N) == C
            print(msg)
            # h = hex(int(msg))[2:].rstrip("L")
            # h = "0" * (len(h) % 2) + h
            # print(h.decode("hex"))
            quit()

