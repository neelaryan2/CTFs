def isprime(n):
    if n <= 1: return False
    elif n <= 3: return True
    elif (n % 2 == 0) or (n % 3 == 0): return False
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0): return i
        i = i + 6
    return True

n = 57436275279999211772332390260389123467061581271245121044959385707165571981686310741298519009630482399016808156120999964
factors = 4 * 73 * 181 * 11411 * 235111 
print(n % factors)
n = n // factors
print(n)

while True:
    i = isprime(n)
    if type(i) != int:
        break
    f = i if n % i == 0 else i + 2
    print(f)
    n //= f
