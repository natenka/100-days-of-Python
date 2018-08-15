from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    Blog = namedtuple('Blog', blog.keys())
    return Blog(**dict_)


def nt2json(nt):
    d = nt._asdict()
    d['started'] = str(d['started'])
    return json.dumps(d)
