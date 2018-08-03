text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'
import re

def strip_vowels(text=text):
    """Replace all vowels by *, return newly formed string
       and number of replacements done"""
    initial = text.count('*')
    new_text = re.sub(f'[{vowels}{vowels.upper()}]', '*', text)
    num_of_star = new_text.count('*') - initial
    return new_text, num_of_star
