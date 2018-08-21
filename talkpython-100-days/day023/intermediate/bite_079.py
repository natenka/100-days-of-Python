import csv
from collections import defaultdict

import requests

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    r = requests.get(CSV_URL)
    return r.text


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    reader = csv.DictReader(content.splitlines())
    tz_map = defaultdict(list)
    for line in reader:
        tz = line['tz']
        if '/' in tz:
            tz_map[tz].append('+')
    for tz, users in sorted(tz_map.items()):
        print(f"{tz:21}| {''.join(users)}")

create_user_bar_chart(get_csv())

def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        return download.content.decode('utf-8')


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        tz = row['tz']
        timezones[tz] += 1

    for location, count in sorted(timezones.items()):
        print(f'{location:<20} | {"+"*count}')
