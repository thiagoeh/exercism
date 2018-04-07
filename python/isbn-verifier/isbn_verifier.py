def verify(isbn):
    
    # Initialize sum
    isbn_sum = 0

    # Removing dashes
    isbn_stripped = isbn.replace('-','')

    # Test if we have the right length
    if len(isbn_stripped) != 10:
        return False

    # X at the end is equivalent to 10 at the position
    if(isbn_stripped[-1] == 'X'):
        # Replace X with a 0 at the end and increment isbn_sum
        isbn_stripped = isbn_stripped[:-1] + '0'
        isbn_sum = 10

    # Test if the input have any letter (which makes it invalid)
    if not isbn_stripped.isnumeric():
        return False

    # Calculates the sum according to validation algorithm
    isbn_sum += ( int(isbn_stripped[0]) * 10 \
            + int(isbn_stripped[1]) * 9 \
            + int(isbn_stripped[2]) * 8 \
            + int(isbn_stripped[3]) * 7 \
            + int(isbn_stripped[4]) * 6 \
            + int(isbn_stripped[5]) * 5 \
            + int(isbn_stripped[6]) * 4 \
            + int(isbn_stripped[7]) * 3 \
            + int(isbn_stripped[8]) * 2 \
            + int(isbn_stripped[9]) * 1 )
    isbn_modulus = isbn_sum % 11

    return (isbn_modulus == 0)

