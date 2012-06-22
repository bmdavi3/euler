def sum_of_squares(numbers):
    _sum = 0

    for n in numbers:
        _sum += n * n

    return _sum


def square_of_sums(numbers):
    _sum = sum(numbers)

    return _sum * _sum


numbers = xrange(1, 101)

print square_of_sums(numbers) - sum_of_squares(numbers)
