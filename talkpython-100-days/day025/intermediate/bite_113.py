'''
In this Bite you extract words from a text that contain non-ascii characters. So Fichier non trouvé would return a list of one matching word: ['trouvé'].

Calling extract_non_ascii_words with He wonede at Ernleȝe at æðelen are chirechen it returns: ['Ernleȝe', 'æðelen'], etc.

See the tests for more. Have fun!
'''
import re
import string

def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    non_ascii = []
    for word in text.split():
        m = re.search('[^\w]+', word.strip(string.punctuation), re.ASCII)
        if m:
            non_ascii.append(word)
    return non_ascii


def _is_ascii(word):
    """Helper to determine if a word consists of only ascii chars"""
    return not all(ord(char) < 128 for char in word)


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [word for word in text.split() if _is_ascii(word)]
