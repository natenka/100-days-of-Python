import re

def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    match = re.match(' +', text)
    if match:
        return len(match.group())
    return 0
