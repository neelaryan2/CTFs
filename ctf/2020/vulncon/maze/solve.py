from pyzbar.pyzbar import decode
from PIL import Image

data = []

for i in range(28):
	img_path = f'./images/image-{i}.png'
	img = Image.open(img_path)
	d = decode(img)[0]
	data.append(d.data.decode())
	print(i, ':', data[-1])
