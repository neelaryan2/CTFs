cityset = set()
edges = []

with open('file.txt', 'r') as fp:
    for l in fp:
        l = l.strip()
        if not l: continue
        cities, timenergy = l.split('=')
        a, b = cities.split('-')
        time, energy = map(int, timenergy.split(','))
        if a == b: continue
        cityset.add(a)
        cityset.add(b)
        edges.append((a, b, time, energy))

cities = sorted(list(cityset))
idx = {v: i for i, v in enumerate(cities)}
n = len(cities)
G = [[] for _ in range(n)]

for a, b, time, energy in edges:
    a, b = idx[a], idx[b]
    G[a].append((b, time, energy))

for i in range(n):
    G[i] = sorted(G[i], key=lambda x: (x[1], x[2]))

care = idx['Diagon Alley']
min_so_far = 10000000000000000000


def hamiltonians(time=0, energy=0, vis=[]):
    global min_so_far

    if not vis:
        for v in range(len(G)):
            for p in hamiltonians(vis=[v]):
                yield p

    elif len(vis) == n:
        for u, t, e in G[vis[-1]]:
            t_ = time + t
            e_ = energy + e
            if u == vis[0] and e_ <= 58000 and t_ <= min_so_far:
                yyy = ''.join([cities[i][:2] for i in vis + [u]])
                print(f'{t_}-{yyy}-{e_}')
                min_so_far = t_
        yield (time, energy, vis)

    else:
        assert 0 < len(vis) < n
        done = set(vis)
        for u, t, e in G[vis[-1]]:
            t_ = time + t
            e_ = energy + e
            if u in done or e_ > 58000 or t_ > min_so_far:
                continue
            if u == care and (t_ <= 135 or t_ > 135 + 515):
                continue
            for p in hamiltonians(t_, e_, vis + [u]):
                yield p


ans = list(hamiltonians())
# print(ans)
