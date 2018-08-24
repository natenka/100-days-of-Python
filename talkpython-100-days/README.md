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

Время:

* 30 минут видео
* 1 час 10 минут код

## Day 2: July 31, 2018

Сегодня продолжаю работать над таймером pomodoro. Он уже [вполне рабочий](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day002/pomodoro_timer.py), хотя пока запускаю всё в секундах, вместо минут. Это легко меняется, достаточно будет изменить только одну функцию в финальной версии.

В целом всё уже работает, но ещё остается добавить интерфейс в cli с argparse или click. Пока что склоняюсь к click, так как его я знаю намного хуже.

Пример выполнения скрипта (записан с помощью [termtosvg](https://github.com/nbedos/termtosvg)):

<img src="https://cdn.rawgit.com/natenka/100-days-of-Python/7fd02998/talkpython-100-days/day002/pomodoro_timer_run_animation.svg" width="800">

Время: 1 час 30 минут код

## Day 3: August 1, 2018

Завершила работу над [таймером Pomodoro](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day003/pomodoro_timer.py). Сегодня добавила интерфейс командной строки. Остановилась на click.
Теперь все параметры можно указывать при вызове скрипта.

Пока оставила на будущее оповещения и обошлась добавлением цвета в вывод. Плюс теперь таймер уже полноценно работает по минутам, а не секундам.

Пример выполнения скрипта с секундными интервалами (записан с помощью [termtosvg](https://github.com/nbedos/termtosvg)):

<img src="https://cdn.rawgit.com/natenka/100-days-of-Python/9cbc94c6/talkpython-100-days/day003/pomodoro_timer_run_animation.svg" width="800">

Время: 1 час 20 минут код

## Day 4: August 2, 2018

Начала следующую [тройку дней](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/04-06-collections/collections.ipynb), тема - модуль collections.
Посмотрела лекции и сделала задание [Code Challenge 13 - Highest Rated Movie Directors](https://pybit.es/codechallenge13.html). Задание в целом простое, но соображаю я сегодня хуже, чем обычно, так что времени ушло больше.

Следующие два дня буду заниматься разбором логов FCC с информацией о том, кто был на лекции онлайн. В итоге хочу получить сводку с информацией о том, кто ходит на лекции чаще всего.

Время:

* 15 минут видео
* 2 часа код

## Day 5: August 3, 2018

Сегодня занималась вечером, так что вместо намеченного скрипта делала задачки [Bites of Py](https://codechalleng.es/bites/). Решила делать все с самого начала, так что пока сделала intro и пару beginner.

Время: 1 час код

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

Время: 3 часа код

## Day 7: Aug 5, 2018

Сегодня только лекции. Посмотрела лекции по 7 дню и начала смотреть курс [Write Pythonic Code Like a Seasoned Developer](https://training.talkpython.fm/courses/explore_pythonic_code/write-pythonic-code-like-a-seasoned-developer)

Время: 1.5 часа лекции

## Day 8: Aug 6, 2018

Решила 4 задачки [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day008)

Время: 50 минут код

## Day 9: Aug 7, 2018

Решила 9 задачек [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day009) и продолжаю слушать курс [Write Pythonic Code Like a Seasoned Developer](https://training.talkpython.fm/courses/explore_pythonic_code/write-pythonic-code-like-a-seasoned-developer).

Время:

* 1 час видео
* 1.5 часа код

## Day 10: Aug 8, 2018

Сегодня только лекции.

Время: 1 час лекции

## Day 11: Aug 9, 2018

Решила 6 задачек [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day011)

Время: 1 час код

## Day 12: Aug 10, 2018

Решила 6 задачек [Bites of Python](https://github.com/natenka/100-days-of-Python/tree/master/talkpython-100-days/day012)

Время: 1 час код

## Day 13: Aug 11, 2018

Сегодня только лекции.

Время: 1 час лекции

## Day 14: Aug 12, 2018

Сегодня по курсу сделала задачку с игрой [Rock Paper Scissors](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day14/rock_paper_scissors.py).

Время: 1 час код


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

Время: 1.5 часа код

## Day 16: Aug 14, 2018

Сегодня новая тема [list comprehensions and generators](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/16-18-listcomprehensions-generators/list-comprehensions-generators.ipynb).  Послушала лекции и два часа на код: решила [challenge 11](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day016/challenge_11.py) и [5 задачек intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/6ad4b69b96f94b07873dc4ee0f50dbe0334660da).

Время:

* 15 минут видео
* 2 часа код

## Day 17: Aug 15, 2018

Так как вчера я сделала все что было по темам на три дня, сегодня решаю задачки: [6 задачек intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/fefee6ac5512acbf10f9d3b17e4b34cd45e0baf3).

Время: 1 час 10 минут код

## Day 18: Aug 16, 2018

Сегодня сделала [4 задачки intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/aeb2bd169c1fdb6d97d336faad0fe81916b5ecaa)

Время: 1 час код

## Day 19: Aug 17, 2018

Сегодня сделала 2 задачки, еще одну вроде сделала, но что-то ответ не совпадает.

Время: 1 час код

## Day 20: Aug 18, 2018

Сегодня сделала [1 задачку](https://github.com/natenka/100-days-of-Python/commit/99d8c0be7c0ec1b253d4ebe4cd9a9f7fb738793a) и посмотрела видео по новым темам [itertools](https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/19-21-itertools).

Время:

* 30 минут код
* 30 минут видео

## Day 21: Aug 19, 2018

Сегодня [сделала задачку](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day021/traffic_lights.py) с созданием [светофора](https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/19-21-itertools#day-n1-create-a-traffic-lights-script) и [одну intermediate уровня](https://github.com/natenka/100-days-of-Python/blob/master/talkpython-100-days/day021/intermediate/bite_060.py)

Пример выполнения скрипта со светофором (записан с помощью [termtosvg](https://github.com/nbedos/termtosvg)):

<img src="https://cdn.rawgit.com/natenka/100-days-of-Python/4cc8aa3a/talkpython-100-days/day021/traffic_lights_animation.svg" width="800">

## Day 22: Aug 20, 2018

Сегодня решила три задачки [intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/0c87743c30d4db3eadc460aa2be635cd92a1cfed).

Время:

* 1 час 20 минут код
* 23 минуты видео

## Day 23: Aug 21, 2018

Сегодня решила пять задачек [intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/e5477c6bfdc348f1f833bc030c091713320a3c02).

Время 1 час 10 минут код

## Day 24: Aug 22, 2018

Сегодня решила 4 задачки [intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/5bfe63009662aad10b01c71a0540853544604155).

Время: 1 час код

## Day 25: Aug 23, 2018

Сегодня решила 6 задачек intermediate уровня.

Время: 1 час 45 минут код

## Day 26: Aug 24, 2018

Сегодня решила [3 задачки intermediate уровня](https://github.com/natenka/100-days-of-Python/commit/93bfa88bdf7c1cd6971edcb4b98ee6b492d46bd5) и посмотрела лекции по теме.

Время:

* 20 минут лекции
* 40 минут код

## Статистика 1-20 день


<img align="center" src="https://raw.githubusercontent.com/natenka/100-days-of-Python/master/talkpython-100-days/day020/20_days_report.png">


## Идеи скриптов

* Скрипт для переноса решения заданий из ветки master в task_check
* разбор логов FCC по присутствию на лекциях
* поиск по всем моим репозиториям (часто надо вспомнить где был пример кода)
* скрипт, который отображает задание по номеру + интеграция со slack
* workout log
* pytest: тесты для заданий
* проверка доступности ссылок в книге
