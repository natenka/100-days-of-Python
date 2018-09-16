from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    book_image = soup.find('div', {'class': 'dotd-main-book-image'})
    link = book_image.find('a').get('href')
    image = book_image.find('img').get('src')

    book_main = soup.find('div', {'class': 'dotd-main-book-summary'})
    title_div = book_main.find('div', {'class': 'dotd-title'})
    title = title_div.find('h2').text.strip()
    descr_div = title_div.find_next_sibling("div")
    description = descr_div.text.strip()

    return Book(title, description, image, link)

print(get_book())
