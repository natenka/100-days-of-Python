def positive_divide(numerator, denominator):
    try:
        result = numerator/denominator
        if result < 0:
            raise ValueError
        return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise
