#!/usr/bin/env python3

import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import binascii
from random import choice
import sys

flagone = "GPSCTF{HackBack1:2cc65d14825c76f5fd5383a9ccf08da2}"
flagtwo = str(open('/root/flag2.txt').read()).strip()

s = sys.argv[1]
c = sys.argv[2]

charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_rand_string(l):
    return ''.join(choice(charset) for i in range(l))

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

password = get_rand_string(32)

def encrypt(raw, password, iv):
    private_key = password
    raw = pad(raw)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return bytes.decode(base64.b64encode(cipher.encrypt(raw)))


def decrypt(enc, password, iv):
    private_key = password
    enc = base64.b64decode(enc)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return bytes.decode(unpad(cipher.decrypt(enc)))

gofolder = get_rand_string(32)
iv = bytes("cmEGiSu192NN80Li", 'utf-8')
keyfolderpw = "2jce3LsR9khUon5dLu2F1DlDDK5np1xP"
keyfolder = "z5q7BWy3EGQ1UhteLbRmZKVKlzcsCQbQ"
keyencrypted = encrypt(keyfolder, keyfolderpw, iv)
goflag = flagtwo

flagencrypt = encrypt(goflag, password, iv)
encflag = "%s" % (bytes.decode(base64.b64encode( iv + base64.b64decode(flagencrypt))))

with open('/template.go', 'r') as x:
    f = x.read()
    f = f.replace('FLAGENC', encflag)
    f = f.replace(' SLEEPCOUNT ', s)
    f = f.replace('CAMPAIGN', c)
x.close()

open('/tmp/main.go','w').write(f)

goencrypted = encrypt(gofolder, keyfolderpw, iv)

keydecrypted = decrypt(keyencrypted, keyfolderpw, iv)
godecrypted = decrypt(goencrypted, keyfolderpw, iv)

try:
    os.mkdir("/var/www/html/%s/" % gofolder)
    os.mkdir("/var/www/html/%s/" % keyfolder)
except:
    pass
open('/var/www/html/%s/Key.txt' % keyfolder,'w').write(password.strip())
open('/var/www/html/%s/flag.txt' % keyfolder,'w').write(flagone.strip())
os.system('env GOOS=windows GOARCH=386 go build -o /var/www/html/%s/Update.exe /tmp/main.go' % gofolder)
try:
    os.remove("/tmp/main.go")
except:
    pass
print(goencrypted.strip().replace('\n',''))