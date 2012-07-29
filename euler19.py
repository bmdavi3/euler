DAYS_IN_MONTH = {
    1: 31,   # Jan
    2: 28,   # Feb
    3: 31,   # Mar
    4: 30,   # Apr
    5: 31,   # May
    6: 30,   # Jun
    7: 31,   # Jul
    8: 31,   # Aug
    9: 30,   # Sep
    10: 31,  # Oct
    11: 30,  # Nov
    12: 31,  # Dec
}


def get_days(month, year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        if month == 2:
            return 29

    return DAYS_IN_MONTH[month]


if __name__ == "__main__":
    day = 1
    sundays_on_first = 0

    for year in xrange(1900, 2001):
        for month in xrange(1, 13):
            if year >= 1901 and day % 7 == 0:
                sundays_on_first += 1

            day += get_days(month, year)

    print sundays_on_first
