'''
In this Bite we will answer some questions about stocks, using some JSON data obtained from the awesome Mockeroo fake data generator service.

Here is a snippet of the output you will parse (full output here):

  [{"id":1,"name":"Anworth Mortgage Asset  Corporation",
    "symbol":"ANH","industry":"Real Estate Investment Trusts",
    "sector":"Consumer Services","market":"NYSE","cap":"$600.57M"},
   {"id":2,"name":"DarioHealth Corp.",
   "symbol":"DRIO","industry":"Medical/Dental Instruments",
   "sector":"Health Care","market":"NASDAQ","cap":"$21.78M"},
   ... 998 more stocks ...
  ]
Complete the 4 functions below following the instructions in the docstrings. Good luck and keep calm and parse your Data in Python.
'''

import json

import requests

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    download = s.get(STOCK_DATA)
    stocks = json.loads(download.content.decode('utf-8'))


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    pass


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    pass


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    pass


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    pass



###tests
from stocks import (_cap_str_to_mln_float,
                    get_stock_symbol_with_highest_cap,
                    get_industry_cap,
                    get_sectors_with_max_and_min_stocks)


def test_cap_str_to_mln_float():
    assert _cap_str_to_mln_float('n/a') == 0
    assert _cap_str_to_mln_float('$100.45M') == 100.45
    assert _cap_str_to_mln_float('$20.9B') == 20900


def test_get_stock_symbol_with_highest_cap():
    assert get_stock_symbol_with_highest_cap() == 'JNJ'


def test_get_industry_cap():
    assert get_industry_cap("Business Services") == 368853.27
    assert get_industry_cap("Real Estate Investment Trusts") == 243295.36


def test_get_sectors_with_max_and_min_stocks():
    assert get_sectors_with_max_and_min_stocks() == ('Finance',
                                                     'Transportation')
