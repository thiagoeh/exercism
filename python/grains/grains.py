def on_square(integer_number):
    if not 0 < integer_number <= 64:
        raise ValueError(
            'square parameter must be a positive integer up to 64')

    return 2 ** (integer_number - 1)


def total_after(integer_number):
    if not 0 < integer_number <= 64:
        raise ValueError(
            'square parameter must be a positive integer up to 64')

    # Can be optimized inserting the on_square formula directly, but it would lose readability
    return sum(on_square(x) for x in range(1, integer_number+1))
