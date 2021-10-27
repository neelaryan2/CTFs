import base64, zlib, json


def decode_cookie(s):
    s = s.replace('-', '+').replace('_', '/').split('.')
    assert s.pop(0) == ''
    chunks = []
    for t in s:
        decoded_chunk = None
        for r in range(3):
            try:
                decoded_chunk = base64.b64decode(t + r * '=')
            except:
                pass
        assert decoded_chunk is not None
        chunks.append(decoded_chunk)

    base64_decoded = b''.join(chunks)
    chunks[0] = zlib.decompress(chunks[0])

    jwt = b'.'.join([base64.urlsafe_b64encode(t).replace(b'=', b'') for t in chunks])
    print(jwt.decode())

    # chunks[0]
    return chunks[0]


def encode_cookie(d):
	d = json.dumps(d).replace(' ', '')
	d = zlib.compress(d.encode())
	d = base64.urlsafe_b64encode(d).decode()
	return d


with open('test_cookies.txt', 'r') as fp:
    lines = [l.strip() for l in fp if l.strip()]


for i in range(0, len(lines), 2):
    userpass, cookie = lines[i:i + 2]
    user, passwd = userpass.split(',')
    cookie = decode_cookie(cookie)
    cookie = json.loads(cookie)
    encode_cookie(cookie)
    # print(cookie['_id'])

