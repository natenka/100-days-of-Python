#TODO
#break/pomodoro start notification
#click/argparse cli

import argparse
from datetime import datetime, date, timedelta
import time
import sys
import subprocess


def clearscreen():
    subprocess.run('clear')


def run_timer_with_live_stdout_update(minutes: int, message: str):
    start = datetime.now().replace(microsecond=0)
    for minute in range(1, minutes+1):
        time.sleep(1)
        now = datetime.now().replace(microsecond=0)
        sys.stdout.write(f"\r{message}: {now-start}")
        sys.stdout.flush()
    print()


def sets_of_pomodoros(podomoros_todo: list, set_size: int):
    for idx in range(0, len(podomoros_todo), set_size):
        yield podomoros_todo[idx: idx + set_size]


def run_pomodoro(pomodoro_num: int, work_minutes: int = 25):
    print("It's time to work!")
    print('Pomodoro', pomodoro_num)
    run_timer_with_live_stdout_update(work_minutes, 'Work')
    print(next(stats))


def take_a_short_break(short_break: int = 5):
    print('#'*40)
    print(f'Short break for {short_break} minutes')
    run_timer_with_live_stdout_update(short_break, 'Short break')
    print('#'*40)


def take_a_long_break(long_break: int = 30):
    print('#'*40)
    print(f'Long break for {long_break} minutes')
    run_timer_with_live_stdout_update(long_break, 'Long break')
    print('#'*40)


def run_pomodoro_set(pomodoro_set: list, work_minutes: int = 25, short_break: int = 5,
                     long_break: int = 30, set_size: int = 4):
    for idx, pomodoro_num in enumerate(pomodoro_set, 1):
        run_pomodoro(pomodoro_num, work_minutes)
        if pomodoro_num == set_size:
            take_a_long_break(long_break)
            break
        if not pomodoro_num == pomodoro_set[-1]:
            take_a_short_break(short_break)


def pomodoro(pomodoros_to_run: int = 4, work_minutes: int = 25, short_break: int = 5,
             long_break: int = 30, set_size: int = 4):
    session_stats = {'total': pomodoros_to_run, 'done': 0, 'todo': pomodoros_to_run}
    global stats
    stats = update_session_stats(session_stats)

    clearscreen()
    all_pomodoros = list(range(1, pomodoros_to_run+1))
    pomodoro_sets = sets_of_pomodoros(all_pomodoros, set_size)
    for pomo_set in pomodoro_sets:
        run_pomodoro_set(pomo_set, work_minutes, short_break, long_break)


def update_session_stats(session_stats):
    while session_stats['todo'] != 0:
        session_stats['todo'] -= 1
        session_stats['done'] += 1
        if session_stats['todo']:
            yield f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}"
        else:
            yield f"Good job! All {session_stats['done']} pomodoros done!"


if __name__ == "__main__":
    pomodoro(pomodoros_to_run=6, work_minutes=10)

