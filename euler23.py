def get_proper_divisors(x):
    proper_divisors = []

    for i in xrange(1, x / 2 + 1):
        if x % i == 0:
            proper_divisors.append(i)

    return proper_divisors


def is_abundant(x):
    pd_sum = sum(get_proper_divisors(x))

    return pd_sum > x


def build_abundant_list(x):
    abundants = []

    for x in xrange(1, x + 1):
        if is_abundant(x):
            abundants.append(x)

    return abundants


def build_abundant_dict(x):
    abundants = {}

    for x in xrange(1, x + 1):
        if is_abundant(x):
            abundants[x] = True

    return abundants


def get_non_sum_abundants():
    print "building list..."

    ab_list = build_abundant_list(28123)

    print "building dict..."

    ab_dict = {}
    for x in ab_list:
        ab_dict[x] = True

    print "finding integers..."

    non_sum_abs = []

    for x in xrange(1, 28123):
        for a in ab_list:
            if a >= x:
                non_sum_abs.append(x)
                print "{}: no".format(x)
                break

            diff = x - a

            if diff in ab_dict:
                print "{}: yes".format(x)
                break

    return non_sum_abs


nsa = get_non_sum_abundants()

print sum(nsa)
