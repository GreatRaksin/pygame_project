from objects import GameRound, Snake, Food


def main():
    game = GameRound()
    player = Snake()
    apple = Food()
    game.chek_errors()


if __name__ == '__main__':
    main()