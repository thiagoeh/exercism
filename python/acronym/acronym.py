import re

def abbreviate(words):

    # Split words using any puctuation as separator
    word_list = re.split('\W+', words)
    
    return ''.join([word[0].upper() for word in word_list])
