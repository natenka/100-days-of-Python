import glob
import json
import os
from urllib.request import urlretrieve
import re

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    data = []
    for file in files:
        with open(file) as f:
            data.append(json.load(f))
    return data


def get_single_comedy(movies):
    return [movie for movie in movies
            if 'Comedy' in movie['Genre']][0]['Title']


def get_movie_most_nominations(movies):
    max_nomin = max(movies, key=lambda x: int(x['Awards'].split()[-2]))
    return max_nomin['Title']


def get_movie_longest_runtime(movies):
    max_run = max(movies, key=lambda x: int(x['Runtime'].split()[-2]))
    return max_run['Title']
