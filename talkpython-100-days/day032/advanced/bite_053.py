from itertools import zip_longest


COL_WIDTH = 20


def split_text(paragraph):
    p_list = paragraph.split(' ')
    parts = []
    part = []
    for word in p_list:
        if len(' '.join(part + [word])) <= COL_WIDTH:
            part.append(word)
        else:
            parts.append(part)
            part = []
            part.append(word)
    parts.append(part)
    return parts


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    paragraphs = text.strip().split('\n\n')
    result = [' '.join([' '.join(column).ljust(COL_WIDTH) for column in row])
              for row in zip_longest(*map(split_text, paragraphs), fillvalue='')]
    return '\n'.join(result)



text = """My house is small but cosy.

It has a white kitchen and an empty fridge.

I have a very comfortable couch, people love to sit on it."""

print(text_to_columns(text))
#print(split_text('My mornings are filled with coffee and reading, if only I had a garden'))


#answer
from itertools import zip_longest
import textwrap

COL_WIDTH = 20
PADDING = 5


def _format(row):
    return " ".join(['{c:{w}}'.format(c=col, w=COL_WIDTH+PADDING)
                     for col in row])


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    cols = []
    for paragraph in text.split("\n\n"):
        col_lines = textwrap.fill(paragraph, width=COL_WIDTH).split("\n")
        cols.append(col_lines)

    output = []
    # need zip_longest otherwise text will get lost
    for row in zip_longest(*cols, fillvalue=''):
        output.append(_format(row))

    return "\n".join(output)

