from pwn import *
from word_search import WordSearch, transpose_grid

host = 'challenge.ctf.games'
port = 30959

# flag{ac670e1f34da9eb748b3f241eb03f51b}

def parse_grid(conn):
    log.info('Parsing grid...')
    # find level
    level = None
    while True:
        l = conn.recvline().decode().split()
        if len(l) >= 1 and l[0] == 'Wordsearch':
            level = int(l[2].split('/')[0])
            break
    assert level is not None

    # find grid start
    while True:
        l = conn.recvline().decode().split()
        if len(l) >= 1 and l[0] == '---':
            break

    # find grid
    grid = []
    l = conn.recvline().decode().split()
    while l[0] != '---':
        row = ''.join(l[2:])
        grid.append(row)
        l = conn.recvline().decode().split()

    # last line
    l = conn.recvline().decode().split()
    assert l[0] == 'Y'
    return grid, level


def play(conn, level, grid):
    G = WordSearch(grid)
    for _ in range(5):
        l = conn.recvuntil(b'> ').decode()
        word = l.split(':')[0]
        log.info(f'Word: {word}')
        indices = G.patternSearch(word)
        ans = str(indices).encode()
        conn.sendline(ans)
    log.success(f'Passed Level {level}')


p = remote(host, port)
p.recvuntil(b'> ')
p.sendline(b'play')

for _ in range(30):
    grid, level = parse_grid(p)
    tgrid = transpose_grid(grid)
    log.info(f'Playing Level {level}')
    log.info('GRID')
    for row in tgrid:
        print('\t', row)
    play(p, level, tgrid)

flag = p.recvlines(6)[-1].decode()
log.success(f'FLAG: {flag}')
