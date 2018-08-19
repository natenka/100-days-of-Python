'''
In this Bite you will create a deck of Uno cards. Here is the equipment requirement as described here - use the same card names as in bold here:

There are 108 cards in a Uno deck. There are four suits, Red, Green, Yellow and Blue, each consisting of one 0 card, two 1 cards, two 2s, 3s, 4s, 5s, 6s, 7s, 8s and 9s; two Draw Two cards; two Skip cards; and two Reverse cards. In addition there are four Wild cards and four Wild Draw Four cards.
Complete create_uno_deck using the provided UnoCard namedtuple and returning the deck as a list. Have fun!
'''
from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_suit(suit):
    pairs = dict.fromkeys(list(range(1, 10)) + ['Draw Two', 'Skip', 'Reverse'], 2)
    cards = {'0':1, **pairs}
    suit_cards = []
    for card_name, num in cards.items():
        suit_cards.append([UnoCard(suit, card_name) for _ in range(num)])
    return suit_cards


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    result = []
    for suit in SUITS:
        result.extend(create_suit(suit))

    #In addition there are four Wild cards and four Wild Draw Four cards.
    for _ in range(4):
        result.append(UnoCard(None, 'Wild'))
        result.append(UnoCard(None, 'Wild Draw Four'))
    return result
