def is_armstrong(number):
    number_len = len(str(number))
    armstrong_sum = 0

    for n in str(number):
        armstrong_sum += int(n) ** number_len

    return number == armstrong_sum
