import re
import json
import time
from collections import namedtuple
from pprint import pprint

import requests
from tabulate import tabulate
import click


def download_title(title):
    #r = requests.get('http://www.omdbapi.com/?t=Iron+Man&plot=full')
    title = '+'.join(title.split())
    req = f'http://www.omdbapi.com/?t={title}&plot=full&apikey='## add API key
    title_info = requests.get(req)
    return title_info.json()


def get_all_titles(filename):
    with open(filename) as f:
        content = json.load(f)
        all_movies = list(content['Marvel Cinematic Universe'].keys())
    return all_movies

def write_json_to_file(titles_file, dst_filename):
    json_data = {}
    all_titles = get_all_titles(titles_file)
    for title in all_titles:
        json_data[title] = download_title(title)
        time.sleep(2)
    with open(dst_filename, 'w', encoding='utf-8') as marvel:
        json.dump(json_data, marvel)


def json_to_namedtuple(json_filename):
    converted_data = []
    Movie = namedtuple('Movie', 'title year rating runtime money')
    with open(json_filename, encoding='utf-8') as marvel:
        data = json.load(marvel)
        for title, info in data.items():
            if info['BoxOffice'] == 'N/A':
                info['BoxOffice'] = '0'
            movie = Movie(title=title,
                          year=int(info['Year']), rating=float(info['imdbRating']),
                          runtime=int(info['Runtime'].split()[0]),
                          money=int(re.sub('[^\d]', '', info['BoxOffice'])))
            converted_data.append(movie)
    return converted_data


@click.command()
@click.argument('sort_by', type=click.Choice('title year rating runtime money'.split()))
@click.option('--top', '-t', type=int, default=5)
def show_best(sort_by, top=5):
    sorted_data = sorted(data, key=lambda movie: getattr(movie, sort_by), reverse=True)
    headers = sorted_data[0]._fields
    print(tabulate(sorted_data[:top], headers=headers))


if __name__ == "__main__":
    #write_json_to_file('marvel-cinematic-universe.json',
    #                   'all_marvel_movies.json')
    data = json_to_namedtuple('all_marvel_movies.json')
    show_best()


