'''
The Tim Ferriss Show is full of wisdom and inspiration. It can also fill up your book shelves because a lot of awesome titles get recommended.

This raises the question: which books to prioritise? We found this list but for some the Top Books (2 or more mentions) might still be daunting!

Luckily we are PyBites Ninjas so what if we use some BeautifulSoup to scrape this site (we'll use a static copy) for the books that are at the top of this Top Books list.

Complete get_top_books below to find the number (limit) of books we could prioritise. Not surprisingly Sapiens is one of them :)
'''

from collections import Counter
from pprint import pprint

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
TIM_BLOG = 'https://bit.ly/2NBnZ6P'


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()
    c = Counter()

    soup = BeautifulSoup(content, 'html.parser')
    books = [link.text for link in soup.find_all('a') if 'amazon' in link['href']]
    return [name for name, count in Counter(books).most_common(limit)]


'''
[('Man’s Search For Meaning', 6),
 ('Tao Te Ching', 5),
 ('The 4-Hour Workweek: Escape the 9-5, Live Anywhere and Join the New Rich',
  4),
 ('The Fountainhead', 4),
 ('Sapiens: A Brief History of Humankind', 4),
 ('The Better Angels of our Nature: Why Violence Has Declined', 3),
 ('The Beginning of Infinity: Explanations That Transform the World', 3),
 ('The War of Art: Break Through the Blocks and Win Your Inner Creative '
  'Battles',
  3),
 ('The Hero with a Thousand Faces ', 3),
 ('Poor Charlie’s Almanack', 3),
 ('The Chronicles of Narnia', 3),
 ('The Selfish Gene', 3),
 ('Tools of Titans', 3),
 ('Song of Solomon', 3),
 ('The Alchemist', 3),
 ('Mastery: The Keys to Success and Long-Term Fulfillment ', 2),
 ('Finite and Infinite Games', 2),
 ('Zen Mind, Beginner’s Mind', 2),
 ('Surely You’re Joking, Mr. Feynman!', 2),
 ('Atlas Shrugged', 2),
 ('The Bible', 2),
 ('Dune', 2),
 ('The Power of a Positive No: How to Say No and Still Get to Yes', 1),
 ('The Open Society and Its Enemies', 1),
 ('The Singularity Is Near', 1),
 ('The Autobiography of Malcolm X', 1),
 ('The Rational Optimist: How Prosperity Evolves', 1),
 ('Last Exit to Brooklyn ', 1),
 ('Requiem for a Dream', 1),
 ('Passages: Predictable Crises of Adult Life', 1)]
'''
