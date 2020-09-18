from TextGame import Game, Roll, Player

if __name__ == '__main__':
    game = Game()
    game.print_header()

    rolls = Roll().build_three_rolls()

    name = game.get_player_name()

    p1 =  Player('P1')
    p2 = Player('CPU')

    game.game_loop(p1, p2, rolls)