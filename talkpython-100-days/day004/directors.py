# -*- coding: utf-8 -*-
from collections import namedtuple, defaultdict, Counter
import csv
from pprint import pprint
from operator import itemgetter, attrgetter



def organize_movie_by_director(filename, min_movies=4, min_year=1960):
    Movie = namedtuple('Movie', 'title year score')
    movies_by_dir = defaultdict(list)

    with open(filename) as f:
        for line in csv.DictReader(f):
            try:
                m = Movie(line['movie_title'].strip(),
                          int(line['title_year']), float(line['imdb_score']))
                if m.year >= min_year:
                    movies_by_dir[line['director_name']].append(m)
            except ValueError:
                continue

    filtered_by_min_movies = {director: movies for director, movies in movies_by_dir.items()
                              if len(movies) >= min_movies}
    return filtered_by_min_movies


def director_rating(dataset):
    rating = {}
    for director, movies in dataset.items():
        rate = round(sum(map(attrgetter('score'), movies))/len(movies), 1)
        rating[director] = rate
    return rating


def pprint_top_directors(directors_rating_data, dataset, top=20):
    top_dirs = sorted(directors_rating_data.items(),
                      key=itemgetter(1), reverse=True)[:top]
    for position, (director, rating) in enumerate(top_dirs, 1):
        print()
        print("{:02}. {:53}{}".format(position, director, rating))
        print('-'*60)
        for movie in sorted(dataset[director], key=attrgetter('score'), reverse=True):
            print("[{}] {:50}{}".format(movie.year, movie.title, movie.score))

if __name__ == "__main__":
    result = organize_movie_by_director('movie_metadata.csv')
    rate = director_rating(result)
    pprint_top_directors(rate, result, top=10)

