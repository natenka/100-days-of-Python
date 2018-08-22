from functools import reduce

def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    return reduce(set.intersection, map(set, programmers.values()))

def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    return set.intersection(*map(set, programmers.values()))

pr_map = {'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
          'paul': ['C++', 'JS', 'Python'],
          'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
          'tim': ['Python', 'Haskell', 'C++', 'JS']}

print(common_languages(pr_map))
