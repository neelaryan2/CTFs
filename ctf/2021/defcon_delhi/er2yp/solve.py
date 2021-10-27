nums = [35, 90, 51, 19, 103, 120, 95, 95, 30, 10, 103, 12, 103, 82, 30, 24, 121, 100, 105, 78, 84, 95, 92, 120, 10, 120, 92, 95]

init = b'dc_9111'

key = []
for b1, b2 in zip(init[::-1], nums[-len(init):]):
	key.append((b2 - 10) ^ b1)

ans = []
for i in range(0, len(nums), len(key)):
	for b1, b2 in zip(key, nums[i:i + len(key)]):
		ans.append((b2 - 10) ^ b1)

flag = bytes(ans[::-1])
print(flag)
