from datetime import datetime, date, timedelta
import time
import sys
import subprocess

import click
import logbook


def clearscreen():
    subprocess.run('clear')


def colored_print(message, color):
    click.echo(click.style(message, fg=color, bold=True))


def print_green(message):
    colored_print(message, "green")


def print_red(message):
    colored_print(message, "red")


def print_yellow(message):
    colored_print(message, "yellow")


def run_timer_with_live_stdout_update(minutes: int, message: str):
    start = datetime.now().replace(microsecond=0)
    for second in range(1, (minutes*60)+1):
    #for second in range(1, (minutes)+1): #test run
        time.sleep(1)
        now = datetime.now().replace(microsecond=0)
        sys.stdout.write(f"\r{message}: {now-start}")
        sys.stdout.flush()
    print()


def sets_of_pomodoros(podomoros_todo: list, set_size: int):
    for idx in range(0, len(podomoros_todo), set_size):
        yield podomoros_todo[idx: idx + set_size]


def run_pomodoro(pomodoro_num: int, work_minutes: int = 25):
    app_log.info(f"Pomodoro {pomodoro_num} started")
    print_green("It's time to work!")
    print_green(f"Pomodoro {pomodoro_num}")
    run_timer_with_live_stdout_update(work_minutes, "Work")
    print_green(next(stats))
    print_yellow("How productive was this pomodoro?")
    productivity = input("Productivity level (percents): ")
    app_log.info(f"Pomodoro {pomodoro_num} finished. Productivity level: {productivity}")


def take_a_short_break(short_break: int = 5):
    print('#'*40)
    print_yellow(f'Short break for {short_break} minutes')
    run_timer_with_live_stdout_update(short_break, 'Short break')
    print('#'*40)


def take_a_long_break(long_break: int = 30):
    print('#'*40)
    print(f'Long break for {long_break} minutes')
    run_timer_with_live_stdout_update(long_break, 'Long break')
    print('#'*40)


def run_pomodoro_set(pomodoro_set: list, work_minutes: int = 25, short_break: int = 5,
                     long_break: int = 30, set_size: int = 4):
    app_log.info(f"Starting Pomodoro set: {len(pomodoro_set)} pomodoros, {work_minutes} minutes each")
    for idx, pomodoro_num in enumerate(pomodoro_set, 1):
        run_pomodoro(pomodoro_num, work_minutes)
        if pomodoro_num == set_size:
            take_a_long_break(long_break)
            break
        if not pomodoro_num == pomodoro_set[-1]:
            take_a_short_break(short_break)


def update_session_stats(session_stats):
    while session_stats['todo'] != 0:
        session_stats['todo'] -= 1
        session_stats['done'] += 1
        if session_stats['todo']:
            yield f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}"
        else:
            yield f"Good job! All {session_stats['done']} pomodoros done!"


@click.command()
@click.option('--pomodoros_to_run', '-r', default=5, show_default=True, type=int)
@click.option('--work_minutes', '-w', default=25, show_default=True, type=int)
@click.option('--short_break', '-s', default=5, show_default=True, type=int)
@click.option('--long_break', '-l', default=30, show_default=True, type=int)
@click.option('--set_size', '-p', default=4, show_default=True, type=int,
              help='Number of pomodoros before a long break')
def pomodoro(pomodoros_to_run: int = 5, work_minutes: int = 25, short_break: int = 5,
             long_break: int = 30, set_size: int = 4):
    session_stats = {'total': pomodoros_to_run, 'done': 0, 'todo': pomodoros_to_run}
    global stats
    stats = update_session_stats(session_stats)

    clearscreen()
    all_pomodoros = list(range(1, pomodoros_to_run+1))
    pomodoro_sets = sets_of_pomodoros(all_pomodoros, set_size)
    app_log.info(f"Pomodoro session started")
    try:
        for pomo_set in pomodoro_sets:
            run_pomodoro_set(pomo_set, work_minutes, short_break, long_break)
    except KeyboardInterrupt:
        print_red("\n\nBye!")
        app_log.info("Session interupted")
    else:
        app_log.info(f"Pomodoro session finished")
    app_log.info(f"Session stats: {session_stats}")


if __name__ == "__main__":
    level = logbook.TRACE
    app_log = logbook.Logger('App')
    #logbook.StreamHandler(sys.stdout, level=level).push_application()
    logbook.TimedRotatingFileHandler("pomodoro.log", level=level).push_application()

    pomodoro()
