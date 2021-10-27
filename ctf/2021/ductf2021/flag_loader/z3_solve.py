from z3 import *


def check1():
    solver = Solver()
    X = [0x44, 0x55, 0x43, 0x54, 0x46]
    buf = [BitVec(f"buf_{i}", 8) for i in range(0, len(X))]
    solver.add(((X[0] ^ buf[0]) + (X[1] ^ buf[1]) + (X[2] ^ buf[2]) + (X[3] ^ buf[3]) + (X[4] ^ buf[4])) == 0)
    solver.add(buf[0] * buf[1] * buf[2] * buf[3] * buf[4] != 0)

    if not solver.check():
        print("No solution")
        exit(0)

    m = solver.model()
    print(m)

    solution = sorted([(d, m[d]) for d in m], key=lambda x: str(x[0]))
    solution = [b.as_long() for a, b in solution]
    p = 120
    for x in solution:
        p *= x
    wait1 = p & 0xff
    print('Wait1:', wait1)

    s = sum(a ^ b for a, b in zip(solution, X))
    assert s % 256 == 0

    return solution, wait1


def check2(num):
    solver = Solver()
    x = BitVec('x', 32)
    y = BitVec('y', 32)
    num = BitVecVal(num, 32)

    # solver.add(x > num)
    solver.add(y > num)
    solver.add((x + y) == num)
    # solver.add(((x * y) & 0xffff) > 0x3B)

    if solver.check() == unsat:
        print("No solution")
        exit(0)

    m = solver.model()
    x = m[x].as_long()
    y = m[y].as_long()
    print(m)
    print((x + y) & 0xffffffff, num)
    wait2 = (x * y) & 0xffff
    print('Wait2', wait2)

    return x, y, wait2


def check3(num):
    solver = Solver()
    x = [BitVec(f'x{i + 1}', 32) for i in range(5)]

    num = BitVecVal(num, 32)

    for i in range(1, 5):
        solver.add(x[i] > x[i - 1])

    solver.add((x[0] + x[1] + x[2] + x[3] + x[4]) == num)
    # solver.add(((x * y) & 0xffff) > 0x3B)

    if solver.check() == unsat:
        print("No solution")
        exit(0)

    m = solver.model()

    solution = sorted([(d, m[d]) for d in m], key=lambda y: str(y[0]))
    x = [b.as_long() for a, b in solution]

    print((x[0] + x[1] + x[2] + x[3] + x[4]) & 0xffffffff, num)
    wait3 = ((x[2] - x[1]) * (x[4] - x[3])) & 0xffff
    print('Wait3', wait3)
    print(x)

    return x, wait3


if __name__ == '__main__':
    check1()
    # check2(11681)
    # check3(31500)