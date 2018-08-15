import os
import urllib.request
from string import punctuation
from collections import Counter
import re

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    with open(harry_text) as harry, open(stopwords_file) as stop:
        text = re.sub(f'[{punctuation}]+', '', harry.read().lower())
        stopwords = set(stop.read().lower().split('\n'))
    words = text.split()
    c = Counter(words)
    [c.pop(w) for w in stopwords if w in c]
    return c.most_common(1)[0]


