class Game():
    line = '-' * 60

    def __init__(self):
        player = input("Please enter your name: ")
        print(f'\nHello {player}! Welcome to Rock, Paper, Scissors!\n{self.line}')
