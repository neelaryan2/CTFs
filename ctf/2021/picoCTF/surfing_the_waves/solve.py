from scipy.io import wavfile
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

samplerate, data = wavfile.read('main.wav')

c = np.mean(data)
s = ''
for d in data:
	if d > 0:
		s += '1'
	else:
		s += '0'

print(len(s))

s = int(s, 2).to_bytes(len(s) // 8, byteorder='big')
print(s)

# cnt = {}
# for d in data:
# 	if d not in cnt.keys():
# 		cnt[d] = 0
# 	cnt[d] += 1
# # print(data)

# fig = plt.figure(figsize=(18, 7))
# plt.bar(range(len(cnt)), list(cnt.values()), align='center')
# plt.xticks(range(len(cnt)), list(cnt.keys()))
# plt.show()
