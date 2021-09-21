import imageio
import numpy as np
from matplotlib import pyplot as plt

im1 = imageio.imread('evil_duck_extra.png')
im2 = imageio.imread('evil_duck.png')
im3 = imageio.imread('duck.png')

print(im2[:,:,0] - im3[:,:,0])

plt.imshow(im2 ^ im3)
plt.show()
# cur = im1[:,:,0]
# for i, r in enumerate(cur):
# 	if (r == cur[0]).all():
# 		print(i)
# for i in range(cur.shape[1]):
# 	if (cur[:,i]==cur[:,0]).all():
# 		print(i)

# print(im1[:109,0,0])
# plt.imshow(im1[:109, :109, 0])
# plt.show()
