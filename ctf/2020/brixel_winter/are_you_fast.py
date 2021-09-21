import requests
from bs4 import BeautifulSoup

# brixelCTF{sp33d_d3m0n}
url = 'http://timesink.be/speedy/index.php'
headers = {'User-Agent': 'Mozilla/5.0'}

session = requests.Session()
r = session.get(url)

soup = BeautifulSoup(r.text)
var = soup.find("div", {"id": "rndstring"})
var = var.contents[0]
payload = {'inputfield': var}

r = session.post(url, headers=headers, data=payload)
soup = BeautifulSoup(r.text)
var = soup.find_all("div")[-1].find("b")
var = var.contents[0]
print(var)
