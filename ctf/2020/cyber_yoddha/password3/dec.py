import base64

base64_string = "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="
base64_bytes = base64_string.encode("ascii")
passBytes = base64.b64decode(base64_bytes) 
finalPass = passBytes.decode("ascii")
newPass = list(finalPass)
for i in range(0,40):
    newPass[i] = chr(ord(newPass[i]) ^ 0x55)
password = ''.join(newPass)
print(password)