import random


class Game():
    line = '-' * 60

    def __init__(self):
        self.player = None
        self.rolls = None

    def loop(self, p1, p2):
        self.rolls = self.build_three_rolls()
        cnt = 1
        while cnt < 4:
            p2.roll = self.random_roll()
            p1.roll = self.get_roll(input("Select a roll: "))
            print(f'{p1.name}-{p1.roll.name} vs. {p2.name}-{p2.roll.name}')
            winner = self.get_winner(p1, p2)
            if winner == p1:
                p1.score += 1
                print(f'{p1.name} wins this round!')
            elif winner == p2:
                p2.score += 1
                print(f'{p2.name} wins this round!')
            else:
                print('Draw round!')
            print()
            cnt += 1
        if p1.score > p2.score:
            print(f'{p1.name} wins the match!')
        elif p1.score < p2.score:
            print(f'{p2.name} wins the match!')
        else:
            print("Match draw!")

    def get_winner(self, p1, p2):
        if p1.roll.name == p2.roll.lose:
            return p1
        elif p2.roll.name == p1.roll.lose:
            return p2
        else:
            return None

    def build_three_rolls(self):
        return {'rock': Roll(name='rock', beat='scissor', lose='paper'),
                'paper': Roll(name='paper', beat='rock', lose='scissor'),
                'scissor': Roll(name='scissor', beat='paper', lose='scissor')}

    def random_roll(self):
        return random.choice(list(self.rolls.values()))

    def get_roll(self, name):
        while True:
            if name in self.rolls:
                return self.rolls[name]
            elif name == 'random':
                return self.random_roll()
            else:
                name = input("Please enter a valid choice: ")

    def print_header(self):
        print(f'Welcome to Rock, Paper, Scissors!\n{self.line}')

    def get_player_name(self):
        self.player = Player(input("Please enter your name: "))


class Player():
    def __init__(self, name):
        self.name = name
        self.roll = None
        self.score = 0


class Roll():
    def __init__(self, name='', beat='', lose=''):
        self.name = name
        self.beat = beat
        self.lose = lose
