def square_of_sum(count):
    sum_ = 0
    for i in range(1, count+1):
       sum_ += i
    return sum_ ** 2


def sum_of_squares(count):
    sum_ = 0
    for i in range(1, count+1):
        sum_ += i ** 2
    return sum_

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)

