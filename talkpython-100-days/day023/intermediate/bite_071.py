'''
In this Bite you write a small class to keep track of the max score in a game. It keeps an internal scores list and when called as a function it receives a new score and returns the max score.

So calling it like this:

record = RecordScore()
print(record(10))
print(record(9))
print(record(11))
print(record(7))
.. would give the following outputs (11 becomes the new max score):

10
10
11
11
To achieve this implement the __call__ dunder (special) method on the RecordScore class. Good luck!
'''

class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.maximum = 0

    def __call__(self, number):
        self.maximum = max(self.maximum, number)
        return self.maximum

record = RecordScore()
print(record(10))
print(record(9))
print(record(11))
print(record(7))

