import random
import time
import hashlib
import sys

nums = [0.3719072557403058, 0.3702330745519661, 0.0634360689087381, 0.2952684217196877, 0.49843979869018884, 0.7895773927381043, 0.2917373566923527, 0.9030776618431813, 0.7181809628413409, 0.28050872595896736, 0.17458286936713008, 0.2767390568969583, 0.5492478684168797, 0.2641653670084557, 0.5156703392963877, 0.32839693347899057, 0.6998299885658202, 0.5811672985185747, 0.4644468325648108, 0.49982517906634727, 0.9333988943747559, 0.7513893164652713, 0.18638831058360805] 

def check(t):
    random.seed(t, version=2)
    for num in nums:
        rnd = random.random()
        if rnd != num:
            return
    rnd = random.random()
    hashs = hashlib.sha256(str(rnd).encode()).hexdigest()
    if "5bc" not in hashs:
        return
    flag = f"SNYK{{{hashs}}}"
    print('Seed found', t)
    print(flag)
    sys.exit(0)

day = 86400
cur = round(time.time()) - 107 * day

for d in range(300000000):
    for i in range(day):
        check(cur)
        cur -= 1
    print(f'{d + 1} done')

