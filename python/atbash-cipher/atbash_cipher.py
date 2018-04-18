from string import ascii_lowercase

cipher = 'zyxwvutsrqponmlkjihgfedcba'
strip_size = 5

encode_translation = str.maketrans(ascii_lowercase, cipher)
decode_translation = str.maketrans(cipher, ascii_lowercase)


def encode(plain_text):
    return add_spaces(plain_text.lower().replace('.', '').replace(',', '').replace(' ', '').translate(encode_translation))


def decode(ciphered_text):
    return ciphered_text.lower().replace(' ', '').translate(decode_translation)


def add_spaces(ciphered_text):
    return ' '.join([ciphered_text[i:i+strip_size] for i in range(0, len(ciphered_text), strip_size)])
