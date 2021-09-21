target = 'jbgkfmgkknbiblpmibgkcneiedgokibmekffokamknbkhgnlhnajeefpekiefmjgeogjbflijnekebeokpgngjnfbimlkdjdjhan'
encodedFlag =  bytes.fromhex(open('flag.txt').read())

encoded = [ord(x) - 97 for x in target]
#             0  1  2  3  4   5   6   7   8   9   a   b   c   d   e   f
jumble_arr = [0, 2, 4, 6, 8, 10, 12, 14, 17, 19, 21, 23, 25, 27, 29, 31]

res = [0] * 100
res[0] = 9

for i in range(1,100,1):
    res[i] =  (encoded[i] - encoded[i-1]) & 0xf
    if res[i-1] < 16 and res[i-1] % 2 == 1:
         res[i-1] +=16
       
res[99] += 16

encoded = bytes.fromhex(''.join([hex(jumble_arr.index(i))[2:] for i in res]))
flag  = ''.join([chr(a ^ b) for a,b in zip(encoded,encodedFlag)])
print(flag)