'''
As you have probably seen on the new dashboard you can now gain Ninja Belts based on the amount of points (or Bitecoins) you gained solving Bites:

from pprint import pprint as pp
pp(HONORS)

{10: 'white',
 50: 'yellow',
 100: 'orange',
 175: 'green',
 250: 'blue',
 400: 'brown',
 600: 'black',
 800: 'paneled',
 1000: 'red'}
Complete the get_belt function below which receives a user_score which you can assume to be an int.

The function should return the corresponding belt name from the HONORS dict. For example with 162 points you would have the orange belt (not yet reached green), 401 = brown, 999 is paneled, etc.

Note that the scores are inclusive so if you have 10 points you have earned the white belt, ≥ 50 = yellow belt, etc. Also make sure you take the min and max boundaries into account (< 10 is no belt and > 1000 is the highest belt).

Is there a stdlib module that could be useful here? Have fun!
'''

from collections import OrderedDict
from itertools import takewhile


scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    if user_score < MIN_SCORE:
        return None
    for idx, (score, belt) in enumerate(HONORS.items()):
        if not score == MAX_SCORE:
            if user_score in range(score, scores[idx+1]):
                break
    return belt


def get_belt_itertools(user_score):
    """Using itertools.takewhile"""
    if user_score < MIN_SCORE:
        return None

    belts = takewhile(lambda x: x[0] <= user_score,
                      HONORS.items())
    return list(belts)[-1][1]
