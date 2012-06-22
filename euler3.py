import math

from util import is_prime


def largest_prime_factor(number):
    for x in xrange(int(math.sqrt(number)), 1, -1):
        if number % x == 0 and is_prime(x):
            return x


print largest_prime_factor(600851475143)
