def is_leap_year(year):
    is_leap = (year%4 == 0) & (not (year%100 == 0) or (year%400 == 0))
    return is_leap
