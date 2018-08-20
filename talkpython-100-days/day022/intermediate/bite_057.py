'''
Bite 57. Create a simple calculator that receives command line arguments
In this Bite you write a simple calculator that can perform additions (add), subtractions (sub), multiplications (mul) and divisions (div).

You will use argparse to interface with the program. You will make it work like this:

$ python calculator.py -h
usage: calculator.py [-h] [-a ADD [ADD ...]] [-s SUB [SUB ...]]
                     [-m MUL [MUL ...]] [-d DIV [DIV ...]]

A simple calculator

optional arguments:
  -h, --help            show this help message and exit
  -a ADD [ADD ...], --add ADD [ADD ...]
                        Sums numbers
  -s SUB [SUB ...], --sub SUB [SUB ...]
                        Subtracts numbers
  -m MUL [MUL ...], --mul MUL [MUL ...]
                        Multiplies numbers
  -d DIV [DIV ...], --div DIV [DIV ...]
                        Divides numbers


$ python calculator.py --add 1 2 3
6.0
$ python calculator.py --sub 10 6 2
2.0
$ python calculator.py --mul 3 3 3
27.0
$ python calculator.py --div 8 5 7
0.23
See also the TESTS tab for more info. Good luck and have fun ... argparse is a good skill to have!

If new to argparse you might want to check out Bite 56 first. For a more advanced Bite try 58.
'''
import argparse
import operator
from functools import reduce, partial

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    operations_map = {
        'add': partial(reduce, operator.add),
        'sub': partial(reduce, operator.sub),
        'mul': partial(reduce, operator.mul),
        'div': partial(reduce, operator.truediv)}
    return round(operations_map[operation](numbers), 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(description='A simple calculator')
    parser.add_argument('-a', '--add', nargs='+', action="store", dest="add", help='Sums numbers', type=float)
    parser.add_argument('-s', '--sub', nargs='+', action="store", dest="sub", help='Subtracts numbers', type=float)
    parser.add_argument('-m', '--mul', nargs='+', action="store", dest="mul", help='Multiplies numbers', type=float)
    parser.add_argument('-d', '--div', nargs='+', action="store", dest="div", help='Divides numbers', type=float)
    return parser



def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)
