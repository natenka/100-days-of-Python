'''
Let's get some more practice with decorators ... in this Bite you will write a decorator that checks if input arguments (*args *1) are positive integers. If one or more of the passed in args are not of type int, it throws a TypeError, if it is an int but < 0, it throws a ValueError.

That's it! Wrap it in a nice decorator and the tests will validate your code. Have fun!
'''
from functools import wraps


def int_args(func):
    @wraps(func)
    def inner(*args):
        ints = [isinstance(i, int) for i in args]
        if not all(ints):
            raise TypeError
        if not all(i > 0 for i in args):
            raise ValueError
        return func(*args)
    return inner



