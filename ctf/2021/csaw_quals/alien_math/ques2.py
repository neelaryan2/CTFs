c = '7759406485255323229225'

def second_question_function(a1, a2):
 	return (12 * a2 - 4 + 48 * a1 - a2) % 0xA;

def second_question(a1):
	for i in range(len(a1) - 1):
		v = a1[i + 1]
		a1[i + 1] = (v + second_question_function(a1[i], (i + a1[i])) ) % 10
	ret = ''.join([str(t) for t in a1])
	return ret

ans = [7]
for j in range(1, len(c)):
	nxt_num = None
	for t in range(10):
		cur = ans + [t]
		ret = second_question(cur)
		if c.startswith(ret):
			nxt_num = t
			break
	assert nxt_num is not None
	ans.append(nxt_num)

print(''.join([str(t) for t in ans]))
print(second_question(ans))

