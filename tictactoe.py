import Player
import time

class tictactoe:
	def __init__(self, char):
		self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
		self.player = Player.User_player(char)
		bot_char = 'o' if char == 'x' else 'x'
		self.bot = Player.Bot_player(bot_char)
		self.available_positions = self.set_available_positions()
		self.winner = ''

# |1 | 2 | 3|   1-2-3===> [0,0]-[0,1]-[0,2] , 4-5-6===> [1,0]-[1,1]-[1,2] , 1-5-9===>[0,0]-[1,1]-[2,2]
# |4 | 5 | 6|			7-8-9===> [2,0]-[2,1]-[2,2] , 1-4-7===> [0,0]-[1,0]-[2,0] , 3-5-7===>[0,2]-[1,1]-[2,0]
# |7 | 8 | 9|			2-5-8===> [0,1]-[1,1]-[2,1] , 3-6-9===> [0,2]-[1,2]-[2,2]
	
	def whoWon(self):
		bul = False
		if self.isWon(self.player.moves) :
			self.winner = 'player'
			bul = True

		elif self.isWon(self.bot.moves): 
			self.winner = 'bot'
			bul = True
		return bul
	
	def isWon(self, moves):
		bul = False
# Line1: 1-2-3===> [0,0]-[0,1]-[0,2]
		if self.check_line(moves, [[0,0], [0,1], [0,2]]) :
			bul = True
# Line2: 4-5-6===> [1,0]-[1,1]-[1,2]
		elif self.check_line(moves, [[1,0], [1,1], [1,2]]) :
			bul = True
# Line3: 7-8-9===> [2,0]-[2,1]-[2,2]
		elif self.check_line(moves, [[2,0], [2,1], [2,2]]) :
			bul = True
# Column1: 1-4-7===> [0,0]-[1,0]-[2,0]
		elif self.check_line(moves, [[0,0], [1,0], [2,0]]):
			bul = True
# Column2: 2-5-8===> [0,1]-[1,1]-[2,1] 
		elif self.check_line(moves, [[0,1], [1,1], [2,1]]):
			bul = True
# Column3: 3-6-9===> [0,2]-[1,2]-[2,2]
		elif self.check_line(moves, [[0,2], [1,2], [2,2]]):
			bul = True
# Diagram1 : 1-5-9===>[0,0]-[1,1]-[2,2]
		elif self.check_line(moves, [[0,0], [1,1], [2,2]]):
			bul = True
# Diagram2 : 3-5-7===>[0,2]-[1,1]-[2,0]
		elif self.check_line(moves, [[0,2], [1,1], [2,0]]):
			bul = True
		return bul


	def check_line(self, moves, line_positions) :
		count = 0
		for move in moves:
			if(move in line_positions) :
				count += 1
		return True if count == 3 else False



	def printTheBoard(self, type='simple'):
		list_to_print = self.board
		if type == 'intro':
			list_to_print = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

		print()
		for i in range(len(list_to_print)):
			string = '|'
			for j in range(len(list_to_print[0])):
				string += list_to_print[i][j] + '|'
			print(string.center(30))
		print()

	def set_available_positions(self):
		self.available_positions = [[i, j] for i in range(
			len(self.board)) for j in range(len(self.board[0])) if self.board[i][j] == ' ']
		return self.available_positions

	def get_available_positions(self):
		return list(self.available_positions)

	def updateBoard(self, pos, player):
		self.board[pos[0]][pos[1]] = player.char
		self.set_available_positions()

	def checkInput(self) :
		player_move  = str(input('Please make a move, choose a number between 1 and 9: ')).strip()
		while (player_move not in '123456789' or self.player.retrieve_positions(player_move) not in self.get_available_positions()):
			string = 'Incorrect input, choose a number between 1 and 9: ' if player_move not in '123456789' else 'Incorrect input, position already taken: '
			player_move = str(input(string)).strip()
		return player_move

	def play(self):
		print('Hello player, this is a tic tac toe game!')
		self.printTheBoard('intro')  # Function to print a board

		while (not self.whoWon() and len(self.get_available_positions()) != 0):
			player_move = self.checkInput()

			self.updateBoard(self.player.make_a_move(player_move), self.player)
			self.printTheBoard()
			if self.whoWon() or len(self.get_available_positions()) == 0:
				break

			time.sleep(0.5)
			print('Your opponnent has made a move')
			self.updateBoard(self.bot.make_a_move(self.get_available_positions()), self.bot)
			self.printTheBoard()

		if self.winner == 'player' : print('Congratulations, You have won!')
		elif(self.winner == 'bot') : print('Sorry, You lost...')
		else: print('Its a draw!')


def getChar():
	char = input('Please choose a character (x or o): ').strip()

	while not (char == 'x' or char == 'X' or char == 'O' or char == 'o'):
		char = input('Incorrect input (please enter x or o): ')
	return char


char = getChar()
game = tictactoe(char.lower())
game.play()
