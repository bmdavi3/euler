import util


def sum_primes_below(limit):
    total = 0

    for x in xrange(2, limit):
        if util.is_prime(x):
            total += x

    return total


print sum_primes_below(2000000)
