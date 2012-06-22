import math


def is_prime(x):
    for y in xrange(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            return False

    return True
