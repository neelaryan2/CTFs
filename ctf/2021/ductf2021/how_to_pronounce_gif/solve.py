import imageio
import numpy as np
from qrtools import qrtools

def read_image(num):
	filename = f'split/frame_{num:>03}_delay-0.05s.png'
	im = imageio.imread(filename)
	return im

# for j in range(10):
# 	img = np.concatenate(tuple(read_image(i) for i in range(j, 120, 10)), axis=0)
# 	file = f'out{j:>02}.png'
# 	imageio.imwrite(file, img)
	
for j in range(10):
	file = f'out{j:>02}.png'
	qr = qrtools.QR()
	qr.decode(file)
	print(qr.data)
