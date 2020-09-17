class Bite5():
    NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
             'julian sequeira', 'sandra bullock', 'keanu reeves',
             'julbob pybites', 'bob belderbos', 'julian sequeira',
             'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

    def dedup_and_title_case_names(self, names):
        """Should return a list of title cased names,
           each name appears only once"""
        return list({self.helper(x) for x in names})

    def helper(self, name):
        tmp = name.split()
        tmp[0] = tmp[0][0].upper() + tmp[0][1:]
        tmp[1] = tmp[1][0].upper() + tmp[1][1:]
        return ' '.join(tmp)

    def sort_by_surname_desc(self, names):
        """Returns names list sorted desc by surname"""
        names = self.dedup_and_title_case_names(names)
        return sorted(names, key=lambda x: x.split()[1], reverse=True)

    def shortest_first_name(self, names):
        """Returns the shortest first name (str).
           You can assume there is only one shortest name.
        """
        names = self.dedup_and_title_case_names(names)
        return sorted(names, key=lambda x: len(x.split()[0]))[0].split()[0]


class Bite26():
    bites = {6: 'PyBites Die Hard',
             7: 'Parsing dates from logs',
             9: 'Palindromes',
             10: 'Practice exceptions',
             11: 'Enrich a class with dunder methods',
             12: 'Write a user validation function',
             13: 'Convert dict in namedtuple/json',
             14: 'Generate a table of n sequences',
             15: 'Enumerate 2 sequences',
             16: 'Special PyBites date generator',
             17: 'Form teams from a group of friends',
             18: 'Find the most common word',
             19: 'Write a simple property',
             20: 'Write a context manager',
             21: 'Query a nested data structure'}
    exclude_bites = {6, 10, 16, 18, 21}

    def filter_bites(self, bites=bites, bites_done=exclude_bites):
        """return the bites dict with the exclude_bites filtered out"""
        return {x: bites[x] for x in bites.keys() if not x in self.exclude_bites}
