#TODO
#live view timer
#info in shell prompt about time
#notification about break

import argparse
from datetime import datetime, date, timedelta
import time


def sets_of_pomodoros(podomoros_todo: list, set_size: int):
    for idx in range(0, len(podomoros_todo), set_size):
        yield podomoros_todo[idx: idx + set_size]


def run_one_pomodoro(pomodoro_num: int, work_minutes: int = 25):
    print('Pomodoro', pomodoro_num)
    time.sleep(2)


def take_a_short_break(short_break: int = 5):
    print(f'Short break for {short_break} minutes')
    time.sleep(1)


def take_a_long_break(long_break: int = 30):
    print(f'Long break for {long_break} minutes')
    time.sleep(10)


def run_pomodoro_set(pomodoro_set: list, work_minutes: int = 25, short_break: int = 5,
                     long_break: int = 30):
    for pomodoro_num in pomodoro_set:
        run_one_pomodoro(pomodoro_num, work_minutes)
        if pomodoro_num == pomodoro_set[-1]:
            take_a_long_break(long_break)
            break
        take_a_short_break(short_break)



def pomodoro(pomodoros_to_run: int = 4, work_minutes: int = 25, short_break: int = 5,
             long_break: int = 30, set_size: int = 4):
    now = datetime.now()
    all_pomodoros = list(range(1, pomodoros_to_run+1))
    pomodoro_sets = sets_of_pomodoros(all_pomodoros, set_size)
    for pomo_set in pomodoro_sets:
        run_pomodoro_set(pomo_set, work_minutes, short_break, long_break)


if __name__ == "__main__":
    pomodoro(pomodoros_to_run=8)
