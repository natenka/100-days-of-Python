'''
Danny does not like rote learning (nor do we!). He is asked to remember multiplication tables of considerable size 😭

Can you give him a hand so he can focus on more interesting things again? (OK maybe HE is the one who should learn Python 😂)

Complete the MultiplicationTable class below implementing the following methods:

Use __init__ (constructor) to store the (x,y) coordinates and their multiplication result in a data structure (say in self._table).
__len__ should return the area of the table (len x* len y)
__str__ should give a visual representation of the table, for example a 3x3 length table should return this str:
 1 | 2 | 3
 2 | 4 | 6
 3 | 6 | 9
The calc_cell method should take a x and y coordinate and return the result multiplying them. If x/y are out of range, raise an IndexError.
Good luck and have fun!
'''

class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._table = [[i+j for i in range(1, length+1)] for j in range(length)]
        for i in range(1, length):
            for j in range(1,length):
                self._table[i][j] = self._table[i][0]*self._table[0][j]


    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table) * len(self._table[0])

    def __str__(self):
        """Returns a string representation of the table"""
        return '\n'.join(' | '.join([str(num) for num in line]) for line in self._table)


    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        return self._table[x-1][y-1]


#####answer
from itertools import product

pad = lambda n: f'{n:>3}'  # noqa E731


class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.length = length
        axis = range(1, self.length + 1)
        self._table = {(i, j): i*j
                       for i, j in product(axis, axis)}

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table)

    def __str__(self):
        """Returns a string representation of the table"""
        output = []
        for i, res in enumerate(self._table.values(), 1):
            val = str(res)
            val += i % self.length == 0 and '\n' or ' | '
            output.append(val)
        return ''.join(output)

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        if not (x, y) in self._table:
            raise IndexError
        return x * y

