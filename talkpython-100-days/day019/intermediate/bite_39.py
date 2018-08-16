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
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    pass


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    pass



###tests
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
