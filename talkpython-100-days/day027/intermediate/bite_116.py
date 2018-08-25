'''
In this Bite you complete get_files that receives a dirname and size_in_kb.

There are two things you need to code:

    Inspect/list the files in dirname,
    Filter out the files that are bigger or equal than size_in_kb, return those in a list (or turn the function into a generator.
    The os module is your friend here, but you also might want to check out glob. Have fun and keep coding in Python!
'''

import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    files = [f for f in os.listdir('.') if os.stat(f).st_size/ONE_KB > size_in_kb]
    return files

#tests
import os
from tempfile import TemporaryDirectory

import pytest

from files import ONE_KB, get_files

TMP = '/tmp'


def _create_files(dirname):
    for i in range(1, 4):
        for j in range(1, 11):
            file_size = i * j * ONE_KB
            filename = f'{file_size}.txt'
            path = os.path.join(dirname, filename)
            _create_file(path, file_size)


def _create_file(path, size):
    with open(path, 'wb') as f:
        f.write(os.urandom(size))


@pytest.mark.parametrize("size", [
    1, 3, 6, 9, 12, 20, 25,
])
def test_get_files(size):
    with TemporaryDirectory(dir=TMP) as dirname:
        test_size_in_kb = size * ONE_KB
        _create_files(dirname)

        files = list(get_files(dirname, test_size_in_kb))
        filenames = [os.path.splitext(os.path.basename(f))[0] for f in files]

        assert all(int(fn) >= test_size_in_kb for fn in filenames)

