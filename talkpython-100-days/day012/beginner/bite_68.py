import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    table = str.maketrans({key: None for key in string.punctuation})
    return input_string.translate(table)
