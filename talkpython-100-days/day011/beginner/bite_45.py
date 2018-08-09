from collections import deque


def queue(n=5):
    return deque([], n)


if __name__ == '__main__':
    q = queue()
    for i in range(10):
        q.append(i)
        print((i, list(q)))

    """Queue size does not go beyond n (int), this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """
