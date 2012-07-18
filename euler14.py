lengths = {}


def collatz_length(x):
    if x <= 1:
        return 1

    if x % 2 == 0:
        _next = x / 2
    else:
        _next = 3 * x + 1

    return 1 + lengths.get(_next, collatz_length(_next))


def fast_collatz_length(x):
    length = 1
    original_x = x

    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1

        if x in lengths:
            length += lengths[x]
            break

        length += 1

    lengths[original_x] = length

    return length


max_length = 0
max_number = None


for x in xrange(0, 1000000):
    length = fast_collatz_length(x)

    if length > max_length:
        max_length = length
        max_number = x


print max_number
