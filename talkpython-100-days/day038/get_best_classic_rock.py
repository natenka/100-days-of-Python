import csv
from collections import namedtuple
import os
from pprint import pprint

import click
from tabulate import tabulate


def convert_csv_to_namedtuple():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'classic-rock-song-list.csv')
    parsed_data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ntuple = parse_row_to_ntuple(row)
            parsed_data.append(ntuple)
    return parsed_data


def parse_row_to_ntuple(row):
    Song = namedtuple('Song', 'name artist year playcount')
    row['Release Year'] = int(row['Release Year']) if row['Release Year'] else 0
    return Song(row['Song Clean'], row['ARTIST CLEAN'],
                row['Release Year'], int(row['PlayCount']))


def best_songs(dataset, top, sort_asc):
    best = sorted(dataset, key=lambda x: x.playcount, reverse=not sort_asc)
    print(tabulate(best[:top], headers=map(str.title,best[0]._fields)))


def best_artist(dataset, top, sort_asc):
    artists = dict.fromkeys(set([song.artist for song in dataset]), 0)
    for song in dataset:
        artists[song.artist] += song.playcount
    best = sorted(artists.items(), key=lambda x: x[1], reverse=not sort_asc)
    print(tabulate(best[:top], headers=('Artist', 'Songs playcount')))


@click.command()
@click.option('--category', '-c', type=click.Choice(['artist', 'song']))
@click.option('--top', '-t', default=10, show_default=True, type=int)
@click.option('--sort_asc', is_flag=True)
def show_info(category, top, sort_asc):
    category_map = {'song': best_songs, 'artist': best_artist}
    function = category_map[category]
    dataset = convert_csv_to_namedtuple()
    function(dataset, top, sort_asc)


if __name__ == "__main__":
    show_info()

'''
$ python get_best_classic_rock.py --help
Usage: get_best_classic_rock.py [OPTIONS]

Options:
  -c, --category [artist|song]
  -t, --top INTEGER             [default: 10]
  --sort_asc
  --help                        Show this message and exit.



$ python get_best_classic_rock.py -c artist
Artist                           Songs playcount
-----------------------------  -----------------
Led Zeppelin                                1556
Van Halen                                   1243
Rolling Stones                              1143
Pink Floyd                                  1044
Tom Petty & The Heartbreakers                965
AC/DC                                        866
Aerosmith                                    813
ZZ Top                                       712
The Beatles                                  704
Queen                                        694



$ python get_best_classic_rock.py -c song
Name                         Artist          Year    Playcount
---------------------------  ------------  ------  -----------
Dream On                     Aerosmith       1973          142
Sweet Emotion                Aerosmith       1975          141
All Along the Watchtower     Jimi Hendrix    1968          141
You Shook Me All Night Long  AC/DC           1980          138
More Than a Feeling          Boston          1976          134
Carry On Wayward Son         Kansas          1976          134
Peace of Mind                Boston          1976          132
Crazy On You                 Heart           1976          125
Legs                         ZZ Top          1983          121
Sharp Dressed Man            ZZ Top          1983          120


$ python get_best_classic_rock.py -c artist --top 5
Artist                           Songs playcount
-----------------------------  -----------------
Led Zeppelin                                1556
Van Halen                                   1243
Rolling Stones                              1143
Pink Floyd                                  1044
Tom Petty & The Heartbreakers                965


$ python get_best_classic_rock.py -c song --sort_asc
Name                       Artist          Year    Playcount
-------------------------  ------------  ------  -----------
Hey, Hey (What Can I Do?)  Led Zeppelin    1970            0
Layla                      Eric Clapton       0            0
Art For Arts Sake          10cc            1975            1
Loser                      3 Doors Down    2000            1
Take On Me                 a-ha            1985            1
Baby, Please Don't Go      AC/DC              0            1
Hard As A Rock             AC/DC           1995            1
Jailbreak                  AC/DC           1984            1
Night Prowler              AC/DC           1979            1
Sin City                   AC/DC              0            1
'''

