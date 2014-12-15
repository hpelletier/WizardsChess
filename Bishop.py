from Piece import Piece

class Bishop(Piece):
	def __init__(self, name, color, ID, location, deathLoc):
		Piece.__init__(self, name, color, ID, location, deathLoc)

	def updatePosMoves(self, status):
		#Determines possible moves based on location
		self.posMoves = []

		locX = self.location[0]  #The x-coordinate of the piece
		locY = self.location[1]  #The y-coordinate of the piece

		#Diagonal check booleans
		check_1 = True
		check_2 = True
		check_3 = True
		check_4 = True
		checks = [check_1,check_2,check_3,check_4]

		for i in range(1,8):
			#Potential moves
			diag1 = [locX+i,locY+i] if self.move_on_board([locX+i,locY+i]) else None
			diag2 = [locX-i,locY-i] if self.move_on_board([locX-i,locY-i]) else None
			diag3 = [locX-i,locY+i] if self.move_on_board([locX-i,locY+i]) else None
			diag4 = [locX+i,locY-i] if self.move_on_board([locX+i,locY-i]) else None
			moves = [diag1,diag2,diag3,diag4]

			#Board status of potential move spaces
			d1 = status[diag1[0]][diag1[1]] if diag1 != None else ""
			d2 = status[diag2[0]][diag2[1]] if diag2 != None else ""
			d3 = status[diag3[0]][diag3[1]] if diag3 != None else ""
			d4 = status[diag4[0]][diag4[1]]	if diag4 != None else ""
			stats = [d1,d2,d3,d4]

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