from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto import Random # May be able to get rid of
from random import choice, shuffle
from OpenSSL import crypto
import binascii
import base64

pub = crypto.load_publickey(crypto.FILETYPE_PEM, base64.b64decode('LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUF0YmEwY2x2RWllS3A0MUtYaGlpUwpqWnluc2E5RlQzTmpVUE1ZaVBVLzN5L2IySU8zcnFaZmh5RTRCNlAzYXpueDRZMkRoYVVVZFNnN0V5OHJzZ29jCis0dzlIdDYwSTdEWWUxblVKeUt1ekZyTDZESmdxSFR6Sml3SHBCWFNTVnVhaU5KY2NRVXJKMWNaRzdTVG44YmcKbzBCdHNGT0tyVzVzTzNyOGxNWitxWDVldXNZWW9UMDd6U0p5T1V4WVNJcWlwUVpPcEc3Y2JNYVhQZlZaaERDbwpyOW9UVFZaUFA1ZzlqOHNoSmdDVnJLeXE4V2dQTk1sWDRBMVhKQnpIcXFZN2RTK2NZRFhuMmc2dmxOa2RESXpmCjd6U1ZxL0NWZzA1MG1CdXZYdTVWaWVheHhZQnREb0xUQ0JWMmcyYXlOY2pac2tJVmhFbXpvTjNveEd5dFFVNFIKUXdJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg=='))
pubkey = crypto.dump_publickey(crypto.FILETYPE_PEM, pub)

def random_string(size, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"):
	return ''.join(choice(chars) for z in range (size))

def encrypt_FileString( raw ):
	BS = 16
	pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
	key = bytes(random_string(16), 'utf-8')
	raw = bytes(pad(raw),'utf-8')
	iv = Random.new().read( AES.block_size )
	cipher = AES.new( key, AES.MODE_CBC, iv )
	return binascii.hexlify(iv + cipher.encrypt( raw )).decode('utf-8').strip(), binascii.hexlify(key)


def encrypt_RSA(pubkey, aeskey):
	try:
		rsakey = RsA.importKey(pubkey)
		rsakey = PKCS1_OAEP.new(rsakey)
		encrypted = rsakey.encrypt(aeskey)
		print('try')
	except:
		print('except')
		encrypted = aeskey
	return binascii.hexlify(encrypted)


outp = '3539333437353461373137333532333833333333333933303335333036383639dcb33a3cca39412b58f4095cbc30faf95f72c9c1e71c01aa0a1b0f89c11f03b751dccaa5bb3ec011cc0a40a08ba87827071e1fb52716c891a1263a53af721a18'
outp = binascii.unhexlify(outp)

key = binascii.unhexlify(outp[:32])
iv = outp[32:48]
c = outp[48:]

cipher = AES.new(key, AES.MODE_CBC, iv)
m = cipher.decrypt(c)

print(m)

