import imageio, os
import numpy as np
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

for i in range(50, -1, -1):
	img_path = 'password.png'
	zip_path = f'UnzipME{i}.zip'

	im = np.array(imageio.imread(img_path))

	with open('shift_keys', 'r') as fp:
		shifts = np.array([int(line.strip()) for line in fp.readlines()])

	im_new = np.zeros_like(im)

	assert im.shape[0] == shifts.shape[0]

	for i in range(im.shape[0]):
		im_new[i] = np.roll(im[i], -shifts[i], axis=0)

	txt = pytesseract.image_to_string(im_new).strip()
	cmd = f'unzip -o -P {txt} {zip_path}'
	
	print(zip_path, 'Password :', txt)
	print('Command :', cmd)

	os.system(cmd)
	os.system(f'rm {zip_path}')
