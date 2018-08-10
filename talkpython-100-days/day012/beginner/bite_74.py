import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return calendar.day_name[
        calendar.weekday(date.year, date.month, date.day)]

