import re

VOWELS = list('aeiou')
PYTHON = list('python')


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(c in VOWELS for c in list(input_str.lower()))


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    if re.search('[python]', input_str, re.I):
        return True
    return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    if re.search('\d', input_str):
        return True
    return False
