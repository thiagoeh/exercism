import string

cipher_origin = string.ascii_lowercase + string.ascii_uppercase


def rotate(text, key):
    cipher_destin = (string.ascii_lowercase[key:] + string.ascii_lowercase[0:key]
                     + string.ascii_uppercase[key:] + string.ascii_uppercase[0:key])

    cipher_transl = str.maketrans(cipher_origin, cipher_destin)

    return text.translate(cipher_transl)
