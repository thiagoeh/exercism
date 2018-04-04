from string import ascii_lowercase

def is_pangram(sentence):
    sentence_lower = sentence.lower()

    for c in ascii_lowercase:
        if c not in sentence_lower:
            return False

    return True
