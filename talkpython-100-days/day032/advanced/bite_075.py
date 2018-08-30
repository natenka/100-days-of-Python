'''
In the last bite we return the weekday from a date object. And you probably used the calendar module.

Unix has a similar tool to look up a week day for a certain date: cal, for example:

$ cal 4 2018
     April 2018
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
In this Bite we are going to ignore the existance of Python's calendar module for a minute and do a parsing Kata. Complete the get_weekdays function below that takes a multiline string output from the Unix cal command (see the TESTS tab for examples) and convert it to a mapping (dict) where the keys are day ints and the values are the 2 letter week days (Su Mo Tu ...).

This way it's easy to lookup any date and get the week day returned (again see how we use the function in the tests)

Sure you might put this off as useless because there is a module to work with dates and calendar, but the point is to be able to convert an output into a workable data structure, a goto skill for any Python endeavor ranging from log parsing (related: Bite 7. Parsing dates from logs) to required data cleaning for plotting, etc.

String manipulation (you might use regexes and slicing here), looping, populating a dict, are Pythonic skills you will use over and over again. So good luck and have fun!
'''
import re


def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    headers, data = re.search('(Su Mo Tu We Th Fr Sa)(.*$)', calendar_output, re.DOTALL).groups()
    headers = headers.split()
    data = [line.split() for line in data.strip().split('\n')]
    data[0] = [0]*(7-len(data[0]))+data[0]
    data[-1] = data[-1] + [0]*(7-len(data[-1]))
    result = {}
    for row in data:
        result.update(dict(zip(map(int, row),  headers)))
    del result[0]
    return result



april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""

jan_1986 = """    January 1986
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""

jan_1956 = """    January 1956
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""

print(get_weekdays(april_1981))
print(get_weekdays(jan_1986))
print(get_weekdays(jan_1956))

import re


def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    lines = calendar_output.split("\n")
    day_names = lines[1].split()  # day names are on 2nd row
    day_rows = lines[2:-1]  # ignore last blank line

    weekdays = {}
    for line in day_rows:
        day_slots = re.findall('(\s{2}|\s\d|\d\d)\s?', line)
        for name, num in zip(day_names, day_slots):
            if num.strip():  # ignore empty slots (empty = Falsy)
                weekdays[int(num)] = name

    return weekdays
