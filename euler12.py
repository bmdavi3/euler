import util


def triangle_numbers():
    _sum = 0
    x = 1

    while True:
        _sum += x
        yield _sum

        x += 1


for x in triangle_numbers():
    if len(util.get_factors(x)) > 500:
        print x
        break
