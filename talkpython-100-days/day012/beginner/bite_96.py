import re

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        content = f.read()
        filename = file_.split('/')[-1]
        lines = len(content.split('\n'))
        words = len(re.findall('(\w+)', content))
        chars = len(content)
        return f"{lines:10} {words:10} {chars:10} {filename}"

