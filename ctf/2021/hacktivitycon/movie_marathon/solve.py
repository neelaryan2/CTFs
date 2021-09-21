import imdb
from pwn import *
import sys
import os
import pickle
from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
tmdb.api_key = '5bc3328a7a238937d85564b1832706d5'
movie = Movie()

cache = {}

def load_cache():
    global cache
    if os.path.isfile('cache.pkl'):
        with open('cache.pkl', 'rb') as fp:
            cache = pickle.load(fp)
        print('Loaded from cache:', len(cache), 'keys')


def save_cache():
    global cache
    with open('cache.pkl', 'wb') as fp:
        pickle.dump(cache, fp, pickle.HIGHEST_PROTOCOL)


def get_actors(movie_name, date, k=5):
    if movie_name in cache:
        return cache[movie_name]
    search = movie.search(movie_name)
    for res in search:
        date_set = set()
        date_results = movie.release_dates(res.id)['results']
        for date_result in date_results:
            for d in date_result['release_dates']:
                date_set.add(d['release_date'][:10])
        if date not in date_set:
            continue
        creds = movie.credits(res.id)
        actors = []
        for crew in creds['cast']:
            if crew['known_for_department'] == 'Acting':
                actors.append(crew['name'])
                if len(actors) == k:
                    actors = '; '.join(actors)
                    cache[movie_name] = actors
                    return actors
        break
    save_cache()
    sys.exit(0)


host = 'challenge.ctf.games'
port = 31260

load_cache()
p = remote(host, port)
p.recvlines(10)

counter = 1

try:
    for i in range(30):
        p.recvline()
        print(f'{counter: <3}', end=' ')
        counter += 1
        l = p.recvline().decode().strip()
        print(l)
        
        prompt = l[2:].split(' ')
        movie_name = ' '.join(prompt[:-1])
        date = prompt[-1][1:-1]
        actors = get_actors(movie_name, date)
        print(actors)
        p.recvuntil(b'* ')
        p.sendline(actors.encode())
    print(p.recvall())
    while True:
        print(p.recvline())
except Exception as e:
    save_cache()
    p.close()
    sys.exit(1)


save_cache()
p.close()


