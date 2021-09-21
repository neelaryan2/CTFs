from Crypto.Cipher import DES
import binascii
import itertools
import random
import string
from pwn import *
from tqdm import tqdm

host = 'mercury.picoctf.net' 
port = 3620

conn = remote(host, port)

conn.recvline()
flag = conn.recvline()[:-1].decode()
flag = binascii.unhexlify(flag)


def pad(msg):
	block_len = 8
	over = len(msg) % block_len
	pad = block_len - over
	return (msg + " " * pad).encode()

def generate_key():
	return pad("".join(random.choice(string.digits) for _ in range(6)))

candidates = []

def oracle(conn, plain):
	conn.recvuntil(b'encrypt? ')
	conn.sendline(binascii.hexlify(plain.encode()))
	cipher = conn.recvline()[:-1]
	print(cipher)
	cipher = binascii.unhexlify(cipher)

	enc, dec = {}, {}
	for i in range(1000000):
		key = pad(str(i).zfill(6))
		des = DES.new(key, DES.MODE_ECB)
		enc[des.encrypt(pad(plain))] = i
		dec[des.decrypt(cipher)] = i

	for p, k1 in enc.items():
		if p not in dec.keys():
			continue
		k2 = dec[p]
		des1 = DES.new(pad(str(k1).zfill(6)), DES.MODE_ECB)
		des2 = DES.new(pad(str(k2).zfill(6)), DES.MODE_ECB)
		enc_msg = des1.decrypt(des2.decrypt(flag))
		print(enc_msg)


while True:
	plain = "".join(random.choice(string.digits) for _ in range(6))
	oracle(conn, plain)

