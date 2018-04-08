def word_count(phrase):
    words = {}

    phrase_stripped = (
       phrase.lower().replace(':', ' ').replace('.', ' ').replace(',', ' '))

    for word in phrase_stripped.split(' '):
        word_stripped = word.strip()
        if word_stripped != '':
            words[word_stripped] = words.get(word_stripped, 0) + 1

    return words


if __name__ == '__main__':
    print(word_count('bblah bleh bleh blih'))
