from scapy.all import *
import hashlib
import sys

# scapy_cap = rdpcap('hash-browns.pcap')
scapy_cap = PcapReader('hash-browns.pcap')

client = '127.0.1.1'
server = '127.0.0.1'

cache = {}
for i in range(256):
    h = hashlib.md5(str(i).encode()).hexdigest()
    cache[h.encode()] = i

fp = open('data.txt', 'w')
file = open('answer.png', 'wb')
lines = []

for p in scapy_cap:
    if 'P' in p[TCP].flags:
        assert p[IP].src == client
        data = bytes(p[TCP].payload)
        if data.startswith(b'Byte Matched='):
            byt = int(data[13:].decode())
            lines.append([byt])
        else:
            hs = [d for d in data.split() if d.startswith(b'hash=')]
            hs = [cache[h[5:37]] for h in hs]
            assert data.startswith(b'ERROR!')
            assert len(hs) == 2
            lines.append(hs)

        l = lines[-1]
        if len(l) == 1:
            fp.write(f'matched={l[0]}\n')
            file.write(bytes(l))
        else:
            fp.write(f'received={l[0]}, original={l[1]}\n')
            file.write(bytes(l[1:]))

file.close()
fp.close()