MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print name is allowed / not allowed to drive based on MIN_DRIVING_AGE"""
    art = 'not ' if age < MIN_DRIVING_AGE else ''
    print(f"{name} is {art}allowed to drive")
