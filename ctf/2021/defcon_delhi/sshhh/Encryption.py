import secrets

def shhh(note):
	lol = [ord(char) for char in note]
	key = secrets.choice(range(128))
	funkey = [fun ^ key for fun in lol]
	return [''.join([fun.to_bytes((fun.bit_length()+7)// 8, byteorder = 'big').decode() for fun in funkey]), key]

flag = shhh('dc_9111{FAKE_FLAG}')

f = open("flag.txt",'w')
for element in flag :
	f.write(str(element) + "\n")
	
f.close()	