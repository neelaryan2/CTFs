import random
import re, os
from rubik.cube import Cube
from rubik.solve import Solver
import subprocess

MOVES = ["L", "R", "U", "D", "F", "B", "M", "E", "S"]
pattern = re.compile(r'\s+')


def get_cube(fp):
    lines = []
    while len(lines) < 9:
        line = re.sub(pattern, '', fp.readline())
        if line: lines.append(line)
    return Cube(''.join(lines))


def solve(file):
    with open(file, 'r') as fp:
        unsolved = get_cube(fp)
        scrambled = get_cube(fp)
        solved = get_cube(fp)

    solver = Solver(unsolved)
    solver.solve()
    assert unsolved.is_solved()
    scrambled.sequence(' '.join(solver.moves))

    rotates = ['X', 'Y', 'Z']
    while unsolved != solved:
        move = random.choice(rotates)
        getattr(unsolved, move)()
        getattr(scrambled, move)()

    password = re.sub(pattern, '', str(scrambled))
    return password


ctr = 127
while ctr >= 0:
    pwdfile = f'password{ctr}.txt'
    zipfile = f'archive{ctr}.zip'
    passwd = solve(pwdfile)
    cmd = f'unzip -q -o -P {passwd} {zipfile}'
    os.system(cmd)
    os.remove(pwdfile)
    os.remove(zipfile)
    print(zipfile, '=>', passwd)
    ctr -= 1
