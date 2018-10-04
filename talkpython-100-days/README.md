---
permalink: /100daysofpython/
title: "100 Days of Python"
comments: true
share: true
tags:
 - python
 - 100daysofpython
 - 100daysofx
---

Предыдущую попытку я забросила, хотя саму учебу нет. Недавно купила bundle курсов от Talk Python и решила пройти их курс [#100DaysOfCode in Python](https://training.talkpython.fm/courses/explore_100days_in_python/100-days-of-code-in-python).
Курс прохожу и для себя, чтобы немного размяться, плюс для того чтобы можно было с чистой совестью рекомендовать его всем желающим.

Даже после беглого просмотра могу сказать, что все здорово организовано, а подробней напишу уже как пройду курс чуть дальше.

## Базовые правила 100 Days of Code с небольшими изменениями

* Каждый день уделять изучению Python 1 час
* Хотя бы половина времени должны тратиться на код (в идеале час в день)
* После каждой сессии коротко описать прогресс и что именно я делала в этот день
* В репозитории каждый день должен быть хотя бы один коммит
* Можно прогулять один день в неделю, но нельзя два дня подряд
* Все прогулы не учитываются



## Day 1: July 30, 2018

В курсе все разделено на темы и на каждую тему выделено по 3 дня:

* 1 день - теория
* 2 день - задачки и практика
* 3 день - продолжение практики

За сегодня я посмотрела видео первого дня, сделала [задачки за второй день и начала задачку из третьего](https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/01-03-datetimes).
Начала делать свой pomodoro timer и пока сделала [костяк скрипта](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day001/pomodoro_timer.py), а завтра уже буду добавлять реальную работу. Если успею, завтра также добавлю интерфейс для вызова скрипта в командной строке, но пока не решила делать его с argparse (его я знаю и будет проще) или с click (пробовала только пару раз).

Time:

* 30 минут видео
* 1 час 10 минут код

## Day 2: July 31, 2018

Сегодня продолжаю работать над таймером pomodoro. Он уже [вполне рабочий](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day002/pomodoro_timer.py), хотя пока запускаю всё в секундах, вместо минут. Это легко меняется, достаточно будет изменить только одну функцию в финальной версии.

В целом всё уже работает, но ещё остается добавить интерфейс в cli с argparse или click. Пока что склоняюсь к click, так как его я знаю намного хуже.

Пример выполнения скрипта (записан с помощью [termtosvg](https://github.com/nbedos/termtosvg)):

<img src="https://cdn.rawgit.com/natenka/100-days-of-Python/7fd02998/talkpython-100-days/day002/pomodoro_timer_run_animation.svg" width="800">

Time: 1 час 30 минут код

## Day 3: August 1, 2018

Завершила работу над [таймером Pomodoro](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day003/pomodoro_timer.py). Сегодня добавила интерфейс командной строки. Остановилась на click.
Теперь все параметры можно указывать при вызове скрипта.

Пока оставила на будущее оповещения и обошлась добавлением цвета в вывод. Плюс теперь таймер уже полноценно работает по минутам, а не секундам.

Пример выполнения скрипта с секундными интервалами (записан с помощью [termtosvg](https://github.com/nbedos/termtosvg)):

<img src="https://cdn.rawgit.com/natenka/100-days-of-Python/9cbc94c6/talkpython-100-days/day003/pomodoro_timer_run_animation.svg" width="800">

Time: 1 час 20 минут код

## Day 4: August 2, 2018

Начала следующую [тройку дней](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/04-06-collections/collections.ipynb), тема - модуль collections.
Посмотрела лекции и сделала задание [Code Challenge 13 - Highest Rated Movie Directors](https://pybit.es/codechallenge13.html). Задание в целом простое, но соображаю я сегодня хуже, чем обычно, так что времени ушло больше.

Следующие два дня буду заниматься разбором логов FCC с информацией о том, кто был на лекции онлайн. В итоге хочу получить сводку с информацией о том, кто ходит на лекции чаще всего.

Time:

* 15 минут видео
* 2 часа код

## Day 5: August 3, 2018

Сегодня занималась вечером, так что вместо намеченного скрипта делала задачки [Bites of Py](https://codechalleng.es/bites/). Решила делать все с самого начала, так что пока сделала intro и пару beginner.

Time: 1 час код

## Day 6: Aug 4, 2018

За сегодня написала скрипт, который парсит отчет [FCC](https://www.freeconferencecall.com). Слушатели  могут подключаться к лекции несколько раз и тогда в отчете они тоже видны несколько раз. Я обработала записи и собрала вместе информацию о каждом слушателе.
Позже в курсе будут темы связанный со скарпингом HTML страниц, так что отложила этот аспект на потом.
Возможно, в следующие дни займусь сбором информации из нескольких отчетов и сводной статистикой по посещению лекций онлайн.

На данный момент скрипт из такого отчета:
```
Caller,Service Type,Start Date and Time,End Date and Time,Duration
jane@example.com - Jane Austen,VoIP,2018-07-01 09:49:33 +0300,2018-07-01 13:16:09 +0300,207m
markt@example.com - Mark Twain,VoIP,2018-07-01 09:57:35 +0300,2018-07-01 13:16:10 +0300,199m
charles.dickens@example.com - Charles Dickens,VoIP,2018-07-01 10:00:10 +0300,2018-07-01 13:00:21 +0300,180m
Homer,VoIP,2018-07-01 12:37:06 +0300,2018-07-01 13:16:11 +0300,40m
william@example.com - William Shakespeare,VoIP,2018-07-01 09:58:10 +0300,2018-07-01 13:16:12 +0300,198m
dumas1802@example.com - Alexandre Dumas,VoIP,2018-07-01 09:51:18 +0300,2018-07-01 13:16:12 +0300,205m
Jules.Verne@example.com - Jules Verne,VoIP,2018-07-01 09:58:13 +0300,2018-07-01 13:16:12 +0300,198m
dumas1802@example.com - Alexandre Dumas,VoIP,2018-07-01 13:18:28 +0300,2018-07-01 13:21:32 +0300,3m
charles.dickens@example.com - Charles Dickens,VoIP,2018-07-01 13:00:20 +0300,2018-07-01 13:16:11 +0300,16m

```

Генерирует такую таблицу
```
name                 email                          duration  first seen           last seen
-------------------  ---------------------------  ----------  -------------------  -------------------
Alexandre Dumas      dumas1802@example.com               208  2018-07-01 09:51:18  2018-07-01 13:21:32
Jane Austen          jane@example.com                    207  2018-07-01 09:49:33  2018-07-01 13:16:09
Mark Twain           markt@example.com                   199  2018-07-01 09:57:35  2018-07-01 13:16:10
William Shakespeare  william@example.com                 198  2018-07-01 09:58:10  2018-07-01 13:16:12
Jules Verne          Jules.Verne@example.com             198  2018-07-01 09:58:13  2018-07-01 13:16:12
Charles Dickens      charles.dickens@example.com         196  2018-07-01 10:00:10  2018-07-01 13:16:11
Homer                                                     40  2018-07-01 12:37:06  2018-07-01 13:16:11
```

Time: 3 часа код

## Day 7: Aug 5, 2018

Сегодня только лекции. Посмотрела лекции по 7 дню и начала смотреть курс [Write Pythonic Code Like a Seasoned Developer](https://training.talkpython.fm/courses/explore_pythonic_code/write-pythonic-code-like-a-seasoned-developer)

Time: 1.5 часа лекции

## Day 8: Aug 6, 2018

Решила 4 задачки [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day008)

Time: 50 минут код

## Day 9: Aug 7, 2018

Решила 9 задачек [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day009) и продолжаю слушать курс [Write Pythonic Code Like a Seasoned Developer](https://training.talkpython.fm/courses/explore_pythonic_code/write-pythonic-code-like-a-seasoned-developer).

Time:

* 1 час видео
* 1.5 часа код

## Day 10: Aug 8, 2018

Сегодня только лекции.

Time: 1 час лекции

## Day 11: Aug 9, 2018

Решила 6 задачек [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day011)

Time: 1 час код

## Day 12: Aug 10, 2018

Решила 6 задачек [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day012)

Time: 1 час код

## Day 13: Aug 11, 2018

Сегодня только лекции.

Time: 1 час лекции

## Day 14: Aug 12, 2018

Сегодня по курсу сделала задачку с игрой [Rock Paper Scissors](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day14/rock_paper_scissors.py).

Time: 1 час код


## Day 15: Aug 13, 2018

Сегодня сделала задачку по курсу [15-way Rock Paper Scissors](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day015/rock_paper_scissors_15_way.py) и решила 7 задачек [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day015/beginner) (дорешала все beginner).

```
$ python rock_paper_scissors_15_way.py
---------------------------------
------ Rock Paper Scissors ------
---------------------------------
Enter your name: nata
Make your roll: dragon
Player Player(nata) roll: Roll(dragon)
Player Player(computer) roll: Roll(fire)
Result: Player(nata) win Player(computer)

Make your roll: paper
Player Player(nata) roll: Roll(paper)
Player Player(computer) roll: Roll(snake)
Result: Player(nata) lose Player(computer)

Make your roll: rock
Player Player(nata) roll: Roll(rock)
Player Player(computer) roll: Roll(tree)
Result: Player(nata) win Player(computer)

Make your roll: dragon
Player Player(nata) roll: Roll(dragon)
Player Player(computer) roll: Roll(fire)
Result: Player(nata) win Player(computer)

Make your roll: fire
Player Player(nata) roll: Roll(fire)
Player Player(computer) roll: Roll(rock)
Result: Player(nata) lose Player(computer)

Player(nata) winned
```

Time: 1.5 часа код

## Day 16: Aug 14, 2018

Сегодня новая тема [list comprehensions and generators](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/16-18-listcomprehensions-generators/list-comprehensions-generators.ipynb).  Послушала лекции и два часа на код: решила [challenge 11](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day016/challenge_11.py) и [5 задачек intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/6ad4b69b96f94b07873dc4ee0f50dbe0334660da).

Time:

* 15 минут видео
* 2 часа код

## Day 17: Aug 15, 2018

Так как вчера я сделала все что было по темам на три дня, сегодня решаю задачки: [6 задачек intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/fefee6ac5512acbf10f9d3b17e4b34cd45e0baf3).

Time: 1 час 10 минут код

## Day 18: Aug 16, 2018

Сегодня сделала [4 задачки intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/aeb2bd169c1fdb6d97d336faad0fe81916b5ecaa)

Time: 1 час код

## Day 19: Aug 17, 2018

Сегодня сделала 2 задачки, еще одну вроде сделала, но что-то ответ не совпадает.

Time: 1 час код

## Day 20: Aug 18, 2018

Сегодня сделала [1 задачку](https://github.com/natenka/100-days-of-Python/commit/99d8c0be7c0ec1b253d4ebe4cd9a9f7fb738793a) и посмотрела видео по новым темам [itertools](https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/19-21-itertools).

Time:

* 30 минут код
* 30 минут видео

## Day 21: Aug 19, 2018

Сегодня [сделала задачку](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day021/traffic_lights.py) с созданием [светофора](https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/19-21-itertools#day-n1-create-a-traffic-lights-script) и [одну intermediate уровня](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day021/intermediate/bite_060.py)

Пример выполнения скрипта со светофором (записан с помощью [termtosvg](https://github.com/nbedos/termtosvg)):

<img src="https://cdn.rawgit.com/natenka/100-days-of-Python/4cc8aa3a/talkpython-100-days/day021/traffic_lights_animation.svg" width="800">

## Day 22: Aug 20, 2018

Сегодня решила три задачки [intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/0c87743c30d4db3eadc460aa2be635cd92a1cfed).

Time:

* 1 час 20 минут код
* 23 минуты видео

## Day 23: Aug 21, 2018

Сегодня решила пять задачек [intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/e5477c6bfdc348f1f833bc030c091713320a3c02).

Время 1 час 10 минут код

## Day 24: Aug 22, 2018

Сегодня решила 4 задачки [intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/5bfe63009662aad10b01c71a0540853544604155).

Time: 1 час код

## Day 25: Aug 23, 2018

Сегодня решила 6 задачек intermediate уровня.

Time: 1 час 45 минут код

## Day 26: Aug 24, 2018

Сегодня решила [3 задачки intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/93bfa88bdf7c1cd6971edcb4b98ee6b492d46bd5) и посмотрела лекции по теме.

Time:

* 20 минут лекции
* 40 минут код

## Day 27: Aug 25, 2018

Сегодня решила 5 задачек intermediate уровня.

Закончилось самое сложное время - отпуск :) Все дни, как минимум, час занималась и почти каждый день час тратила на код, в основном, решала задачки.

Time: 1 час 20 минут код

## Day 28: Aug 26, 2018

Сегодня решила 2 задачки advanced уровня.

Time: 1 час код

## Day 29: Aug 27, 2018

Сегодня решила 6 задачек advanced уровня.

Получила красивую бумажку :)

<img src="https://pybites-certificates.s3.amazonaws.com/natasha_samoylenko_03efe4d0-821c-42ec-ae70-ab6e31251f7d.png" width="800">

Time: 2 часа код

## Day 30: Aug 28, 2018

Сегодня только лекции

Time: 50 минут лекции

## Day 31: Aug 29, 2018

Сегодня начала следующую тему - логирование. Узнала про [модуль logbook](https://logbook.readthedocs.io/en/stable/).
Добавила базовое [логирование в Pomodoro timer](https://github.com/natenka/100-days-of-Python/commit/0d3388612dcb3d10f3ac28aa45c074638c58bad1) из 3 дня. Завтра продолжу разбираться с logbook

Time:

* 1 час лекции
* 1 час код

## Day 32: Aug 30, 2018

Сегодня решила [2 задачки advanced уровня](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day032/advanced)

Time: 1 час код

## Day 33: Aug 31, 2018

Сегодня только лекции

Time: 1 час лекции

## Day 34: Sep 1, 2018

Сегодня решила [2 задачки intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/d4041445a7f580aa7378e06ce092cdf6fc887bd).

Time: 1 час код

## Day 35: Sep 2, 2018

Сегодня решила [2 задачки intermediate уровня](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day035/intermediate).

Time:

* 40 минут код
* 35 минут лекции

## Day 36: Sep 3, 2018

Последние несколько дней как-то тяжелее заниматься, видимо отчасти потому что вечером кодила, но похоже не только. Сегодня тоже вечером, но хорошо пошло.
А может задачек передозировка :)

Сегодня дополняла свой [pomodoro timer](https://github.com/natenka/100-days-of-Python/commit/ce5f7c35aeb24daf552525a3e8cbd29fe78db4e3): добавила запись статистики в бд, позже будет рассматриваться plotly, вот тогда еще займусь рисованием графиков на основании статистики.

Time: 1 час 20 минут код

## Day 37: Sep 4, 2018

Сегодня только лекции. Кажется загадка разгадана: я просто постепенно сама по себе начала вставать раньше, перехожу к своему нормальному графику и соответственно, раньше хочу спать. И ровно в то время, когда я хочу спать, я сажусь заниматься )
Первые недели я занималась первым делом с утра или днем. Надо опять так делать, а то совсем тяжело заниматься в сонном состоянии.

Time: 1 час лекции

## Day 38: Sep 5, 2018

Сегодня поступила умно и занималась утром - разница огромная. Работала с данными по популярности песен и исполнителей классического рока.
 Было весело :)

Такой [получился скрипт](https://github.com/natenka/100-days-of-Python/commit/d2970433ce2e609bce14c5047d1c14acf41bdc57):
```python
$ python get_best_classic_rock.py --help
Usage: get_best_classic_rock.py [OPTIONS]
Options:
  -c, --category [artist|song]
  -t, --top INTEGER             [default: 10]
  --sort_asc
  --help                        Show this message and exit.


$ python get_best_classic_rock.py -c artist
Artist                           Songs playcount
-----------------------------  -----------------
Led Zeppelin                                1556
Van Halen                                   1243
Rolling Stones                              1143
Pink Floyd                                  1044
Tom Petty & The Heartbreakers                965
AC/DC                                        866
Aerosmith                                    813
ZZ Top                                       712
The Beatles                                  704
Queen                                        694


$ python get_best_classic_rock.py -c song
Name                         Artist          Year    Playcount
---------------------------  ------------  ------  -----------
Dream On                     Aerosmith       1973          142
Sweet Emotion                Aerosmith       1975          141
All Along the Watchtower     Jimi Hendrix    1968          141
You Shook Me All Night Long  AC/DC           1980          138
More Than a Feeling          Boston          1976          134
Carry On Wayward Son         Kansas          1976          134
Peace of Mind                Boston          1976          132
Crazy On You                 Heart           1976          125
Legs                         ZZ Top          1983          121
Sharp Dressed Man            ZZ Top          1983          120
```

Time: 1 час 40 минут код

## Day 39: Sep 6, 2018

Сегодня сделала [скрипт для переноса решения заданий из ветки master в task_check](https://github.com/natenka/100-days-of-Python/commit/1797bc33c257ccff3236e06a6dab358578d37d5c), который снимет одну небольшую рутинную задачу с меня. В проверке заданий  я это использую каждый раз, поэтому он точно пригодится.

Time: 1:20 код

## Day 40: Sep 7, 2018

Сегодня только лекции.

Time: 2:00 лекции

## Day 41: Sep 8, 2018

Сегодня только лекции.

Time: 2:15 лекции

## Day 42: Sep 5, 2018

Сегодня работала с JSON и данными из [OMDb API](http://www.omdbapi.com/). Продолжаю использовать click для cli. Так я больше запоминаю, плюс он мне нравится.

Такой [получился скрипт](https://github.com/natenka/100-days-of-Python/commit/86462fdf1ee2636d68c522a86dfa1e8858cc0482#diff-4fe9ac54e1fddd6659e5197101acaaa7):
```python
$ python get_marvel_stats.py rating
title                      year    rating    runtime      money
-----------------------  ------  --------  ---------  ---------
Avengers: Infinity War     2018       8.7        149  664987816
The Avengers               2012       8.1        143  623279547
Guardians of the Galaxy    2014       8.1        121  270592504
Iron Man                   2008       7.9        126  318298180
Thor: Ragnarok             2017       7.9        130  314971245


$ python get_marvel_stats.py rating --top 10
title                                  year    rating    runtime      money
-----------------------------------  ------  --------  ---------  ---------
Avengers: Infinity War                 2018       8.7        149  664987816
The Avengers                           2012       8.1        143  623279547
Guardians of the Galaxy                2014       8.1        121  270592504
Iron Man                               2008       7.9        126  318298180
Thor: Ragnarok                         2017       7.9        130  314971245
Captain America: The Winter Soldier    2014       7.8        136  228636083
Captain America: Civil War             2016       7.8        147  408080554
Guardians of the Galaxy Vol. 2         2017       7.7        136  389804217
Doctor Strange                         2016       7.5        115  232630718
Spider-Man: Homecoming                 2017       7.5        133  334166825


$ python get_marvel_stats.py money -t 8
title                             year    rating    runtime      money
------------------------------  ------  --------  ---------  ---------
Avengers: Infinity War            2018       8.7        149  664987816
The Avengers                      2012       8.1        143  623279547
Black Panther                     2018       7.4        134  501105037
Avengers: Age of Ultron           2015       7.4        141  429113729
Iron Man 3                        2013       7.2        130  408992272
Captain America: Civil War        2016       7.8        147  408080554
Guardians of the Galaxy Vol. 2    2017       7.7        136  389804217
Spider-Man: Homecoming            2017       7.5        133  334166825


$ python get_marvel_stats.py runtime
title                                  year    rating    runtime      money
-----------------------------------  ------  --------  ---------  ---------
Avengers: Infinity War                 2018       8.7        149  664987816
Captain America: Civil War             2016       7.8        147  408080554
The Avengers                           2012       8.1        143  623279547
Avengers: Age of Ultron                2015       7.4        141  429113729
Captain America: The Winter Soldier    2014       7.8        136  228636083

```

Time: 1:25 код

## Day 43: Sep 10, 2018

Сегодня только лекции.

Time: 0:30 лекции

## Day 44: Sep 11, 2018

Сегодня только лекции.

Time: 1:10 лекции

## Day 45: Sep 12, 2018

Небольшой скрипт для поиска эпизодов подкаста Talk Python:

```
$ python search_talkpython.py concurrency
There are 27 matching episodes:
1. Monitoring high performance Python apps at Opbeat
2. Flask, Django style with Flask-Diamond
3. Fluent Python
4. Adding concurrency to Django with Django Channels
5. Effective Python
6. Grumpy: Running Python on Go
7. Deep Dive into Modules and Packages
8. Crossing the streams with Podcast.__init__
9. Shipping software to users
10. MongoDB Applied Design Patterns
11. Simplifying Python's Async with Trio
12. Python in Biology and Genomics
13. Scaling Python to 1000's of cores with Ufora
14. SQLAlchemy and data access in Python
15. Home Assistant: Pythonic Home Automation
16. Enterprise Python and Large-Scale Projects
17. A Pythonic Database Tour
18. Turbogears and the future of Python web frameworks
19. Python concurrency with Curio
20. PyPy - The JIT Compiled Python Implementation
21. Python and MongoDB
22. Create better Python programs with concurrency, libraries, and patterns
23. Quart: Flask, but 3x faster
24. Python Book Authors'  Panel Discussion
25. Python for Humans projects
26. 10 top talks of PyCon 2017 reviewed
27. Inside the new PyPI launch


$ python search_talkpython.py concurrency --table
There are 27 matching episodes:
  Index    Show number  Title
-------  -------------  -----------------------------------------------------------------------
      1             43  Monitoring high performance Python apps at Opbeat
      2             97  Flask, Django style with Flask-Diamond
      3             24  Fluent Python
      4             98  Adding concurrency to Django with Django Channels
      5             25  Effective Python
      6             95  Grumpy: Running Python on Go
      7             12  Deep Dive into Modules and Packages
      8             68  Crossing the streams with Podcast.__init__
      9            127  Shipping software to users
     10            109  MongoDB Applied Design Patterns
     11            167  Simplifying Python's Async with Trio
     12            154  Python in Biology and Genomics
     13             60  Scaling Python to 1000's of cores with Ufora
     14              5  SQLAlchemy and data access in Python
     15            122  Home Assistant: Pythonic Home Automation
     16              4  Enterprise Python and Large-Scale Projects
     17            105  A Pythonic Database Tour
     18             35  Turbogears and the future of Python web frameworks
     19            107  Python concurrency with Curio
     20             21  PyPy - The JIT Compiled Python Implementation
     21              2  Python and MongoDB
     22             58  Create better Python programs with concurrency, libraries, and patterns
     23            147  Quart: Flask, but 3x faster
     24            148  Python Book Authors'  Panel Discussion
     25            115  Python for Humans projects
     26            116  10 top talks of PyCon 2017 reviewed
     27            159  Inside the new PyPI launch

```

Time: 1:00 код

## Day 46: Sep 13, 2018

Сегодня доделывала [скрипт для переноса решения заданий из ветки master в task_check](https://github.com/natenka/100-days-of-Python/commit/a7d24dc9683a56fed0b656812f1d9dbbe813f10a). Добавила поддержку отдельных заданий и glob выражений.

Time: 1:10 код

## Day 47: Sep 14, 2018

Сегодня только лекции.

Time: 1:00 лекции

## Day 48: Sep 16, 2018

Решила две задачки Bites of Py.

> Один день пропустила

Time: 1:00 код

## Day 49: Sep 17, 2018

Сегодня только лекции: лекция по курсу, плюс выступление [Refactoring Python: Why and How to Restructure Your Code](https://www.youtube.com/watch?v=D_6ybDcU5gc)

Time: 1:00 лекции

## Day 50: Sep 18, 2018

Сегодня только лекции: смотрю выступления с pycon.

Time: 1:00 лекции

## Day 51: Sep 19, 2018

Сегодня только лекции: смотрю выступления с pycon 2018.

Time: 1:10 лекции

## Day 52: Sep 20, 2018

Сегодня только лекции: смотрю выступления с pycon.

Time: 3:30 лекции

## Day 53: Sep 21, 2018

Сегодня только лекции: смотрю выступления с pycon.

Time: 2:00 лекции

## Day 54: Sep 22, 2018

Сегодня только лекции: смотрю выступления с pycon.

Time: 2:40 лекции

## Day 55: Sep 23, 2018

Сегодня только лекции.

Time: 1:00 лекции

## Day 56: Sep 24, 2018

Сегодня только лекции: смотрю выступления с pycon.

Time: 0:40 лекции

## Day 57: Sep 25, 2018

Сегодня только лекции: смотрю выступления с pycon.

Time: 1:05 лекции

## Day 58 Sep 26, 2018

Сегодня только лекции: смотрю выступления с pycon и начала курс [Async Techniques and Examples in Python](https://training.talkpython.fm/courses/explore_async_python/async-in-python-with-threading-and-multiprocessing)

Time: 2:30 лекции

## Day 59 Sep 27, 2018

Продолжаю смотреть курс Async Techniques and Examples in Python.

Time: 0:30 лекции

## Day 60 Sep 28, 2018

Продолжаю смотреть курс Async Techniques and Examples in Python.

Time: 0:40 лекции

## Day 61 Sep 29, 2018

Продолжаю смотреть курс Async Techniques and Examples in Python.

Time: 1:10 лекции

## Day 62 Sep 30, 2018

Продолжаю смотреть курс Async Techniques and Examples in Python.

Time: 1:00 лекции

## Day 63 Oct 1, 2018

Продолжаю смотреть курс Async Techniques and Examples in Python.

Time: 1:05 лекции

## Day 64 Oct 2, 2018

Продолжаю смотреть курс Async Techniques and Examples in Python.

Time: 0:50 лекции

## Day 65 Oct 3, 2018

Продолжаю смотреть курс Async Techniques and Examples in Python.

Time: 0:50 лекции


## Статистика 1-20 день


<img align="center" src="https://raw.githubusercontent.com/natenka/100-days-of-Python/master/talkpython-100-days/day020/20_days_report.png">


## Идеи скриптов

* Дополнить скрипт для переноса решения заданий из ветки master в task_check: сделать поддержку отдельных заданий
* разбор логов FCC по присутствию на лекциях
* поиск по всем моим репозиториям (часто надо вспомнить где был пример кода)
* скрипт, который отображает задание по номеру + интеграция со slack
* workout log
* pytest: тесты для заданий
* проверка доступности ссылок в книге

