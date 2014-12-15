from Piece import Piece

class Queen(Piece):
	def __init__(self, name, color, ID, location, deathLoc):
		Piece.__init__(self, name, color, ID, location, deathLoc)
		self.posMoves = [] #List of possible moves

	def updatePosMoves(self, status):
		#Determines possible moves based on location
		self.posMoves = []

		locX = self.location[0]  #The x-coordinate of the piece
		locY = self.location[1]  #The y-coordinate of the piece

		#Straight check booleans
		s_check_1 = True
		s_check_2 = True
		s_check_3 = True
		s_check_4 = True
		#Diagonal check booleans
		d_check_1 = True
		d_check_2 = True
		d_check_3 = True
		d_check_4 = True
		checks = [s_check_1,s_check_2,s_check_3,s_check_4,d_check_1,d_check_2,d_check_3,d_check_4]

		for i in range(1,8):
			#Potential moves
			#Straight
			stra1 = [locX+i,locY] if self.move_on_board([locX+i,locY]) else None
			stra2 = [locX,locY+i] if self.move_on_board([locX,locY+i]) else None
			stra3 = [locX-i,locY] if self.move_on_board([locX-i,locY]) else None
			stra4 = [locX,locY-i] if self.move_on_board([locX,locY-i]) else None
			#Diagonal
			diag1 = [locX+i,locY+i] if self.move_on_board([locX+i,locY+i]) else None
			diag2 = [locX-i,locY-i] if self.move_on_board([locX-i,locY-i]) else None
			diag3 = [locX-i,locY+i] if self.move_on_board([locX-i,locY+i]) else None
			diag4 = [locX+i,locY-i] if self.move_on_board([locX+i,locY-i]) else None
			moves = [stra1,stra2,stra3,stra4,diag1,diag2,diag3,diag4]

			#Board status of potential move spaces
			#Straight
			s1 = status[stra1[0]][stra1[1]] if stra1 != None else ""
			s2 = status[stra2[0]][stra2[1]] if stra2 != None else ""
			s3 = status[stra3[0]][stra3[1]] if stra3 != None else ""
			s4 = status[stra4[0]][stra4[1]] if stra4 != None else ""
			#Diagonal
			d1 = status[diag1[0]][diag1[1]] if diag1 != None else ""
			d2 = status[diag2[0]][diag2[1]] if diag2 != None else ""
			d3 = status[diag3[0]][diag3[1]] if diag3 != None else ""
			d4 = status[diag4[0]][diag4[1]]	if diag4 != None else ""
			stats = [s1,s2,s3,s4,d1,d2,d3,d4]

			#Append potential moves to list of possible moves if they are legal
			for j in range(len(moves)):
				if checks[j] and stats[j] != "":			#If still checking this direction, and space is on board:
					if stats[j] == None:						#Append if space is empty and continue checking this direction
						self.posMoves.append(moves[j])
					elif stats[j].color != self.color:		#Append if opponent piece in space, then stop checking this direction
						self.posMoves.append(moves[j])
						checks[j] = False
					else:									#Do not append if own piece in space, then stop checking this direction
						checks[j] = False