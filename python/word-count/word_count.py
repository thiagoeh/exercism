def word_count(phrase):
    words = {}

    phrase_stripped = (
           phrase.lower().replace(':', ' ').replace('.', ' ').replace(',', ' ').replace('_', ' ').replace('\t', ' ')
       )

    phrase_stripped = ''.join( c for c in phrase_stripped if  c not in
            '?:!/;$#@&%^*()' )

    for word in phrase_stripped.split(' '):
        word_stripped = word.strip()
        word_stripped = word_stripped.strip("\"")
        word_stripped = word_stripped.strip("'")
        if word_stripped != '':
            words[word_stripped] = words.get(word_stripped, 0) + 1

    return words


if __name__ == '__main__':
    print(word_count("Joe can't tell between 'large' and large."))
