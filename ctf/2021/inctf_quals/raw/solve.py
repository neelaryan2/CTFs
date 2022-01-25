import numpy as np
import matplotlib.pyplot as plt

with open('Oliver_Tree.mp3', 'rb') as fp:
	data = fp.read()

data = np.array(list(data))
data = data.reshape(2930, 2930)

data = data[:600, 300:900]

fig = plt.figure(dpi=400)
plt.imshow(data)
plt.savefig('image.png')
plt.close()

print(data.shape)