from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_year_mark():
    year = PYBITES_BORN.year
    while True:
        year += 1
        yield PYBITES_BORN.replace(year=year)


def gen_100_days_mark():
    delta = timedelta(days=100)
    while True:
        yield PYBITES_BORN + delta
        delta += timedelta(days=100)


def gen_special_pybites_dates():
    hundred_days = gen_100_days_mark()
    year = gen_year_mark()
    while True:
        next_year = next(year)
        next_100_days = next(hundred_days)
        while next_100_days < next_year:
            yield next_100_days
            next_100_days = next(hundred_days)
        yield next_year
        yield next_100_days


if __name__ == "__main__":
    g = gen_special_pybites_dates()

    for i in range(100):
        print(next(g))
