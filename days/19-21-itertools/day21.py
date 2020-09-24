import itertools
import os
import urllib.request


class Bite65:
    # PREWORK
    TMP = os.getenv("TMP", "/tmp")
    DICT = 'dictionary.txt'
    DICTIONARY = os.path.join(TMP, DICT)
    urllib.request.urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
        DICTIONARY
    )

    with open(DICTIONARY) as f:
        dictionary = set([word.strip().lower() for word in f.read().split()])

    def get_possible_dict_words(self, draw):
        """Get all possible words from a draw (list of letters) which are
           valid dictionary words. Use _get_permutations_draw and provided
           dictionary"""
        permutations = self._get_permutations_draw(self, draw)
        return [''.join(x).lower() for x in permutations if ''.join(x).lower() in self.dictionary]

    def _get_permutations_draw(self, draw):
        """Helper to get all permutations of a draw (list of letters), hint:
           use itertools.permutations (order of letters matters)"""
        res = []
        for n in range(1, len(draw) + 1):
            res += list(itertools.permutations(draw, n))
        return res


class Bite17:
    def friends_teams(friends: list, team_size: int = 2, order_does_matter: bool = False):
        if order_does_matter:
            return itertools.permutations(friends, team_size)
        else:
            return itertools.combinations(friends, team_size)


class Bite64:
    names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
    locations = 'DE ES AUS NL BR US'.split()
    confirmed = [False, True, True, False, True]

    def get_attendees(self):
        for participant in itertools.zip_longest(self.names, self.locations, self.confirmed, fillvalue='-'):
            print(participant)

    if __name__ == '__main__':
        get_attendees()
