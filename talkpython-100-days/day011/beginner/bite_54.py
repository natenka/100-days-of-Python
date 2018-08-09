import re

INDENTS = 4


def print_hanging_indents(poem):
    lines = [re.split('\n +', line.lstrip()) for line in poem.split('\n\n')]
    for line_list in lines:
        print(line_list[0])
        for line in line_list[1:]:
            print(' '*INDENTS + line)

