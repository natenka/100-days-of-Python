'''
Bite 39. Calculate the total duration of a course
In this Bite you read in a text file with course times (MM:SS) per video.

You extract these and calculate the total course duration in HH:MM:SS.

See the docstrings and tests for more details.

Have fun and we hope you learn a thing or two.
'''

from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
#COURSE_TIMES = os.path.join('/tmp', 'course_timings')
#urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)
COURSE_TIMES = 'test_file_bite_39.txt'


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as data:
        return [match.group(1) for match in re.finditer('\((\d+:\d+)\)', data.read())]

d = ['3:47', '4:41', '1:21', '5:32', '2:23', '1:01', '0:43', '1:46', '4:08', '3:20', '2:17', '4:03', '2:48', '3:04', '3:36', '6:45', '2:12', '3:54', '5:41', '6:08', '3:01', '4:15', '5:30', '4:46', '2:49', '0:52', '3:31', '3:11', '3:13', '3:10', '3:28', '1:15', '1:10', '5:14', '4:27', '6:06', '1:39', '7:01', '4:26', '0:40', '6:36', '6:58', '6:11', '1:40', '3:05', '6:44', '4:02', '2:05', '3:36', '2:51', '7:16', '2:56', '1:28', '8:21', '6:44', '2:36', '9:48', '3:34', '2:25', '5:27', '4:19', '2:09', '2:04', '2:25', '4:37', '1:54', '9:45', '3:29', '1:15', '7:51', '6:17', '3:47', '4:04', '2:20', '2:29', '7:34', '8:48', '2:49', '7:38', '5:57', '3:49', '6:04', '2:03', '7:10', '4:50', '4:17', '3:34', '3:10', '1:48', '3:56', '2:05', '2:58', '6:14', '8:39', '3:48', '0:37', '10:30', '7:20', '2:51']


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    result = timedelta(0,0)
    for timestamp in timestamps:
        h, m = map(int, timestamp.split(':'))
        result += timedelta(0, h*60*60 + m*60)
    return str(result)



data = get_all_timestamps()
print(data)
print(calc_total_course_duration(data))

###tests
'''
from coursetime import get_all_timestamps, calc_total_course_duration


def test_get_all_timestamps():
    timestamps = get_all_timestamps()
    assert len(timestamps) == 99
    assert '2:29' in timestamps
    assert '4:19' in timestamps
    assert '6:06' in timestamps
    assert '8:39' in timestamps


def test_calc_total_course_duration():
    timestamps = get_all_timestamps()
    assert '6:50:31' in calc_total_course_duration(timestamps)
'''
