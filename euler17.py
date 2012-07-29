words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    15: 'fifteen',
    18: 'eighteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'onethousand',
}


def letterfy(x):
    if x in words:
        return words[x]

    if 13 < x and x < 20 and x not in words:
        return words[x % 10] + 'teen'

    if x < 100:
        return "%s%s" % (words[x - x % 10], words[x % 10])

    if x % 100 == 0:
        return "%shundred" % (words[x / 100])

    return "%sand%s" % (letterfy(x - x % 100), letterfy(x % 100))


print len("".join([letterfy(x) for x in range(1, 1001)]))
