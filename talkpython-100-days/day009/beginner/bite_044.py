import string
import secrets


def gen_key(parts=4, chars_per_part=8):
    items = string.ascii_uppercase + string.digits
    key = []
    for _ in range(parts):
        key.append(''.join(secrets.choice(items) for i in range(chars_per_part)))
    return '-'.join(key)

print(gen_key())
