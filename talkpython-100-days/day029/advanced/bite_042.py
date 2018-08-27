import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False


    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        guess = input(f'Guess a number between {START} and {END}: ')
        if not guess:
            raise ValueError('Please enter a number')
        try:
            guess = int(guess)
        except ValueError:
            raise ValueError('Should be a number')

        if not guess in range(START, END+1):
            raise ValueError('Number not in range')
        if guess in self._guesses:
            raise ValueError('Already guessed')
        self._guesses.add(guess)
        return guess

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too low
           Return a boolean"""
        if guess == self._answer:
            print(f"{guess} is correct!")
            return True
        elif guess > self._answer:
            print(f"{guess} is too high")
            return False
        elif guess < self._answer:
            print(f"{guess} is too low")
            return False


    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        for _ in range(MAX_GUESSES):
            while True:
                try:
                    guess = self.guess()
                except ValueError as err:
                    print(err)
                else:
                    break
            if self._validate_guess(guess):
                print(f"It took you {len(self._guesses)} guesses")
                self._win = True
                break
        if not self._win:
            print(f"Guessed {MAX_GUESSES} times, answer was {self._answer}")


if __name__ == '__main__':
    game = Game()
    #game()

    game = Game()
    # good
    g = game.guess()
    assert g == 11
    g = game.guess()
    assert g == 12
    # not a number
    game.guess()
    # already guessed 12
    game.guess()
