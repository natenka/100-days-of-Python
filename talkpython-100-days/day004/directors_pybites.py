import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from pprint import pprint

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_dir = defaultdict(list)
    with open(MOVIE_DATA) as f:
        for line in csv.DictReader(f):
            try:
                m = Movie(line['movie_title'].strip(),
                          int(line['title_year']), float(line['imdb_score']))
                if m.year >= MIN_YEAR:
                    movies_by_dir[line['director_name']].append(m)
            except ValueError:
                continue
    return movies_by_dir


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(sum(map(lambda x: x.score, movies))/len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    dir_score = [(director, calc_mean_score(movies))
                 for director, movies in directors.items()
                 if len(movies) >= MIN_MOVIES]
    best_dirs = sorted(dir_score, key=lambda x: x[1], reverse=True)
    return best_dirs

if __name__ == "__main__":
    dirs = get_movies_by_director()
    best = get_average_scores(dirs)
    pprint(best[:20])
