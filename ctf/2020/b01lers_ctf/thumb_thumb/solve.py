arr = [0 for i in range(26)]
arr[0] = 0x66
arr[21] = 0x75
arr[4] = 0x7b
arr[7] = 0x6e
arr[9] = 0x5f
arr[10] = 0x30
arr[15] = 0x33
arr[22] = 0x6d
arr[12] = 0x72
arr[13] = 0x5f
arr[14] = 0x62
arr[17] = 0x74
arr[8] = 100
arr[18] = 0x5f
arr[11] = 0x75
arr[19] = 0x74
arr[6] = 0x33
arr[1] = 0x6c
arr[2] = 0x61
arr[3] = 0x67
arr[5] = 0x73
arr[20] = 0x68
arr[23] = 0x62
arr[16] = 0x73
arr[24] = 0x35
arr[25] = 0x7d
flag = ''
for i in arr:
	flag += chr(i)
print(flag)