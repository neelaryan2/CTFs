import gdb
import string

CHARSET = string.printable[:94].encode()

base_addr = 0x555555554000

bp = gdb.Breakpoint(f'*{base_addr + 0x1036}')


def run_input(inp):
    with open('temp_input', 'w+') as fp:
        fp.write(inp)
    gdb.execute(f'run < temp_input')
    
fuckthisfuckthisfuckthisfuckthisfuckthisfuckthis
run_input('fuckthis')
ret = gdb.parse_and_eval("*$rdi")
print(ret)

# def get_(addr, lent):
#     retval = b''
#     for i in range(0, lent, 4):
#         t = gdb.parse_and_eval(f"*{addr+i}")
#         retval += int.to_bytes(int(t), 4, 'little')
#     return retval


# with open('temp_input', 'wb') as f:
#     f.write(b'LMAO')
# gdb.execute('run < temp_input')
# flag_enc = get_string(base_addr + 0x4830, 30)


# def encrypt(flag):
#     with open('temp_input', 'wb') as f:
#         f.write(flag)
#     gdb.execute(f'run < temp_input')
#     flag_enc = get_string(base_addr + 0x4800, 30)
#     return flag_enc


# flag = bytearray(30)
# for i in range(30):
#     for c in CHARSET:
#         flag[i] = c
#         x = encrypt(flag)
#         if x[i] == flag_enc[i]:
#             print(flag)
#             break