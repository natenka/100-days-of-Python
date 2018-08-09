import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sums = itertools.accumulate(sequence)
    indexes = [idx for idx, item in enumerate(sequence, 1)]
    for s, idx in zip(sums, indexes):
        yield round(s/idx,2)
