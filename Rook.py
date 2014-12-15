from Piece import Piece

class Rook(Piece):
	def __init__(self, name, color, ID, location, deathLoc):
		Piece.__init__(self, name, color, ID, location, deathLoc)

	def updatePosMoves(self, status):
		#Determines possible moves based on location
		self.posMoves = []

		locX = self.location[0]  #The x-coordinate of the piece
		locY = self.location[1]  #The y-coordinate of the piece

		#Check booleans
		check_1 = True
		check_2 = True
		check_3 = True
		check_4 = True
		checks = [check_1,check_2,check_3,check_4]

		for i in range(1,8):
			#Potential moves
			stra1 = [locX+i,locY] if self.move_on_board([locX+i,locY]) else None
			stra2 = [locX,locY+i] if self.move_on_board([locX,locY+i]) else None
			stra3 = [locX-i,locY] if self.move_on_board([locX-i,locY]) else None
			stra4 = [locX,locY-i] if self.move_on_board([locX,locY-i]) else None
			moves = [stra1,stra2,stra3,stra4]

			#Board status of potential move spaces
			s1 = status[stra1[0]][stra1[1]] if stra1 != None else ""
			s2 = status[stra2[0]][stra2[1]] if stra2 != None else ""
			s3 = status[stra3[0]][stra3[1]] if stra3 != None else ""
			s4 = status[stra4[0]][stra4[1]] if stra4 != None else ""
			stats = [s1,s2,s3,s4]

			#Append potential moves to list of possible moves if they are legal
			for i in range(len(moves)):
				if checks[i] and stats[i] != "":			#If still checking this direction, and space is on board:
					if stats[i] == None:						#Append if space is empty and continue checking this direction
						self.posMoves.append(moves[i])
					elif stats[i].color != self.color:		#Append if opponent piece in space, then stop checking this direction
						self.posMoves.append(moves[i])
						checks[i] = False
					else:									#Do not append if own piece in space, then stop checking this direction
						checks[i] = False