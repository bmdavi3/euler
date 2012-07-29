import util


proper_divisor_sums = {}
amicable_sum = 0


for x in xrange(1, 10001):
    proper_divisors = sorted(util.get_factors(x))[:-1]

    _sum = sum(proper_divisors)

    if _sum in proper_divisor_sums and proper_divisor_sums[_sum] == x:
        amicable_sum += _sum
        amicable_sum += x

    proper_divisor_sums[x] = _sum

print amicable_sum
