from random import randint


class Player:
    def __init__(self, char):
        self.char = char
        # self.board = board
        self.moves = []

    def make_a_move(self):
        pass

    def retrieve_positions(self, box_number):

        if box_number == '1':
            pos = [0, 0]
        elif box_number == '2':
            pos = [0, 1]
        elif box_number == '3':
            pos = [0, 2]
        elif box_number == '4':
            pos = [1, 0]
        elif box_number == '5':
            pos = [1, 1]
        elif box_number == '6':
            pos = [1, 2]
        elif box_number == '7':
            pos = [2, 0]
        elif box_number == '8':
            pos = [2, 1]
        else:
            pos = [2, 2]
        return pos

# |1 | 2 | 3|
# |4 | 5 | 6|
# |7 | 8 | 9|


class User_player(Player):
    def make_a_move(self, box_number):
        positions = self.retrieve_positions(box_number)
        self.moves.append(positions)
        
        return positions


class Bot_player(Player):
    def make_a_move(self, available_positions):
        rand_num = str(randint(1, 9))
        pos = self.retrieve_positions(rand_num)
        while pos not in available_positions:

            rand_num = str(randint(1, 9))
            pos = self.retrieve_positions(rand_num)
        self.moves.append(pos)
        return pos
