def func8(a):
    return a + 2


def func7(a):
    if a <= 100:
        return 7
    else:
        return a


def func6(a):
    return (800 * 1932) % 314


def func5(a):
    return func8(a)


def func4(a):
    return a


def func3(a):
    return func7(a)


def func2(a):
    if a > 499:
        return func5(a + 13)
    else:
        return func4(a - 86)


def func1(a=3459413018):
    if a <= 100:
        return func3(a)
    else:
        return func2(a + 100)

print(func1())