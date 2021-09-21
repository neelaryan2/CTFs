import os
from subprocess import check_output, STDOUT, CalledProcessError

# flag{ec8753d9932766b1724618b5ad12de13}

def extract(password, verbose=False):
    command = f'.\\uharc.exe e -pw{password} -o+ .\\uhaha.uha'.split()
    try:
        out = check_output(command, stderr=STDOUT)
    except CalledProcessError as e:
        out = e.output

    out = out.decode().replace('\r', '')
    out = [line for line in out.split('\n')[5:] if line]
    out = '\n'.join(out)

    if verbose:
        print('[+] Trying password:', password)
        print('[+] Command:', ' '.join(command))
        print(out)
    return out


def one_pass(passwords):
    os.replace('uhaha', 'uhaha.uha')
    for pw in passwords:
        out = extract(pw)
        if 'successfully' in out:
            os.remove('uhaha.uha')
            return pw
    os.replace('uhaha.uha', 'uhaha')
    return None


with open('passwords.txt') as fp:
    passwords = [l.strip() for l in fp.readlines() if l.strip()]


for i in range(100):
    found = one_pass(passwords)
    print('Password found:', found)

