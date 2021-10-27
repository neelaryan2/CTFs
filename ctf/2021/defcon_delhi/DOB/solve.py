months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

fp = open('wordlist.txt', 'w')

for day in range(1, 32):
	for year in range(2000, 2021):
		for month in months:
			passw = f'{month}-{day:>02}-{year}'
			print(passw, file=fp)
			passw = f'{month.lower()}-{day:>02}-{year}'
			print(passw, file=fp)
			passw = f'{month}-{day}-{year}'
			print(passw, file=fp)
			passw = f'{month.lower()}-{day}-{year}'
			print(passw, file=fp)


fp.close()