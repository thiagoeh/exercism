def is_isogram(string):
    chars = []
    ignored_chars = ['-', ' ']


    # Iterate the input string in lowercase form
    for c in string.lower():
        # Check if the current char is already in the chars list
        # AND if it's not one that should be ignored
        if c in chars and c not in ignored_chars:
            return(False)

        chars.append(c)
    
    # We are at the end of the string, without repeated chars
    # so it's a isogram!
    return True
