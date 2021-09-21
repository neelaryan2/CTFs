import socket
import base64
from tqdm import tqdm
from time import sleep

host = 'chall.bsidesalgiers.com'
port = 5002
charset = """_abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ}{,!"#$%&'()*+-./:;<=>?@[\\]^`|~"""

p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p.connect((host, port))

p.recv(4096)

def query(s):
    p.send(s + b'\n')
    sleep(1)
    a = p.recv(4096)
    a = a[:-4].split(b':')[1].strip()
    a = base64.b64decode(a)
    return a

def get_next(mssg_so_far, oracle, block=32):
    l = len(mssg_so_far)
    extra = (block - 1 - l % block) % block
    payload = b'A' * extra
    cur_len = l + extra + 1
    q = oracle(payload)[:cur_len]
    for c in tqdm(charset):W
        ch = c.encode()
        qn = oracle(payload + mssg_so_far + ch)
        if q == qn[:cur_len]:
            return ch

mssg = b'shellmates{I_though_AES_w4s_m1l1tary_gr4de_encryp7ion_1n_al1_m0des}'
print('Message so far :', mssg)

while not mssg.endswith(b'}'):
    mssg += get_next(mssg, query, block=32)
    print('Message so far :', mssg)
