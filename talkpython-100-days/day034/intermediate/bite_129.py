import json

import requests
from collections import Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    download = s.get(STOCK_DATA)
    stocks = json.loads(download.content.decode('utf-8'))

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    cap = cap.strip('$')
    if cap == 'n/a':
        return 0
    if 'M' in cap:
        return float(cap.strip('M'))
    if 'B' in cap:
        return float(cap.strip('B')) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    result = sum([_cap_str_to_mln_float(info['cap'])
                  for info in stocks if info['industry'] == industry])
    return round(result, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    max_st = max(stocks, key=lambda x: _cap_str_to_mln_float(x['cap']))
    return max_st['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    c = Counter([info['sector'] for info in stocks
                 if not info['sector'] == 'n/a'])
    max_s, *others, min_s = c.most_common()
    return max_s[0], min_s[0]

