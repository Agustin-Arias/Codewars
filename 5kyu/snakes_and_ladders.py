# Snakes and ladders
# https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python
class SnakesLadders:
    def __init__(self):
        self.ladders = {
            2: 38,
            7: 14,
            8: 31,
            15: 26,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            78: 98,
            87: 94
        }
        self.snakes = {
            99: 80,
            95: 75,
            92: 88,
            89: 68,
            74: 53,
            64: 60,
            62: 19,
            49: 11,
            46: 25,
            16: 6
        }
        self.playing = 0
        self.player_positions = [0, 0]
        self.gameover = False

    def play(self, die1, die2):
        if self.gameover:
            return "Game over!"
        position = self.player_positions[self.playing]
        num_of_player = self.playing + 1
        position += die1 + die2

        if position == 100:
            self.gameover = True
            return f"Player {num_of_player} Wins!"
        elif position > 100:
            position = 200 - position

        if position in self.ladders.keys():
            position = self.ladders[position]
        elif position in self.snakes.keys():
            position = self.snakes[position]

        output = f"Player {num_of_player} is on square {position}"
        self.player_positions[self.playing] = position

        if die1 != die2:
            self.playing += 1
            self.playing %= 2
        return output


game = SnakesLadders()
print(game.play(1,1))
print(game.play(1,5))
print(game.play(6,2))
print(game.play(1,1))
