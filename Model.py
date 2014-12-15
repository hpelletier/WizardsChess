import sys
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King
from Speech import Speech
from View import Mover

class Board():
	def __init__(self):
		self.rep_status = [[0 for x in xrange(10)] for x in xrange(11)]  	  #Array of board representation (piece short-names and 0s)
		self.piece_status = [[None for x in xrange(10)] for x in xrange(11)]  #Array of board representation (piece objects and Nones)
		self.sp = Speech()
		self.mover = Mover()

		#Initialize all the black pieces 
		self.blackPawn0 = Pawn("pawn", "black", 1, [2,2], [10,0])
		self.blackPawn1 = Pawn("pawn", "black", 2, [3,2], [10,1])
		self.blackPawn2 = Pawn("pawn", "black", 3, [4,2], [10,2])
		self.blackPawn3 = Pawn("pawn", "black", 4, [5,2], [10,3])
		self.blackPawn4 = Pawn("pawn", "black", 5, [6,2], [10,6])
		self.blackPawn5 = Pawn("pawn", "black", 6, [7,2], [10,7])
		self.blackPawn6 = Pawn("pawn", "black", 7, [8,2], [10,8])
		self.blackPawn7 = Pawn("pawn", "black", 8, [9,2], [10,9])
		self.blackBishop0 = Bishop("bishop", "black", 1, [4,1], [10,4])
		self.blackBishop1 = Bishop("bishop", "black", 2, [7,1], [10,5])
		self.blackKnight0 = Knight("knight", "black", 1, [3,1], [1,2])
		self.blackKnight1 = Knight("knight", "black", 2, [8,1], [1,3])
		self.blackRook0 = Rook("rook", "black", 1, [2,1], [1,0])
		self.blackRook1 = Rook("rook", "black", 2, [9,1], [1,1])
		self.blackQueen = Queen("queen", "black", 1, [5,1], [1,4])
		self.blackKing = King("king", "black", 1, [6,1], [1,4])

		#Initialize all the white pieces
		self.whitePawn0 = Pawn("pawn", "white", 1, [2,7], [0,0])
		self.whitePawn1 = Pawn("pawn", "white", 2, [3,7], [0,1])
		self.whitePawn2 = Pawn("pawn", "white", 3, [4,7], [0,2])
		self.whitePawn3 = Pawn("pawn", "white", 4, [5,7], [0,3])
		self.whitePawn4 = Pawn("pawn", "white", 5, [6,7], [0,6])
		self.whitePawn5 = Pawn("pawn", "white", 6, [7,7], [0,7])
		self.whitePawn6 = Pawn("pawn", "white", 7, [8,7], [0,8])
		self.whitePawn7 = Pawn("pawn", "white", 8, [9,7], [0,9])
		self.whiteBishop0 = Bishop("bishop", "white", 1, [4,8], [0,4])
		self.whiteBishop1 = Bishop("bishop", "white", 2, [7,8], [0,5])
		self.whiteKnight0 = Knight("knight", "white", 1, [3,8], [1,6])
		self.whiteKnight1 = Knight("knight", "white", 2, [8,8], [1,7])
		self.whiteRook0 = Rook("rook", "white", 1, [2,8], [1,8])
		self.whiteRook1 = Rook("rook", "white", 2, [9,8], [1,9])
		self.whiteQueen = Queen("queen", "white", 1, [5,8], [1,5])
		self.whiteKing = King("king", "white", 1, [6,8], [1,5])

		#Add all the black pieces to an array
		self.blackPieces = [self.blackPawn0,self.blackPawn1,self.blackPawn2,self.blackPawn3,self.blackPawn4,self.blackPawn5,self.blackPawn6,self.blackPawn7,self.blackRook0,self.blackRook1,self.blackKnight0,self.blackKnight1,self.blackBishop0,self.blackBishop1,self.blackQueen,self.blackKing]

		#Add all the white pieces to an array
		self.whitePieces = [self.whitePawn0,self.whitePawn1,self.whitePawn2,self.whitePawn3,self.whitePawn4,self.whitePawn5,self.whitePawn6,self.whitePawn7,self.whiteRook0,self.whiteRook1,self.whiteKnight0,self.whiteKnight1,self.whiteBishop0,self.whiteBishop1,self.whiteQueen,self.whiteKing]

		#Add all the pieces of both colors to an array
		self.pieces = []
		self.pieces.extend(self.blackPieces)
		self.pieces.extend(self.whitePieces)
		

	def updateBoard(self):
		#Clear current board status before setting new status
		self.rep_status = [[0 for x in xrange(10)] for x in xrange(11)]
		self.piece_status = [[None for x in xrange(10)] for x in xrange(11)]

		#Place the pieces within the status arrays based on their locations on the board
		for piece in self.pieces:
			x = piece.location[0]
			y = piece.location[1]			
			self.rep_status[x][y] = piece.name[0:2].capitalize() + piece.color[0].capitalize() + str(piece.ID)  
			self.piece_status[x][y] = piece


	def updatePosMoves(self,player):
		#Update the possible moves of a player's pieces
		if player =="black":
			pieces = self.blackPieces
		elif player =="white":
			pieces = self.whitePieces
		for piece in pieces:
			piece.updatePosMoves(self.piece_status)


	def movePiece(self,player,move):
		#Update piece locations based on given move
		if len(move) == 3:								 #If a Standard Move:
			kind = move[0]								 #Kind of piece to be moved
			ID = move[1]								 #ID of piece to be moved
			destination = move[2]						 #Final destination of piece to be moved
			dest0 = destination[0]						 #X component of destination
			dest1 = destination[1]						 #Y component of destination
			dest_piece = self.piece_status[dest0][dest1] #Piece at destination (may be None)
			castle = False

		elif len(move) == 2:							 #If a Castle Move:			
			direction = move[0]							 #Direction of castle
			kind = "rook"								 #Kind of piece to be moved
			if direction == "queenside":				 #ID of piece to be moved
				ID = 1
			elif direction == "kingside":
				ID = 2		
			castle = True

		if player == "white": 						 
			king_piece = self.whiteKing				 #Which king to be moved
			other_pieces = self.blackPieces			 #Which pieces are other player's
			other_player = "black"
			row = 7
		elif player == "black":
			king_piece = self.blackKing
			other_pieces = self.whitePieces
			other_player = "white"	
			row = 0

		move_piece = None 							 #Piece to be moved
		move_piece_index = 0 						 #Index of piece to be moved

	    #Assign piece to be moved and its index in pieces list
		for i in range(len(self.pieces)):
			piece = self.pieces[i]
			if piece.color == player and piece.name == kind and piece.ID == ID:
				move_piece = piece
				move_piece_index = i
				break

		#If the move is NOT a Castle move:
		if not castle:
			#Try to move the piece
			if move_piece != None:											#Check if piece is a real piece
				if not move_piece.isDead():									#Check if piece is still in play						
					if destination in move_piece.posMoves:					#Check if destination in piece's possible moves

						#See if the moving piece is a king
						if move_piece.name == "king":
							check_dest = destination
						else:
							check_dest = king_piece.location

						#See if the king is in check
						king_in_check = self.check(other_pieces,king_piece.location)

						#Move the piece to its possible destination				
						hold_piece_status = self.piece_status
						self.piece_status[dest0][dest1] = move_piece
						self.updatePosMoves(other_player)

						#See if the king is now in check
						#If it is, do not make the move, and inform the player why
						if self.check(other_pieces,check_dest):							
							if not king_in_check:
								self.sp.engine.say("Move not possible. King would be in check.")
								self.sp.engine.runAndWait()							
								print "Move not possible. King would be in check."
							else:
								self.sp.engine.say("Move not possible. King must be taken out of check.")
								self.sp.engine.runAndWait()							
								print "Move not possible. King must be taken out of check."
							self.piece_status = hold_piece_status
							self.updateBoard()
							self.updatePosMoves(other_player)
							return False

						#If it can't be taken, make the move
						else:
							self.piece_status = hold_piece_status
							self.updateBoard()
							self.updatePosMoves(other_player)
							if dest_piece != None:								#If there is a piece at the destination:			
								dest_piece.explode(self.mover,self.sp)			#Send that piece to its death location

							move_piece.move(self.mover,self.sp,destination,self.piece_status,False)	#Move the piece to its destination

							if move_piece.name == "pawn":						#If the piece is a pawn at the oppostite end of the board:
								if ((move_piece.color == "black" and move_piece.location[1] == 8) or 
										(move_piece.color == "white" and move_piece.location[1] == 1)):
									newPiece = self.transformPiece(move_piece)	#Transform the piece (make a queen, etc. with same attributes)
									self.pieces[move_piece_index] = newPiece	#Replace the old piece with the new piece
							return True
							
					else:													#Return false if destination not in piece's possible moves
						self.sp.engine.say("That move is not possible.")
						self.sp.engine.runAndWait()							
						print "That move is not possible."
						return False
				else:														#Return false if piece is in its death location
					self.sp.engine.say("That piece is dead.")
					self.sp.engine.runAndWait()								
					print "That piece is dead."
				return False
			else:															#Return false if piece is not on board (not real)
				self.sp.engine.say("That is not a valid piece.")
				self.sp.engine.runAndWait()	
				print "That is not a valid piece."
				return False

		#If the move IS a Castle move:	
		else:
			if not move_piece.isDead():										#Check if piece is still in play
				if not king_piece.hasMoved:									#Check if the king has moved before
					if not move_piece.hasMoved:								#Check if the rook has moved before
						if direction == "queenside":
							for i in range(1,4):
								if self.piece_status[king_piece.location[0]-i][row] != None:
									self.sp.engine.say("Castle not possible. Space between rook and king not empty.")
									self.sp.engine.runAndWait()								
									print "Castle not possible. Space between rook and king not empty."
									return False
							for i in range(0,3):
								if self.check(other_pieces,[king_piece.location[0]-i,row]):									
									self.sp.engine.say("Castle not possible. King is or would be in check.")
									self.sp.engine.runAndWait()								
									print "Castle not possible. King is or would be in check."
									return False									
							
							king_piece.move(self.mover,self.sp,(king_piece.location[0]-2,row),self.piece_status,False)
							move_piece.move(self.mover,self.sp,(move_piece.location[0]+3,row),self.piece_status,True)
							return True

						elif direction == "kingside":
							for i in range(1,3):
								if self.piece_status[king_piece.location[0]+i][row] != None:
									self.sp.engine.say("Castle not possible. Space between rook and king is not empty.")
									self.sp.engine.runAndWait()								
									print "Castle not possible. Space between rook and king not empty."
									return False
							for i in range(0,3):
								if self.check(other_pieces,[king_piece.location[0]+i,row]):
									self.sp.engine.say("Castle not possible. King is or would be in check.")
									self.sp.engine.runAndWait()
									print "Castle not possible. King is or would be in check."
									return False

							king_piece.move(self.mover,self.sp,[king_piece.location[0]+2,row],self.piece_status,False)
							move_piece.move(self.mover,self.sp,[move_piece.location[0]-2,row],self.piece_status,True)
							return True							
					else:
						self.sp.engine.say("Castle not possible. That rook has previously moved.")
						self.sp.engine.runAndWait()								
						print "Castle not possible. That rook has previously moved."
						return False
				else:
					self.sp.engine.say("Castle not possible. The king has previously moved.")
					self.sp.engine.runAndWait()								
					print "Castle not possible. The king has previously moved."
					return False
			else:														#Return False if piece is in its death location
				self.sp.engine.say("That rook is dead.")
				self.sp.engine.runAndWait()								
				print "That rook is dead."
				return False


	def transformPiece (self,pawn):
		#Ask the player what kind of piece they want their pawn to turn into
		self.sp.engine.say("What piece will your pawn become? Queen, bishop, knight, or rook?")
		self.sp.engine.runAndWait()

		#Get the kind of piece from the player
		newPiece = raw_input("What piece will your pawn become: queen, bishop, knight, or rook?").lower()
		while newPiece != 'queen' and newPiece != 'bishop' and newPiece != 'knight' and newPiece != 'rook':
			self.sp.engine.say("A piece can only become a queen, bishop, knight, or rook. Try again.")
			self.sp.engine.runAndWait()
			newPiece = raw_input("A piece can only become a queen, bishop, knight, or rook. Try again.").lower()

		#Get the relevant attributes of the pawn
		col = pawn.color
		loc = pawn.location
		dloc = pawn.deathLoc

		#See how many instances of that kind of piece there are
		in_play = 0		
		for piece in self.pieces:
			if piece.color == col and piece.name == newPiece:
				in_play += 1

		#Create and return an instance of the new "transformed" piece
		if newPiece == "queen":
			return Queen(newPiece,col,in_play+1,loc,dloc)
		elif newPiece == "rook":
			return Rook(newPiece,col,in_play+1,loc,dloc)
		elif newPiece == "knight":
			return Knight(newPiece,col,in_play+1,loc,dloc)
		elif newPiece == "bishop":
			return Bishop(newPiece,col,in_play+1,loc,dloc)


	def check(self,other_pieces,king_loc):		
		for piece in other_pieces:
			if king_loc in piece.posMoves:	
				return True
		return False


	def continuePlay(self,player):
		#Get important values for relevant player
		if player == "white":
			king = self.whiteKing
			king_loc = self.whiteKing.location			
			king_pos_moves = self.whiteKing.posMoves
			other_pieces = self.blackPieces	
			other_player = "black"		
		elif player == "black":
			king = self.blackKing
			king_loc = self.blackKing.location			
			king_pos_moves = self.blackKing.posMoves
			other_pieces = self.whitePieces	
			other_player ="white"
		check = False
		checkmate = False

		#See if the king is in check
		check = self.check(other_pieces,king_loc)

		#If the king is in check, see if it is in checkmate
		if check:
			hold_piece_status = self.piece_status 			#Save the current state of the board
			open_spaces = len(king_pos_moves)			#Number of possible moves of king
			threatened_spaces = 0 						#Number of threatened pos moves

			#Move the king to each of its possible moves
			for loc in king_pos_moves:				
				self.piece_status = hold_piece_status
				self.piece_status[loc[0]][loc[1]] = king 
				self.updatePosMoves(other_player)

				#See if the king can be taken in that location
				if self.check(other_pieces,loc):
					threatened_spaces += 1			

			#If the king can be taken in all of its possible moves, it is in checkmate
			if open_spaces == threatened_spaces:
				checkmate = True

			#Set the board back to its original status
			self.piece_status = hold_piece_status
			self.updateBoard()
			self.updatePosMoves(other_player)
								
		#If the king is in checkmate
		if checkmate:
			self.sp.engine.say("CHECKMATE!")
			self.sp.engine.runAndWait()
			print 'CHECKMATE!'		#Let the player know the king is in checkmate
			return 0 				#End the game

		#If the king is in check
		elif check:
			self.sp.engine.say("CHECK!")
			self.sp.engine.runAndWait()
			print 'CHECK!'					#Let the player know if the king is in check							
			return 1 						#If the king is not in checkmate, continue the game
		
		return 1 	#Continue play


	def printBoard(self):
		#Print a representation of the board to the console
		cols = ['X','X','.','A','B','C','D','E','F','G','H','.','X']
		rows = ['X','8','7','6','5','4','3','2','1','X']
		print ""
		sys.stdout.write(' '*5)
		for c in range(13):
			sys.stdout.write(cols[c]+' '*5)
		print ""
		print ""
		for i in range(10):
			sys.stdout.write(rows[i]+' '*4)
			for j in range(0,2):
				piece = str(self.rep_status[j][i])
				sys.stdout.write(piece + ' '*(6-len(piece)))
			sys.stdout.write('.     ')
			for j in range(2,10):
				piece = str(self.rep_status[j][i])
				sys.stdout.write(piece + ' '*(6-len(piece)))
			sys.stdout.write('.     ')
			for j in range(10,11):
				piece = str(self.rep_status[j][i])
				sys.stdout.write(piece + ' '*(6-len(piece)))
			print ""
			print ""
