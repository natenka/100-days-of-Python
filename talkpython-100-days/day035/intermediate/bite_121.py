'''
In this Bite you evaluate the strength of a password. Complete the function below and return a score from 0 to 5. Each of the following matches increases the score by one:

Password has both lower- and uppercase letters,
Password contains one or more numbers in addition to one or more characters,
Password has one or more special characters,
Password has a minimum length of 8 characters,
Password starting 8 chars ("long enough") that doesn't have repeating characters ('1234abcd' = good, '1234abbd' = bad)
Let's brush up some regex skills and score those passwords, have fun!
'''

import re


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    lower = re.compile(r'[a-z]+')
    upper = re.compile(r'[A-Z]+')
    numbers = re.compile(r'\d+')
    chars = re.compile(r'[a-zA-Z]+')
    special = re.compile(r'[$@]+')
    min_length = len(password) >= 8
    unique = re.compile(r'(.)\1')
    score = 0
    if lower.search(password) and upper.search(password):
        score += 1
    if numbers.search(password) and chars.search(password):
        score += 1
    if special.search(password):
        score += 1
    if min_length:
        score += 1
        if unique.search(password) == None:
            score += 1
    return score



