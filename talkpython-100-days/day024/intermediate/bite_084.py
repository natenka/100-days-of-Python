'''
Complete flatten that takes a list of lists (which can have lists ad infinitum) and flatten them into a one dimensional list.

So this input:

[1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
... should generate this output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Make sure you support both lists and tuples. You probably want to use recursion here ... have fun!
'''

def generator_flatten(list_of_lists):
    for item in list_of_lists:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


def flatten(list_of_lists):
    result = []
    for item in list_of_lists:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]))

inp = ['a', 'b', [1, 2, 3],
      ['c', 'd', ['e', 'f', ['g', 'h']]],
      [4, [5, 6, [7, [8]]]]]


print(flatten(inp))
