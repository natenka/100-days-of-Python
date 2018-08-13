import random



class Roll:
    def __init__(self, roll=None):
        self.roll_map = {
            'rock': {'rock': 'draw', 'paper': 'lose', 'scissors': 'win'},
            'paper': {'rock': 'win', 'paper': 'draw', 'scissors': 'lose'},
            'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'draw'}}
        if not roll:
            self.roll = random.choice(list(self.roll_map.keys()))
        else:
            self.roll = roll

    def can_defeat(self, other):
        return self.roll_map[self.roll][other.roll]

    def defeated_by(self):
        return [r for r in self.roll_map[self.roll] if self.roll_map[r] == 'win']

    def __repr__(self):
        return f"Roll({self.roll})"


class Player:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Player({self.name})"


def print_header():
    print('---------------------------------')
    print('------ Rock Paper Scissors ------')
    print('---------------------------------')


def build_the_three_rolls():
    return [Roll() for _ in range(3)]

def get_players_name():
    return input('Enter your name: ')


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    results = []
    count = 0
    while count < 3:
        p2_roll = random.choice(rolls) # TODO: get random roll
        p1_roll = Roll(input('Make your roll: ')) # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)
        results.append(outcome)

        # display throws
        print(f'Player {player1} roll: {p1_roll}')
        print(f'Player {player2} roll: {p2_roll}')
        # display winner for this round
        print(f'Result: {player1} {outcome} {player2}\n')

        count += 1

    # Compute who won
    if results.count('win') > results.count('lose'):
        print(f'{player1} winned')
    elif results.count('win') ==  results.count('lose'):
        print('Draw')
    else:
        print(f'{player1} lose')

if __name__ == "__main__":
    main()
