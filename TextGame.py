from collections import namedtuple


class Game():
    line = '-' * 60

    def __init__(self):
        self.rolls = None

    def loop(self, p1, p2, rolls):
        self.rolls = self.build_three_rolls()
        cnt = 1
        while cnt < 3:
            p2_roll = None
            p1_roll = None
            # Display throws
            # Display winner
            cnt += 1
        # Compute winner

    def build_three_rolls(self):
        Rolls = namedtuple('Rolls', ['name', 'beat', 'lose'])
        d = {'rock': Rolls(name='rock', beat='scissor', lose='paper'),
             'paper': Rolls(name='paper', beat='rock', lose='scissor'),
             'scissor': Rolls(name='scissor', beat='paper', lose='scissor')}
        return d

    def print_header(self):
        print(f'Welcome to Rock, Paper, Scissors!\n{self.line}')

    def get_player_name(self):
        return input("Please input your name: ")


class Player():
    def __init__(self, name):
        self.name = name
