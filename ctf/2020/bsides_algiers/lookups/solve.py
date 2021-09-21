import struct

def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

s = ['35', '6f', '85', '4a', 'ca', '10', '8d', '4a', '69', '13', '8f', '4a', '82', 'ef', '9c', '4a', 'dc', 'f2', '9a', '4a', 'fa', 'ad', '81', '4a', '0a', '6e', '45', '4a', 'e9', '34', '70', '4a', '39', '0e', '5c', '49', 'ae', '05', '8f', '4a', '81', '83', 'ad', '49', '52', '37', '69', '4a', '56', '21', '69', '4a', '1d', '4b', '70', '4a', 'a2', 'e3', '86', '4a', '5a', 'f0', '98', '4a', '77', 'eb', '9c', '4a', '37', '56', '70', '4a', '05', '0f', '69', '4a', 'f3', '68', '7f', '4a', 'c7', '88', '94', '4a', 'd7', '59', '7f', '4a', '77', 'eb', '9c', '4a', '21', 'a3', 'ad', '49', 'b1', '2f', '8b', '4a', '5c', 'b1', 'ae', '44']

flag = ''
for i in range(len(s)//4):
    cur = ''.join(reversed(s[4*i:4*i+4]))
    binary = format(int(cur, 16), '032b')
    f = bin_to_float(binary)
    cur = round(pow(f, 2/3))
    cur = hex(cur)[2:]
    cur = bytearray.fromhex(cur).decode()
    flag += cur[::-1]

print(flag)
