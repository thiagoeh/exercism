def largest_product(series, size):
    if size < 0:
        raise ValueError('size must be a non-negative integer')

    # Generate all combinations based on the size
    combinations = (series[i:size+i] for i in range(0, len(series)-size+1))

    products = set()
    for combination in combinations:
        multiple = 1
        for char in combination:
            multiple *= int(char)
        products.add(multiple)

    # Return the largest product
    return max(products)


print(largest_product('23453456353645',3))
