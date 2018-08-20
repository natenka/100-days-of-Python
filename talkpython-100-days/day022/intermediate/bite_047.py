'''
You know these Create a new password forms? They do a lot of checks to make sure you make a password that is hard to guess and you will surely forget.

In this Bite you will write a validator for such a form field.

Complete the validate_password function below. It takes a password str and validates that it:

is between 6 and 12 chars long (both inclusive)
has at least 1 digit [0-9]
has at least two lowercase chars [a-z]
has at least one uppercase char [A-Z]
has at least one punctuation char (use: PUNCTUATION_CHARS)
Has not been used before (use: used_passwords)

If the password matches all criteria the function should store the password in used_passwords and return True.

Have fun, keep calm and code in Python!
'''
import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    length = 6 <= len(password) <= 12
    has_digit = re.search('\d', password)
    has_two_lowercase = len(re.findall('[a-z]', password)) >= 2
    has_uppercase = len(re.findall('[A-Z]', password)) >= 1
    has_punctuation = len(re.findall('[{}]'.format(''.join(PUNCTUATION_CHARS)), password)) >= 1
    new = password not in used_passwords
    correct = all(locals().values())
    if correct:
        used_passwords.add(password)
        return correct


assert not validate_password('short')
assert not validate_password('waytoolongpassword')


#def test_password_missing_chars():
assert not validate_password('UPPERCASE')
assert not validate_password('lowercase')
assert not validate_password('PW_no_digits')
assert not validate_password('Pw9NoPunc')
assert not validate_password('_password_')
assert not validate_password('@#$$)==1')


#def test_password_only_one_letter():
assert not validate_password('@#$$)==1a')


#def test_validate_password_good_pws():
assert validate_password('passWord9_')
assert validate_password('another>4Y')
assert validate_password('PyBites@1912')
assert validate_password('We<3Python')


#def test_password_not_used_before():
assert not validate_password('PassWord@1')
assert not validate_password('PyBit$s9')

