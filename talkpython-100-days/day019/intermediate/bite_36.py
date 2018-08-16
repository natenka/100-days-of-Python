'''
Bite 36. Having fun with *args and **kwargs
Write a function called get_profile that takes:

a required name,
a required age,
one or more optional sports (args),
one or more optional awards (keyword args).
Add the following validations:

if age is not an int raise a ValueError,
if more than 5 sports are provided raise a ValueError.
Some examples how your function can be called (see also the TESTS tab):

get_profile('tim', 36)
get_profile('tim', 36, 'tennis', 'basketball')
get_profile('tim', 36, 'tennis', 'basketball', champ='helped out team in crisis') 
The function should return a dict with all the args, like so:

get_profile('tim', 36) == {'name': 'tim', 'age': 36}  # some arg types
{'name': 'tim', 'age': 36, 'sports': ['basketball', 'tennis'], 'awards': {'champ': 'helped out team in crisis'}}  # all arg types
(args list to be sorted alphabetically)
We hope this gives you a good handle on Python's different types of function arguments. Enjoy!
'''
def get_profile():
    pass


###########################tests
import pytest

from profile import get_profile


def test_get_profile_no_name():
    with pytest.raises(TypeError):
        assert get_profile()


def test_get_profile_no_age():
    with pytest.raises(TypeError):
        assert get_profile('tim')


def test_get_profile_valueerror():
    with pytest.raises(ValueError):
        assert get_profile('tim', 'nonint')


def test_get_profile_too_many_sports():
    with pytest.raises(ValueError):
        sports = ['tennis', 'basketball', 'badminton',
                  'baseball', 'volleyball', 'boxing']
        assert get_profile('tim', 36, *sports)


def test_get_profile_dict():
    assert get_profile('tim', 36) == {'name': 'tim', 'age': 36}


def test_get_profile_one_sport():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['tennis']}
    assert get_profile('tim', 36, 'tennis') == expected


def test_get_profile_two_sports():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis']}
    assert get_profile('tim', 36, 'tennis', 'basketball') == expected


def test_get_profile_award():
    expected = {'name': 'tim', 'age': 36,
                'awards': {'champ': 'helped out team in crisis'}}
    assert get_profile('tim', 36,
                       champ='helped out team in crisis') == expected


def test_get_profile_two_sports_and_one_award():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis'],
                'awards': {'champ': 'helped out team in crisis'}}
    assert get_profile('tim', 36, 'tennis', 'basketball',
                       champ='helped out team in crisis') == expected


def test_get_profile_two_sports_and_three_awards():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis'],
                'awards': {'champ': 'helped out the team in crisis',
                           'service': 'going the extra mile for our customers',
                           'attitude': 'unbeatable positive + uplifting'}}
    assert get_profile('tim', 36, 'tennis', 'basketball',
                       service='going the extra mile for our customers',
                       champ='helped out the team in crisis',
                       attitude='unbeatable positive + uplifting') == expected

