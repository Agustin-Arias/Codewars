# https://www.codewars.com/kata/586c0909c1923fdb89002031/train/python

import numpy as np
class Connect4():

    def __init__(self):
        self.board = np.zeros((6,7))
        self.playing = 0
        self.gameover = false

    def play(self, col):
        num_of_player = self.playing + 1
        column_chosen = self.board[:col]
        if any(num == 0 for num in column_chosen):
            return "Column full!"

        for index, element in enumerate(column_chosen):
            if element == 0:
                column_chosen[index] = num_of_player

        if self.gameover:
            return "Game has finished!"
        elif self.four_connected(num_of_player):
            return f"Player {num_of_player} wins!"

        output = f"Player {num_of_player} has a turn"
        self.playing += 1
        self.playing &= 2
        return output

    def four_connected(self, num_of_player):
        '''
        determines if the board contains a
        sequence of 4 1's or 2's depending on
        which player is playing
        '''
        pass

