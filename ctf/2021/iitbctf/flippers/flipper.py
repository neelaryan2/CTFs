#!/usr/local/bin/python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii
import os

key = os.urandom(16)
iv = os.urandom(16)

operations = 3

for _ in range(operations):
    print("Enter a string that when decrypted contains 'csec_iitb'.")
    print("1. Check")
    print("2. Encrypt")
    inp = input("> ")
    if inp == "1":
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct = binascii.unhexlify(input("Enter ciphertext (in hex): "))
        assert len(ct) % 16 == 0
        pt = cipher.decrypt(ct)

        if b"csec_iitb" in pt:
            print("Here is the flag: [REDACTED]")
            exit()
        else:
            print("Bad")
    else:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = binascii.unhexlify(input("Enter plaintext (in hex): "))

        if b"csec_iitb" in pt:
            print("I'm not making it that easy for you!")
        else:
            ct = cipher.encrypt(pad(pt, 16))
            print(binascii.hexlify(ct).decode())

print("Out of operations!")