def is_palindrome(x):
    _x = str(x)

    if len(_x) == 1:
        return True

    if _x[0] == _x[-1]:
        if len(_x) == 2:
            return True

        return is_palindrome(_x[1:-1])

    return False


def largest_palindrome(largest_factor):
    largest_palindrome = 0

    for x in xrange(largest_factor, 1, -1):
        for y in xrange(x, 1, -1):
            product = x * y

            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome


print largest_palindrome(999)
