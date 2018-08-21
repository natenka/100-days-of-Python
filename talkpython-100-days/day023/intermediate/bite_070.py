'''
In this Bite you make an iterator called EggCreator by implementing the __iter__ and __next__ dunder methods (as dictated by the iterator protocol).

Have it receive an int called limit which is the max number of eggs to create. It then generates eggs of randomly chosen colors from the COLORS constant.

Make sure you raise the right exception when you reach the passed in limit.

So this is how the iterator would work + its output:

for egg in EggCreator(5):
    print(egg)
Would output (colors will vary due to randomness):

green egg
yellow egg
yellow egg
blue egg
red egg
Eggs theme? Yep, this Bite was produced the 31st of March 2018 - Happy Easter all!

Good luck and keep calm and code in Python!
'''

from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit):
        self.start = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.limit:
            raise StopIteration
        else:
            self.start += 1
            return f'{choice(COLORS)} egg'
