# Connect 4
# https://www.codewars.com/kata/586c0909c1923fdb89002031/train/python

import numpy as np
class Connect4():

    def __init__(self):
        self.board = np.zeros((6,7))
        self.playing = 0
        self.gameover = False

    def play(self, col):
        if self.gameover:
            return "Game has finished!"
        num_of_player = self.playing + 1
        column_chosen = self.board[:, col]
        if all(num != 0 for num in column_chosen):
            return "Column full!"

        for index, element in list(enumerate(column_chosen))[::-1]:
            if element == 0:
                column_chosen[index] = num_of_player
                break

        if self.four_connected(num_of_player):
            self.gameover = True
            return f"Player {num_of_player} wins!"

        output = f"Player {num_of_player} has a turn"
        self.playing += 1
        self.playing %= 2

        return output

    def four_connected(self, num_of_player):
        '''
        determines if the board contains a
        sequence of 4 1's or 2's depending on
        which player is playing
        '''
        board = self.board
        if not self.gameover: print(board, flush = True)
        def check_horizontal(board, num_of_player):
            for row in board:
                if any([all(row[i: i+4]==np.zeros(4) + num_of_player) for i in range(len(row)-3)]):
                    return True
            return False

        def get_main_diag(board):
            return [board.diagonal(i) for i in range(-2, 4)]

        return any(
            (check_horizontal(board, num_of_player),  # we look for horizontals strings of (num_of_player)
            check_horizontal(board.transpose(), num_of_player),  # vertical
            check_horizontal(get_main_diag(board), num_of_player),  # main diagonals (\)
            check_horizontal(get_main_diag(board[:, ::-1]), num_of_player))  # other diagonals (/)
            )

import time
game = Connect4()
while not game.gameover:
    import random
    x = random.randint(0, 6)
    print(game.play(x), flush = True)
    time.sleep(2)
    print()
