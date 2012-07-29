GRID_SIZE = 20

cache = {}


def get_key(x, y):
    return str(sorted([x, y]))


def routes(x, y):
    key = get_key(x, y)

    if key in cache:
        return cache[key]

    if GRID_SIZE == x or GRID_SIZE == y:
        return 1

    r = 0

    if x < GRID_SIZE:
        r += routes(x + 1, y)

    if y < GRID_SIZE:
        r += routes(x, y + 1)

    cache[key] = r

    return r


print routes(0, 0)
