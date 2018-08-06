from collections import deque

def rotate(string, n):
    """Rotate characters in a string. Expects string and n (int) for
       number of characters to move.
    """
    deq = deque(string)
    if n > 0:
        for _ in range(n):
            deq.append(deq.popleft())
    elif n < 0:
        for _ in range(abs(n)):
            deq.appendleft(deq.pop())
    return ''.join([i for i in deq])


