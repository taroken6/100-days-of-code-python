from collections import namedtuple


class Game():
    line = '-' * 60

    def __init__(self):
        self.player = None

    def get_player_name(self, name):
        self.player = Player(input("Please enter your name: "))

    def print_header(self):
        print(f'Welcome to Rock, Paper, Scissors!\n{self.line}')

    def game_loop(self, p1, p2, rolls):
        count = 1
        while count < 3:
            p2_roll = None # Get random roll
            p1_roll = None # Have player choose roll

            outcome = p1_roll.can_defeat(p2_roll)

            # Display throws
            # Display winner for this round

            count += 1

        # Compute who won


class Player():
    def __init__(self, name):
        self.name = name


class Roll():
    def __init__(self):
        roll = namedtuple('Roll', ('win', 'lose'))
        self.rock = None
        self.paper = None
        self.scissor = None

    def build_three_rolls(self):
        _rock = 'rock'
        _scissor = 'scissor'
        _paper = 'paper'
        self.rock = Roll(_scissor, _paper)
        self.paper = Roll(_rock, _scissor)
        self.scissor = Roll(_paper, _rock)
