
def decode_char(c, multiplier):
    if multiplier == '':
        multiplier = 1

    return c * int(multiplier)


def decode(string):
    multiplier = ''
    decoded_str = ''
    for c in string:
        if c.isdigit():
            multiplier = multiplier + c
        else:
            decoded_str = decoded_str + decode_char(c, multiplier)
            multiplier = ''

    return decoded_str


def encode_char(c, multiplier):
    if int(multiplier) == 0:
        return ''
    elif int(multiplier) == 1:
        return c
    else:
        return str(multiplier) + c


def encode(string):
    encoded_str = ''
    previous_char = ''
    char_counter = 0
    for c in string:
        if c == previous_char:
            char_counter = char_counter + 1
        else:
            encoded_str = encoded_str + \
                encode_char(previous_char, char_counter)
            previous_char = c
            char_counter = 1
    encoded_str = encoded_str + encode_char(previous_char, char_counter)

    return encoded_str
