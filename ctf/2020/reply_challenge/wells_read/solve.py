with open('The Time Machine by H. G. Wells.txt', 'r') as fp:
	content = fp.read()

with open('words.txt') as fp:
	words = fp.readlines()

wordset = set([w.strip().lower() for w in words])

fin = []
for cur in content.split():
	word = cur.lower()
	if word not in wordset:
	# if '{' in word or '}' in word:
		fin.append(word)

print(len(fin))
print(fin)
