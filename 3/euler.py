import math


def is_prime(x):
    for y in xrange(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            return False

    return True


def largest_prime_factor(number):
    for x in xrange(int(math.sqrt(number)), 1, -1):
        if number % x == 0 and is_prime(x):
            return x


print largest_prime_factor(600851475143)
