from collections import Counter
import json

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    download = s.get(CAR_DATA)
    data = json.loads(download.content.decode('utf-8'))


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    unique_automakers = {dicty['automaker'] for dicty in data}
    result = {automaker: get_models(automaker, year)
              for automaker in unique_automakers}
    most = max(result.items(), key=lambda x: len(x[1]))
    return most[0]



def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = {dicty['model'] for dicty in data
              if dicty['automaker'] == automaker and dicty['year'] == year}
    return models

