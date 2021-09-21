import hashlib

username = b"MORTON"
enc = hashlib.sha256(username).hexdigest()[1:9]
print(enc)
# picoCTF{1n_7h3_|<3y_of_75fc1081}
