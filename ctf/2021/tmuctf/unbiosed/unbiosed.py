# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.5 (default, Jan 27 2021, 15:41:15)
# [GCC 9.3.0]
# Embedded file name: Unbiosed.py

# TMUCTF{M4y_4ll_Y0ur_D3c1510n5_b3_Unb1053d!}
import numpy as np, random
a = np.empty([10, 10])
b = np.empty([10, 10])
c = np.dot(a, b)
if random.uniform(0, 5) <= 2:
    print('The Bios is Corrupted!')
    exit()
d = input('Please Enter the Recovery Key:')
e = list(d)
g = 0
h = [84, 77, 85, 67, 84, 70, 123, 77, 52, 121, 95, 52, 108, 108, 95, 89, 48, 117, 114, 95, 68, 51, 99, 49, 53, 49, 48, 110, 53, 95, 98, 51, 95, 85, 110, 98, 49, 48, 53, 51, 100, 33, 125]
for f in range(len(h)):
    if ord(e[f]) != h[f]:
        g = g + 1

if g > 0:
    print('Your Bios Data Cannot be Recovered with This Key.')
    exit()
print("Congratulations! You Have The Flag, But I'll Print it Out Again For You:")
print(d)
# okay decompiling file.pyc
