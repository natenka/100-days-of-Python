'''
After Bite 19. Write a simple property let's write a more advanced one.

In this Bite you are presented with a NinjaBelt class that keeps track of scores and Ninja Belts earned (a very real scenario). Some setup code has been provided like the _score and _last_earned_belt variables and the getter and setter methods that make up the property.

The goal is to write a property called score that does the following:

Make sure it can only be assigned an integer,
It can not be assigned a score lower than the current score,
It checks in BELTS if a new belt was earned (for example going from 49 to 50 you earn the yellow belt), if so it stores it in self._last_earned_belt.
For each new score print a message:
If a new badge was earned: Congrats, you earned {score} points obtaining the PyBites Ninja {rank} Belt
Else just the new score: Set new score to {score}
See the TESTS tab for more info. Good luck, have fun and keep calm and code in Python!
'''
from itertools import takewhile

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


def current_belt(user_score):
    if user_score < scores[0]:
        return None
    belts = takewhile(lambda x: x[0] <= user_score, BELTS.items())
    return list(belts)[-1][1]


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None
        self.belts_map = dict(zip(ranks, scores))


    def _get_belt(self, new_score):
        """Might be a useful helper"""
        pass

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        try:
            new_score = int(new_score)
        except ValueError:
            raise ValueError
        if new_score < self._score:
            raise ValueError
        self._score = new_score
        belt = current_belt(new_score)
        if belt and self._last_earned_belt:
            if self.belts_map[belt] > self.belts_map[self._last_earned_belt]:
                self._last_earned_belt = belt
                print(f'Congrats, you earned {self._score} points '
                      f'obtaining the PyBites Ninja {self._last_earned_belt} Belt')
            else:
                print(f'set new score to {self._score}')
        else:
            print(f'set new score to {self._score}')

    score = property(_get_score, _set_score)
