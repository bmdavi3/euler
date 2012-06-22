import math


def is_prime(x):
    for y in xrange(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            return False

    return True


def prime_factorization(x):
    if is_prime(x):
        return [x]

    for y in xrange(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            return prime_factorization(x / y) + prime_factorization(y)


def in_powers(factors):
    powers = {}

    for x in factors:
        if x in powers:
            powers[x] += 1
        else:
            powers[x] = 1

    return powers


biggest_powers = {}

for x in xrange(1, 21):
    pf = prime_factorization(x)
    powers = in_powers(pf)

    for key, value in powers.iteritems():
        if value > biggest_powers.get(key, 0):
            biggest_powers[key] = value

print biggest_powers

product = 1

for key, value in biggest_powers.iteritems():
    print key, value
    product = product * int(math.pow(key, value))

print product
