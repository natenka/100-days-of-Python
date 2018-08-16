"""
Bite 41. Write a login_required decorator

If you worked with Flask or Django you must have seen routes being decorated to enforce authentication.

In this Bite you will write your own login checking decorator.

We simplify the request / session stuff by using 2 hardcoded lists:

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']
Write the login_required decorator used here:

@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'
Using this decorator there are 3 possible scenarios you have to account for:

user is not on the system, return "please create an account"
user is on the system but not logged in, return "please login"
user is on the system and logged in, return the function's "welcome back {user}"
See also the tests for more details. Have fun and enjoy!
"""

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    pass


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    pass


### tests

from login import welcome


def test_no_account():
    """User is not on the system"""
    assert welcome('anonymous') == 'please create an account'


def test_not_loggedin():
    """User is on the system but not logged in"""
    assert welcome('julian') == 'please login'


def test_loggedin():
    """User is on the system and logged in"""
    assert welcome('sue') == 'welcome back sue'


def test_docstring():
    """Decorator should not lose function's docstring"""
    assert welcome.__doc__ == 'Return a welcome message if logged in'

