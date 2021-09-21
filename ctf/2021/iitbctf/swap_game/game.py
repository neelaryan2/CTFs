#!/usr/bin/python3
import random
import time

rand = random.SystemRandom()
randint = rand.randint


def replacement_test(list_replacements, string):
    def substitute(test_string, ini, after):
        initial = test_string
        s = test_string.replace(ini, after)
        return s, not s == initial

    # s ^ 2 rounds for string of length s
    for _ in range(len(string) ** 2):
        performed_replacement = False
        # Hint : you may define ur own list_replacements while solving the challenge
        for find, replace in list_replacements:
            string, performed_replacement = substitute(string, find, replace)
            # once a replacement is performed, go to next round, we go through the list from starting
            if performed_replacement:
                break
        # if no replacement was performed this round, we are done
        if not performed_replacement:
            break
    return string


def read_replacements_input(string):
    substitution = tuple(s.strip() for s in string.split('=>'))
    return substitution if len(substitution) == 2 else ('', '')


def level_runner(case_generator, max_subs, level, test_cases=32):
    if level == 5:
        print('-' * 80)
        print('Warning: This is the Final Level and is slightly tougher than the rest ;)')
    if input('See the next level? (y/n) ') == 'n':
        exit()

    print('-' * 80)
    print('Here is this level\'s intended behavior:')
    for _ in range(10):
        initial, target = case_generator()
        print(f'\nInitial string: {initial}')
        print(f'Target string: {target}')

    print('-' * 80)
    list_replacements = []
    current = input(
        f'Enter substitution of form "find => replace", {max_subs} max: '
    )
    list_replacements.append(read_replacements_input(current))
    for i in range(max_subs - 1):
        if input('Add another? (y/n) ') == 'n':
            break
        current = input(f'Enter substitution of form "find => replace", {max_subs - i - 1} left: ')
        list_replacements.append(read_replacements_input(current))

    print('-' * 80)
    print('Testing substitutions...', flush=True)
    for _ in range(test_cases):
        initial, target = case_generator()
        output = replacement_test(list_replacements, initial)
        if output != target:
            print(f'Failed on string: {initial}.')
            print(f'Expected: {target}.')
            print(f'Computed: {output}.')
            exit()
    print('Level passed!')


print('''
*********** Welcome to The Swap Game ****************
The game has 5 levels with 2 flags which you get after level 4 and level 5.
You have to enter a list of replacements to be swapped in the initial string to get target.
Your replacements will be tested on randomly generated test cases :).
There is a levelwise limit on number of max replacements you can define.
* Each time The first possible substitution will be performed recursively.
''')


def level_1():
    initial = f'{"1" * randint(0, 20)}hacking{"0" * randint(0, 20)}'
    target = initial.replace('hacking', 'CSeC')
    return initial, target


def level_2():
    initial = ''.join(
        rand.choice(['hi', 'asc']) for _ in range(randint(10, 20))
    )
    target = initial.replace('hi', 'bye').replace('asc', 'crash')
    return initial, target


def level_3():
    return 'q' * randint(11, 97), 'q'


def level_4():
    return 'q' * randint(11, 97), 'quackquack'


def level_5():
    random_string = ''.join(
        str(randint(0, 1)) for _ in range(randint(25, 50))
    )
    initial = random_string
    initial += rand.choice(['', '0', '1'])
    initial += random_string[::-1]

    if rand.randint(0, 1):
        return f'*{initial}$', 'palindrome'
    else:
        shuffled = list(initial)
        rand.shuffle(shuffled)
        return f'*{"".join(shuffled)}$', 'not_palindrome'


level_runner(level_1, 5, level=1)
level_runner(level_2, 10, level=2)
level_runner(level_3, 10, level=3)
level_runner(level_4, 10, level=4)
print('-' * 80)
print('Congrats! Here is the flag for the easy version of the Swap Game: IITB{w3ll_sw4p5_ar3_1nte9es7in6}') # flag present in the program running on server
print('-' * 80)
# time.sleep(2)
level_runner(level_5, 100, test_cases=128, level=5)
print('-' * 80)
print('You win! Here is the final flag: IITB{tu9in6_c0mpl3t3_w0w_UwU}')  # flag present in the program running on server
print('-' * 80)
