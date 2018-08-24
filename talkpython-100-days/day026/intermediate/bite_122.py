from collections import Counter


def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    c1 = Counter(word1.replace(' ', '').lower())
    c2 = Counter(word2.replace(' ', '').lower())
    return c1 == c2
