import decimal


def round_even(number):
    """Takes number int and returns it rounded even"""
    n = decimal.Decimal(number)
    lower = int(n.to_integral())
    higher = lower+1
    if (number - lower) == (higher - number):
        if lower % 2 == 0:
            return lower
        elif higher % 2 == 0:
            return higher
    else:
        return round(number)

    #answer:
    #return decimal.Decimal(number).quantize(0)
