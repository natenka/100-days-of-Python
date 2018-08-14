'''
# assuming you pulled our challenges master and are in our 11/ subdirectory
# code this unix pipeline into Python using generators
#
$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
4 unittest
4 sys
3 re
3 csv
2 tweepy
2 random
2 os
2 json
2 itertools
1 time
1 datetime
'''
from glob import glob
import re
from collections import Counter

import click


def gen_files(path):
    files = glob(path)
    for f in files:
        yield f


def grep_lines(filenames, pattern):
    for filename in filenames:
        with open(filename) as f:
            for line in f:
                if re.search(pattern, line):
                    yield line.rstrip()


def sed_replace(lines, pattern1, pattern2):
    for line in lines:
        yield re.sub(pattern1, pattern2, line)


def get_count_report(lines, top=None):
    counted_items = Counter(lines)
    for item, count in counted_items.most_common(top):
        print(f'{count:5} {item}')


@click.command()
@click.option('--path', '-p', required=True)
@click.option('--search', '-s', default='^import ', show_default=True)
@click.option('--replace', '-r', default='', show_default=True)
@click.option('--top', '-t', default=None, show_default=True, type=int)
def run_pipeline(path, search, replace, top):
    files = gen_files(path)
    lines = grep_lines(files, search)
    replaced_lines = sed_replace(lines, search, replace)
    get_count_report(replaced_lines, top)



if __name__ == "__main__":
    run_pipeline()
    #files = gen_files('../*/*py')
    #lines = grep_lines(files, '^import ')
    #replaced_lines = sed_replace(lines, 'import ', '')
    #get_count_report(replaced_lines)

'''
$ python challenge_11.py --help
Usage: challenge_11.py [OPTIONS]

Options:
  -p, --path TEXT     [required]
  -s, --search TEXT   [default: ^import ]
  -r, --replace TEXT  [default: ]
  -t, --top INTEGER
  --help              Show this message and exit.


$ python challenge_11.py --path "../*/*/*py"
    6 re
    2 itertools
    2 string
    1 feedparser
    1 calendar
    1 json
    1 requests
    1 argparse
    1 decimal
    1 xml.etree.ElementTree as ET
    1 secrets


$ python challenge_11.py --path "../*/*/*py" --top 5
    6 re
    2 itertools
    2 string
    1 feedparser
    1 calendar
'''
