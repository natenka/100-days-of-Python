import random
import csv
from pprint import pprint


def read_battle_table(filename):
    roll_map = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            attack_by = str.lower(row['Attacker'])
            del row['Attacker']
            roll_map[attack_by] = {key.lower(): value for key, value in row.items()}
    return roll_map


class Roll:
    def __init__(self, roll=None, battle_table_file='battle-table.csv'):
        self.roll_map = read_battle_table(battle_table_file)
        if not roll:
            self.roll = random.choice(list(self.roll_map.keys()))
        else:
            self.roll = roll.lower()

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


def build_the_rolls(number_of_rolls):
    return [Roll() for _ in range(number_of_rolls)]


def get_players_name():
    return input('Enter your name: ')


def main(loop_count=3):
    print_header()

    rolls = build_the_rolls(loop_count)

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls, loop_count=loop_count)


def game_loop(player1, player2, rolls, loop_count=3):
    results = []

    for _ in range(loop_count):
        p2_roll = random.choice(rolls)
        p1_roll = Roll(input('Make your roll: '))

        outcome = p1_roll.can_defeat(p2_roll)
        results.append(outcome)

        # display throws
        print(f'Player {player1} roll: {p1_roll}')
        print(f'Player {player2} roll: {p2_roll}')
        # display winner for this round
        print(f'Result: {player1} {outcome} {player2}\n')


    # Compute who won
    if results.count('win') > results.count('lose'):
        print(f'{player1} winned')
    elif results.count('win') ==  results.count('lose'):
        print('Draw')
    else:
        print(f'{player1} lose')

if __name__ == "__main__":
    #pprint(read_battle_table('battle-table.csv'))
    main(5)
