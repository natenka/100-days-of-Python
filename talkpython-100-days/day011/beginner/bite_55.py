from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    result = []
    data = feedparser.parse(FEED_URL)
    for info in data['entries']:
        title = info['title']
        link = info['link']
        result.append(Game(title, link))
    return result
