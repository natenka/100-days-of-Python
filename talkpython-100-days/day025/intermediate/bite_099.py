'''
Write a generator that produces the sequence [1, 'A', 2, 'B', 3, 'C', ... 'X', 25, 'Y', 26, 'Z'] infinitely. So once you hit Z you start at 1 again, etc. Maybe itertools can help you here? Have fun!
'''

from itertools import cycle
import string


def sequence_generator():
    numbers = cycle(range(1, len(string.ascii_uppercase) + 1))
    letters = cycle(ascii_uppercase)

    for number, letter in zip(numbers, letters):
        yield number
        yield letter
