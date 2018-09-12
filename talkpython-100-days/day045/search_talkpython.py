from pprint import pprint

from tabulate import tabulate
import requests
import click


def search_talkpython_api(keyword):
    link = 'http://search.talkpython.fm/api/search?q={}'
    resp = requests.get(link.format(keyword.replace(' ', '-')))
    resp.raise_for_status()

    results = resp.json()
    episodes = {int(ep['id']): ep['title']
                for ep in results['results'] if ep['category'] == 'Episode'}
    return episodes


@click.command()
@click.argument('keyword')
@click.option('--table', is_flag=True)
def show_result(keyword, table):
    result = search_talkpython_api(keyword)
    print(f'There are {len(result)} matching episodes:')
    if table:
        print(tabulate(result.items(),
                       showindex=range(1, len(result)+1),
                       headers=('Index', 'Show number', 'Title')))
    else:
        for idx, (number, title) in enumerate(result.items(), 1):
            print(f'{idx}. {title}')


if __name__ == "__main__":
    show_result()
