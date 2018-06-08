def transform(legacy_data):
    converted_data = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            converted_data[letter.lower()] = score
    return converted_data
