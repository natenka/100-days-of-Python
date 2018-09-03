from datetime import datetime, date, timedelta
import time
import sys
import subprocess
import sqlite3

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
    #for second in range(1, (minutes*60)+1):
    for second in range(1, (minutes)+1): #test run
        time.sleep(1)
        now = datetime.now().replace(microsecond=0)
        sys.stdout.write(f"\r{message}: {now-start}")
        sys.stdout.flush()
    print()


def sets_of_pomodoros(podomoros_todo: list, set_size: int):
    for idx in range(0, len(podomoros_todo), set_size):
        yield podomoros_todo[idx: idx + set_size]


def run_pomodoro(pomodoro_num: int, work_minutes: int = 25):
    start = datetime.now()
    interupted = 0
    app_log.info(f"Pomodoro {pomodoro_num} started")
    print_green("It's time to work!")
    print_green(f"Pomodoro {pomodoro_num}")
    try:
        run_timer_with_live_stdout_update(work_minutes, "Work")
    except KeyboardInterrupt:
        interupted = 1
        stop_session = input('\n\nStop entire session? [y/n] ')
        if stop_session == 'y':
            raise KeyboardInterrupt
        print()
    print_green(next(stats))
    print_yellow("How productive was this pomodoro?")
    productivity = input("Productivity level (percents): ")
    app_log.info(f"Pomodoro {pomodoro_num} finished. Productivity level: {productivity}")
    return (start, datetime.now(), productivity, interupted)


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
    pomodoro_set_stats = []
    for idx, pomodoro_num in enumerate(pomodoro_set, 1):
        pomodoro_set_stats.append(run_pomodoro(pomodoro_num, work_minutes))
        if pomodoro_num == set_size:
            take_a_long_break(long_break)
            break
        if not pomodoro_num == pomodoro_set[-1]:
            take_a_short_break(short_break)
    return pomodoro_set_stats


def update_session_stats(session_stats):
    while session_stats['todo'] != 0:
        session_stats['todo'] -= 1
        session_stats['done'] += 1
        if session_stats['todo']:
            yield f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}"
        else:
            yield f"Good job! All {session_stats['done']} pomodoros done!"


def write_session_stats(db_name, start, end, planned, done):
    connect = sqlite3.connect(db_name)
    with connect:
        query = 'insert into sessions values (?, ?, ?, ?)'
        connect.execute(query, (start, end, planned, done))

def write_pomodoro_stats(db_name, session_start_time, data):
    connect = sqlite3.connect(db_name)
    with connect:
        query = 'insert into pomodoros values (?, ?, ?, ?, ?)'
        for row in data:
            connect.execute(query, row + (session_start_time,))


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
    session_start = datetime.now()
    global stats
    stats = update_session_stats(session_stats)

    clearscreen()

    pomodoros_stats = []
    all_pomodoros = list(range(1, pomodoros_to_run+1))
    pomodoro_sets = sets_of_pomodoros(all_pomodoros, set_size)
    app_log.info(f"Pomodoro session started")
    try:
        for pomo_set in pomodoro_sets:
            pomodoros_stats.extend(
                run_pomodoro_set(pomo_set, work_minutes, short_break, long_break))
    except KeyboardInterrupt:
        print_red("\n\nBye!")
        app_log.info("Session interupted")
    else:
        app_log.info(f"Pomodoro session finished")
    app_log.info(f"Session stats: {session_stats}")
    write_session_stats(database, start=session_start, end=datetime.now(),
                        planned=pomodoros_to_run, done=session_stats['done']) #TODO: done pomodoros
    write_pomodoro_stats(database, session_start_time=session_start, data=pomodoros_stats)



if __name__ == "__main__":
    database = 'pomodoros_stats.db'
    level = logbook.TRACE
    app_log = logbook.Logger('App')
    #logbook.StreamHandler(sys.stdout, level=level).push_application()
    logbook.TimedRotatingFileHandler("pomodoro.log", level=level).push_application()

    pomodoro()


'''
sqlite> select * from sessions;
start_time                  end_time                    planned     done
--------------------------  --------------------------  ----------  ----------
2018-09-03 18:55:50.745359  2018-09-03 18:56:49.614284  2           0
2018-09-03 19:18:02.481014  2018-09-03 19:19:19.720039  5           5
2018-09-03 19:20:41.651539  2018-09-03 19:21:06.049601  2           2
2018-09-03 19:21:51.010325  2018-09-03 19:23:27.122094  5           5
2018-09-03 19:23:55.573195  2018-09-03 19:24:51.739044  5           4
2018-09-03 19:27:31.418792  2018-09-03 19:27:39.011671  5           0
2018-09-03 19:27:58.841099  2018-09-03 19:28:04.043831  5           0
2018-09-03 19:28:08.519302  2018-09-03 19:29:03.692148  5           1
2018-09-03 19:32:08.339595  2018-09-03 19:33:09.622581  5           5
sqlite>
sqlite>
sqlite> select * from pomodoros;
start_time                  end_time                    productivity  interupted  session_id
--------------------------  --------------------------  ------------  ----------  --------------------------
2018-09-03 19:20:41.653701  2018-09-03 19:20:53.424761  90            0           2018-09-03 19:20:41.651539
2018-09-03 19:20:54.426738  2018-09-03 19:21:06.049371  100           0           2018-09-03 19:20:41.651539
2018-09-03 19:21:51.013705  2018-09-03 19:22:25.625629  100           0           2018-09-03 19:21:51.010325
2018-09-03 19:22:26.626808  2018-09-03 19:22:38.721171  90            0           2018-09-03 19:21:51.010325
2018-09-03 19:22:39.723688  2018-09-03 19:22:52.194089  90            0           2018-09-03 19:21:51.010325
2018-09-03 19:22:53.195336  2018-09-03 19:23:05.521675  85            0           2018-09-03 19:21:51.010325
2018-09-03 19:23:15.533330  2018-09-03 19:23:27.121959  100           0           2018-09-03 19:21:51.010325
2018-09-03 19:32:08.342102  2018-09-03 19:32:14.877438  100           1           2018-09-03 19:32:08.339595
2018-09-03 19:32:15.878691  2018-09-03 19:32:26.797554  80            0           2018-09-03 19:32:08.339595
2018-09-03 19:32:27.797828  2018-09-03 19:32:34.741511  20            1           2018-09-03 19:32:08.339595
2018-09-03 19:32:35.742705  2018-09-03 19:32:46.693529  90            0           2018-09-03 19:32:08.339595
2018-09-03 19:32:56.704221  2018-09-03 19:33:09.622371  90            0           2018-09-03 19:32:08.339595
'''
