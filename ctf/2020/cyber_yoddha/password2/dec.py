import random

password = "CYCTF{ju$@rcs_3l771l_@_t}bd3cfdr0y_u0t__03_0l3m"

flag = ['b']*47

for i in range(0,9):
    flag[i] = password[i]

for i in range(9,24):
    flag[32-i] = password[i]

for i in range(24,47,2):
    flag[70-i] = password[i]

for i in range(45,25,-2):
    flag[i] = password[i]

print(''.join(flag))
