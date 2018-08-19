from itertools import cycle
import time
import subprocess
import random

import click


ascii_traffic_light = '''
 OOO
OOOOO
 OOO'''


def clearscreen():
    subprocess.run('clear')


def random_sleep(min_sleep=1, max_sleep=4):
    return random.randint(min_sleep, max_sleep)


def lights_cycle():
    lights = {0: 'red', 1: 'yellow', 2: 'green'}
    display_lights = dict.fromkeys(lights.keys(), ascii_traffic_light)

    for idx, light in cycle(lights.items()):
        clearscreen()
        dl = display_lights.copy()
        dl[idx] = click.style(ascii_traffic_light, fg=light, bold=True)
        print(''.join(dl.values()))
        time.sleep(random_sleep())


if __name__ == "__main__":
    try:
        lights_cycle()
    except KeyboardInterrupt:
        print('\nBye!')


