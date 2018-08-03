NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return [name.title() for name in set(names)]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda x: x.split()[-1], reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    sorted_by_name_length = sorted(names, key=lambda x: len(x.split()[0]))
    
    return sorted_by_name_length[0].split()[0]
