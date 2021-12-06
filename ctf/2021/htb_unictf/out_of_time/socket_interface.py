import time
import socket
import base64
import numpy as np
import matplotlib.pyplot as plt



HOST = '165.227.225.205' # This must be changed to the corresponding value of the live instance
PORT = 32482  # This must be changed to the corresponding value of the live instance

# This function is used to decode the base64 transmitted power trace (which is a NumPy array)
def b64_decode_trace(leakage):
	byte_data = base64.b64decode(leakage) # decode base64
	return np.frombuffer(byte_data) # convert binary data into a NumPy array


# This function is used to communicate with the remote interface via socket
# The socket connection is also accessible with the use of netcat (nc)
def connect_to_socket(option, data):
	data = data.encode()
	# Initialize a socket connection 
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		# Connect to the HOST machine on the provided PORT
		s.connect((HOST, PORT))
		
		# Receive initial message
		resp_1 = s.recv(1024)

		# Select one of the two available options of this interface
		s.sendall(option) 	

		# Receive response
		resp_2 = s.recv(1024)

		# Send the data 
		s.sendall(data) 

		# Receive response
		# receive base64 encoded binary data 
		# that represented the power traces as a Numpy array 
		# use loop to avoid missing packets due to high latency 
		resp_data = b''
		tmp = s.recv(8096)
		while tmp != b'':
			resp_data += tmp
			tmp = s.recv(8096)
		s.close()

		# The print commands can be used for debugging in order to observe the responses
		# The following print commands can be commented out.
		# print(resp_1.decode('ascii'))
		# print(option)
		# print(resp_2.decode('ascii'))
		# print(data)

		return resp_data


# Sample plaintext 
# password_guess = 'password_guess'
password_guess = 'a'

# Example use 
# print("Option 1:")
leakage = connect_to_socket(b'1', password_guess)
power_trace = b64_decode_trace(leakage)
# print("Length of power trace: {}".format(power_trace.shape))

p = np.copy(power_trace)
p -= p.min()
p *= 255 / p.max()
p = p.astype(int)
p = bytes(p)

for i in range(0, len(p), 4):
	extra = p[i + 1:i + 4]
	assert extra == bytes([0] * 3)

p = [p[i] for i in range(0, len(p), 4)]
cnt = [0 for _ in range(256)]

print(p[0])

# import string
# for ch in p:
# 	cnt[ch] += 1
# 	if chr(ch) in string.printable:
# 		print(chr(ch), end='')
# print()

# plt.plot(cnt)
# plt.show()
# plt.close()


# Always use a delay between each connection 
# in order to have a stable communication with the remote instance
time.sleep(0.1)
