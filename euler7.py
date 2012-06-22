from util import is_prime


def get_xth_prime(xth):
    primes_found = 0
    x = 2

    while True:

        if is_prime(x):
            primes_found += 1

            if primes_found == xth:
                return x

        x += 1


print get_xth_prime(10001)
