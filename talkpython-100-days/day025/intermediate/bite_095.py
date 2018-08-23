'''
In this Bite you will subclass the dict built-in to support a birthday dictionary.

This dictionary takes names as keys and birthday dates as values. Implement the __setitem__ dunder method to print a message every time somebody gets added with a birthday that is already in the dictionary. It should work like this when running it in the REPL:

from datetime import date
from bdaydict import BirthdayDict
bd = BirthdayDict()
bd['bob'] = date(1987, 6, 15)
bd['tim'] = date(1984, 7, 15)
bd['mary'] = date(1987, 6, 15)  # whole date match
  Hey mary, there are more people with your birthday!

bd['sara'] = date(1987, 6, 14)
bd['mike'] = date(1981, 7, 15)  # day + month match
  Hey mike, there are more people with your birthday!
So if day and month are the same, you have a match, the year can be different. Use MSG to print the message, string replacing it with the name key of the newly added person.

Note that this exercise is to get you thinking about subclasses and extending built-in behavior. There is a caveat though: the code of the built-ins (written in C) does not call special methods overriden by user-defined classes (source: Fluent Python), so use this with caution.

Good luck and have fun!
'''
MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        filter_bd = [bd for bd in self.values() if bd.day == birthday.day and bd.month == birthday.month]
        if filter_bd: print(MSG.format(name))
        super().__setitem__(name, birthday)
