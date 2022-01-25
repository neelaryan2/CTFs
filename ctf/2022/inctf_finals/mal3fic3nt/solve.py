# from scapy.all import *
# import sys

# # scapy_cap = rdpcap('mal3fic3nt.pcap')
# scapy_cap = PcapReader('mal3fic3nt.pcap')

# friend = '172.16.120.5'
# bits = ''

# for p in scapy_cap:
#     if IP in p and p[IP].src == friend:
#         bit = int(p[IP].flags != 0)
#         bits += str(bit)

# with open('data.txt', 'w') as fp:
#     fp.write(bits)

import numpy as np
import matplotlib.pyplot as plt

with open('data.txt', 'r') as fp:
    data = fp.read()

data = np.array([255 if ch == '1' else 0 for ch in data])
data = data.reshape(200, 200)

fig = plt.figure(dpi=400)
plt.imshow(data)
plt.savefig('image.png')
plt.close()
