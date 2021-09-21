import requests

url = 'http://15.206.202.26/cookie.php'

cookies = {'Piece': '1'}

for i in range(40):
	r = requests.post(url, cookies=cookies)
	cookies = r.cookies.get_dict()
	value = cookies['Our_Fav_Cookie']
	print(value)


