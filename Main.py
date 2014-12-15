import sys
from Model import Board
from View import Mover
from Control import Control
from Speech import Speech

class Game():
	def __init__(self):
		self.gameState = 1			#State of game: 1 if playing, 0 if game over
		self.player = 'white'		#Current player: white player always starts
		self.board = Board()		#The board representation
		self.control = Control()	#The control that handles user input
		self.sp = Speech()			#The verbal feedback given by the computer

	def play(self):
		#What happens when the game is started:
		self.sp.engine.say("Welcome to Wizard's Chess!")
		self.sp.engine.runAndWait()	
		print ""
		print "*~*~*~*~*~*~*~*~*~*       Welcome to Wizard's Chess!       *~*~*~*~*~*~*~*~*~*"
		print "*~*~*~*~*~*~*~*~*~*  Input is of the form 'Knight 1 to H3'  *~*~*~*~*~*~*~*~*~*\n"
		self.board.updateBoard()
		self.board.printBoard()  #Print the board so the player can make their first move

		#The game loop: runs continuously until the game is over
		while self.gameState == 1:
			self.board.updatePosMoves(self.player)									#Update the possible moves of the player's pieces
			#move = self.control.getKeyboardInput(self.player.capitalize())			#Get the desired move from user (keyboard) input
			move = self.control.getVoiceInput(self.player.capitalize())
			if move:																#If the user input is valid:
				success = self.board.movePiece(self.player,move)	 				#Try to move the piece
			while not move or not success:											#While the user input isn't valid or the piece can't be moved:
				#move = self.control.getKeyboardInput(self.player.capitalize())		#Get new user input until both conditions are satisfied
				move = self.control.getVoiceInput(self.player.capitalize())
				if move:
					success = self.board.movePiece(self.player,move)
			self.board.updateBoard()												#Once input is valid and piece is successfully moved:
			self.board.printBoard()													#Print the board to the console
			self.board.updatePosMoves(self.player)									#Update the possible moves of the player's pieces
			self.player = self.other(self.player)									#Switch players
			self.gameState = self.board.continuePlay(self.player)					#Check to see if the game is over
			
		#Terminate the program once the game is over
		self.sp.engine.say(self.player + " player loses!")
		self.sp.engine.runAndWait()
		print self.player.capitalize() + " player loses!"
		sys.exit(0)

	def other(self,player):
		#Return the name of the other player
		if player == 'white':
			return 'black'
		if player == 'black':
			return 'white'

game = Game()
game.play()
