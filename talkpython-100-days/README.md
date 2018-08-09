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

## Идеи скриптов

* разбор логов FCC по присутствию на лекциях
* поиск по всем моим репозиториям (часто надо вспомнить где был пример кода)
* скрипт, который отображает задание по номеру + интеграция со slack
* workout log
* pytest: тесты для заданий
* проверка доступности ссылок в книге
