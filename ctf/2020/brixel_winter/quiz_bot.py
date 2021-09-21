import requests
import os, sys
from bs4 import BeautifulSoup
from tqdm import tqdm

# brixelCTF{kn0wl3dg3}
url = 'http://timesink.be/quizbot/index.php'
cache_file = 'saved_ques.txt'
sep = ' @@@ '

cache = {}
try:
	with open(cache_file, 'r') as fp:
		lines = fp.readlines()
	for line in lines:
		ques, ans = line.strip().split(sep)
		cache[ques] = ans
except Exception as e:
	print(e)

def collect_data():
	session = requests.Session()

	r = session.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	prev_ques = soup.find_all("h4")[0].contents[0]

	max_iter = int(sys.argv[1])
	already_there = 0

	try:
		for i in tqdm(range(max_iter)):
			payload = {'insert_answer' : 'this cant be right'}
			r = session.post(url, data=payload)
			soup = BeautifulSoup(r.text, 'lxml')
			ques = soup.find_all("h4")[0].contents[0]
			prev_ans = soup.find("div", {"id": "answer"}).contents[0]
			cache[prev_ques] = prev_ans
			prev_ques = ques
			if prev_ques in cache.keys():
				already_there += 1
	except Exception as e:
		print(e)
	finally:
		print(f'{already_there}/{i+1} answers were already present!')
		with open(cache_file, 'w+') as fp:
			for ques, ans in cache.items():
				line = ques + sep + ans + '\n'
				fp.write(line)


def solve():
	session = requests.Session()

	r = session.get(url)
	max_iter = int(sys.argv[1])
	fucked = False

	try:
		for i in tqdm(range(max_iter)):
			soup = BeautifulSoup(r.text, 'lxml')
			ques = soup.find_all("h4")[0].contents[0]
			if ques not in cache.keys():
				payload = {'insert_answer' : 'this cant be right'}
				r = session.post(url, data=payload)
				soup = BeautifulSoup(r.text, 'lxml')
				cache[ques] = soup.find("div", {"id": "answer"}).contents[0]
				fucked = True
				break
			payload = {'insert_answer' : cache[ques]}
			r = session.post(url, data=payload)
		print(r.text)
	except Exception as e:
		print(e)
	finally:
		if fucked:
			with open(cache_file, 'w+') as fp:
				for ques, ans in cache.items():
					line = ques + sep + ans + '\n'
					fp.write(line)

solve()