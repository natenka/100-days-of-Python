'''
In this Bite you are provided with 3 data structures: a list of ints, a list of datetimes, and a list of dicts.

Complete the 3 functions to return the largest n of each using heapq (our tests require this data type here).

Have fun and keep calm and code in Python!
'''
from datetime import datetime
import heapq

numbers = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]
dates = [datetime(2018, 1, 23, 0, 0),
         datetime(2017, 12, 19, 0, 0),
         datetime(2017, 10, 15, 0, 0),
         datetime(2019, 2, 27, 0, 0),
         datetime(2017, 3, 29, 0, 0),
         datetime(2018, 8, 11, 0, 0),
         datetime(2018, 5, 3, 0, 0),
         datetime(2018, 12, 19, 0, 0),
         datetime(2018, 11, 19, 0, 0),
         datetime(2017, 7, 7, 0, 0)]
# https://www.forbes.com/celebrities/list
earnings_mln = [
    {'name': 'Kevin Durant', 'earnings': 60.6},
    {'name': 'Adele', 'earnings': 69},
    {'name': 'Lionel Messi', 'earnings': 80},
    {'name': 'J.K. Rowling', 'earnings': 95},
    {'name': 'Elton John', 'earnings': 60},
    {'name': 'Chris Rock', 'earnings': 57},
    {'name': 'Justin Bieber', 'earnings': 83.5},
    {'name': 'Cristiano Ronaldo', 'earnings': 93},
    {'name': 'Beyoncé Knowles', 'earnings': 105},
    {'name': 'Jackie Chan', 'earnings': 49},
]


def get_largest_number(numbers, n=3):
    heapq.heapify(numbers)
    return numbers[-n:]



def get_latest_dates(dates, n=3):
    pass


def get_highest_earnings(earnings_mln, n=3):
    pass


#########################################
#TESTS
from datetime import datetime
import inspect

from top_n import (numbers, dates, earnings_mln,
                   get_largest_number, get_latest_dates,
                   get_highest_earnings)


def test_get_top_n():
    assert get_largest_number(numbers) == [6, 5, 4]
    assert get_largest_number(numbers, n=2) == [6, 5]
    assert get_largest_number(numbers, n=4) == [6, 5, 4, 3]

    assert get_latest_dates(dates) == [datetime(2019, 2, 27, 0, 0),
                                       datetime(2018, 12, 19, 0, 0),
                                       datetime(2018, 11, 19, 0, 0)]
    assert get_latest_dates(dates, n=1) == [datetime(2019, 2, 27, 0, 0)]

    assert get_highest_earnings(earnings_mln) == [{'name': 'Beyoncé Knowles',
                                                   'earnings': 105},
                                                  {'name': 'J.K. Rowling',
                                                   'earnings': 95},
                                                  {'name': 'Cristiano Ronaldo',
                                                   'earnings': 93}]


def test_heapq_used():
    err_msg = 'We want you to play with heapq for this one :)'
    assert 'heapq' in inspect.getsource(get_largest_number), err_msg
    assert 'heapq' in inspect.getsource(get_latest_dates), err_msg
    assert 'heapq' in inspect.getsource(get_highest_earnings), err_msg
