import requests

url = 'http://147.182.172.217:42100/'

# Latest version: 133791021
# flag{h0w_l0ng_wher3_y0u_g0ne_f0r_3910512832}

def check(v):
	print(v, end=': ')
	r = requests.head(url + 'v' + str(v))
	is_ok = not r.headers['Content-Type'].startswith('text/html')
	print(is_ok) 
	return is_ok
	
lo = 1
hi = 1
while check(hi):
	lo = hi
	hi *= 2

while lo < hi - 1:
	mid = (lo + hi) // 2
	if check(mid):
		lo = mid
	else:
		hi = mid

print('Latest version:', lo)
