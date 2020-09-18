from TextGame import Game, Roll, Player

if __name__ == '__main__':
    game = Game()
    game.print_header()

    name = game.get_player_name()

    p1 = Player('P1')
    p2 = Player('CPU')

    game.loop(p1, p2)
