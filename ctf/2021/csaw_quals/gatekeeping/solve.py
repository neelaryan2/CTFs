from Crypto.Cipher import AES
import binascii

key = 'b5082f02fd0b6a06203e0a9ffb8d7613dd7639a67302fc1f357990c49a6541f3'
key = bytes.fromhex(key)

with open('dist/flag.txt.enc', 'rb') as fp:
	data = fp.read()


key_id = data[:16]
data = data[16:]


iv = data[:AES.block_size]
data = data[AES.block_size:]

cipher = AES.new(key, AES.MODE_CFB, iv)
data = cipher.decrypt(data)

print(data)
