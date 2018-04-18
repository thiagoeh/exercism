def sum_of_multiples(limit, multiples):

    unique_multiples = set()

    # Maybe there is a more 'pythonic' way to do this, without the for loop
    for multiple in multiples:
        unique_multiples = unique_multiples.union(
            set(range(multiple, limit, multiple)))

    return sum(unique_multiples)
