import imageio
import numpy as np
from matplotlib import pyplot as plt

im1 = imageio.imread('scrambled1.png')
im2 = imageio.imread('scrambled2.png')

plt.imshow(im1 + im2)
plt.show()
# print(im1.shape)
# print(im2.shape)