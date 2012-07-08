import math


def is_prime(x):
    for y in xrange(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            return False

    return True


def get_factors(n):
    factors = [1, n]

    for x in xrange(1, int(math.sqrt(n)) + 1):
        if n % x == 0:
            factors.append(x)
            factors.append(n / x)

    return sorted(list(set(factors)))
