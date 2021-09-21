# /usr/bin/env python3
import pickle
import sys
import pickletools
import inspect
import dis
import pdb

# Check version >= 3.9
if sys.version_info[0] != 3 or sys.version_info[1] < 9:
    print("Check your Python version!")
    exit(0)

# This function is truly amazing, so do not fix it!
def amazing_function(a, b, c=None):
    if type(b) == int:
        return a[b]
    else:
        return (
            f"CORRECT! The flag is: ACSC{{{c.decode('ascii')}}}" if a == b else "WRONG!"
        )


with open("rick.pickle", "rb") as f:
    pickle_rick = f.read()

rick_says = b"Wubba lubba dub-dub!!"  # What is the right input here?
assert type(rick_says) == bytes and len(rick_says) == 21
# pickle.loads(pickle_rick)

func_class = type(amazing_function)
code_class = type(getattr(amazing_function, '__code__'))

k0 = [115, 99, 97, 162, 81, 225, 215, 72, 111, 229, 64, 155, 212, 66, 95, 200, 177, 45, 206, 18, 140, 47, 122, 19, 186, 123, 91, 94, 26, 104, 119, 88, 44, 82, 58, 139, 193, 101, 209, 213, 65, 16, 164, 124, 150, 149, 132, 1, 79, 236, 131, 196, 113, 194, 185, 4, 107, 36, 181, 218, 120, 40, 142, 11, 183, 129, 51, 125, 6, 222, 13, 161, 141, 109, 100, 175, 153, 252, 117, 127, 54, 156, 62, 167, 160, 198, 152, 211, 178, 21, 73, 214, 253, 135, 105, 190, 85, 12, 243, 34, 137, 233, 128, 228, 151, 8, 247, 92, 60, 174, 138, 114, 130, 169, 15, 103, 230, 106, 158, 57, 76, 5, 84, 210, 32, 39, 165, 87, 184, 237, 28, 207, 75, 172, 176, 231, 37, 195, 232, 182, 25, 201, 188, 61, 163, 251, 227, 2, 46, 35, 71, 250, 246, 38, 136, 255, 199, 29, 20, 242, 238, 126, 17, 179, 148, 220, 240, 86, 59, 145, 80, 189, 224, 170, 24, 143, 0, 10, 166, 77, 41, 203, 31, 90, 239, 191, 197, 112, 159, 118, 157, 244, 226, 216, 43, 49, 70, 93, 50, 78, 7, 208, 96, 202, 89, 108, 168, 235, 3, 254, 146, 55, 9, 180, 241, 121, 98, 110, 68, 83, 63, 42, 69, 52, 30, 221, 27, 248, 33, 147, 205, 14, 56, 116, 173, 192, 53, 74, 234, 223, 154, 67, 187, 217, 23, 134, 171, 102, 22, 204, 249, 245, 219, 144, 48, 133]

k1 = code_class(2, 0, 0, 5, 6, 67, b'd\x01}\x02zB|\x00\\\x02}\x03}\x04|\x01d\x02\x16\x00|\x02k\x02r0|\x04}\x00|\x01d\x02\x1c\x00}\x01d\x03|\x02\x18\x00}\x02n\x14|\x03}\x00|\x01d\x02\x1c\x00}\x01d\x03|\x02\x18\x00}\x02W\x00q\x04\x01\x00\x01\x00\x01\x00|\x00d\x01\x19\x00\x06\x00Y\x00S\x000\x00q\x04d\x00S\x00', (None, 0, 2, 1), (), ('a', 'b', 'c', 'a0', 'a1'), 'something_suspicious.py', 'search', 45, b'\x00\x01\x04\x02\x02\x01\x08\x01\x0c\x01\x04\x01\x08\x01\n\x02\x04\x01\x08\x01\x0c\x01\x06\x01', (), ())
k1 = func_class(k1, {})
print(dis.dis(k1))

print('=' * 90)

k2 = code_class(1, 0, 0, 6, 5, 67, b'|\x00\xa0\x00\xa1\x00}\x01g\x00}\x02d\x01}\x03|\x03|\x01k\x00rvd\x02\\\x02}\x04}\x05|\x05|\x01k\x00rN|\x04|\x05d\x03\x17\x00|\x00|\x03|\x05\x17\x00|\x01\x16\x00\x19\x00\x14\x007\x00}\x04|\x05d\x037\x00}\x05q |\x04d\x04;\x00}\x04|\x04d\x05k\x00sbJ\x00\x82\x01|\x02\xa0\x01|\x04\xa1\x01\x01\x00|\x03d\x037\x00}\x03q\x10|\x02S\x00', (None, 0, (0, 0), 1, 257, 256), ('__len__', 'append'), ('a', 'ln', 'arr', 'i', 's', 'j'), 'something_suspicious.py', 'mix', 61, b'\x00\x01\x08\x01\x04\x01\x04\x01\x08\x01\x08\x01\x08\x01\x1c\x01\n\x01\x08\x01\x0c\x01\n\x01\n\x01', (), ())
k2 = func_class(k2, {})
# print(dis.dis(k2))
k2 = k2(rick_says)


l2 = [53, 158, 33, 115, 5, 17, 103, 3, 67, 240, 39, 27, 19, 68, 81, 107, 245, 82, 130, 159, 227]
l1 = [k1(k0, amazing_function(k2, i)) for i in range(21)]

# print(amazing_function(l1, l2, rick_says))


# k0 = [10, 1, 2]
for i in range(256):
    print(k1(k0, i))

# c = 0

# try:
#     a0, a1 = a
#     if b % 2 == c:
#         a = a1
#         b //= 2
#         c = 1 - c
#     else:
#         a = a0
#         b //= 2
#         c = 1 - c
# except:
#     pass

# # a[0]


def my_k2(a):
    ln = len(a)
    arr = []
    for i in range(ln):
        s, j = 0, 0
        for j in range(ln):
            s += (j + 1) * a[(i + j) % ln]
        s %= 257
        if s < 256:
            arr.append(s)
        else:
            assert False
    return arr

# print(my_k2(rick_says))