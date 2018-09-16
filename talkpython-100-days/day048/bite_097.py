from collections import defaultdict
import os
from urllib.request import urlretrieve
import re

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table')
    tds = table.find_all('td', {'style': "white-space: nowrap"})
    dates = [re.split('[A-Z]', td.getText().strip())[0].split('-')[1] for td in tds]
    links = table.find_all('a')
    holidays_names = [a.getText() for a in links]
    for month, hol in zip(dates, holidays_names):
        holidays[month].append(hol)
    return holidays


print(get_us_bank_holidays())

def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all("table", class_="list-table")

    # start at 2nd item ignoring header
    for tr in table[0].find_all('tr')[1:]:
        time = tr.find('time')
        href = tr.find('a')
        day = href.text
        yy, mm, dd = time.text.split('-')  # or use dt.striptime
        holidays[mm].append(day)

    return holidays
