import itertools


class App():
    line = '-' * 60

    def __init__(self):
        pass

    def run(self):
        # Cycle
        self._cycle()
        print(self.line * 2)

        # Product
        self._product()
        print(self.line * 2)

        # Combinations
        self._combinations()
        print(self.line * 2)

        # Permutations
        self._permutations()

    def _cycle(self):
        l1 = [1, 'a', 2, 'b']
        l2 = 'wasd'

        cycler = itertools.cycle(l1)
        out = ''
        for _ in range(9):
            out += str(next(cycler))
        print(out)

        cycler = itertools.cycle(l2)
        out = ''
        for _ in range(len(l2) * 3):
            out += next(cycler)
        print(out)

    def _product(self):
        l1 = [1, 'a', 2, 'b']
        l2 = 'wasd'

        it = itertools.product(l1, repeat=3)
        for x in it:
            print(x)

        print(self.line)

        it = itertools.product(l1, l2)
        for x in it:
            print(x)

    def _combinations(self):
        # Creates iterable of all non-repeating combinations of 'r' length
        l1 = ['a', 'b', 'c', 'd']

        it = itertools.combinations(l1, 2)
        for x in it:
            print(x)

    def _permutations(self):
        # Creates iterable of all permutations of an iterable with 'r' length (With repeating elements)
        l1 = ['a', 'b', 'c', 'd']

        it = itertools.permutations(l1, 2)
        for x in it:
            print(x)
