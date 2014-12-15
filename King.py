from Piece import Piece

class King(Piece):
	def __init__(self, name, color, ID, location, deathLoc):
		Piece.__init__(self, name, color, ID, location, deathLoc)

	def updatePosMoves(self, status):
		#Determines possible moves based on location
		self.posMoves = []

		locX = self.location[0]  #The x-coordinate of the piece
		locY = self.location[1]  #The y-coordinate of the piece

		#Possible moves
		#Straight
		stra1 = [locX+1,locY] if self.move_on_board([locX+1,locY]) else None
		stra2 = [locX,locY+1] if self.move_on_board([locX,locY+1]) else None
		stra3 = [locX-1,locY] if self.move_on_board([locX-1,locY]) else None
		stra4 = [locX,locY-1] if self.move_on_board([locX,locY-1]) else None
		#Diagonal
		diag1 = [locX+1,locY+1] if self.move_on_board([locX+1,locY+1]) else None
		diag2 = [locX-1,locY-1] if self.move_on_board([locX-1,locY-1]) else None
		diag3 = [locX-1,locY+1] if self.move_on_board([locX-1,locY+1]) else None
		diag4 = [locX+1,locY-1] if self.move_on_board([locX+1,locY-1]) else None
		moves = [stra1,stra2,stra3,stra4,diag1,diag2,diag3,diag4]

		#Board status of possible move spaces
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

		#Append all possible moves to list if they are legal
		for i in range(len(moves)):
			if stats[i] != "":									#If space on board:
				if stats[i] == None or stats[i].color != self.color:		#Append if space is empty or opponent piece in space
					self.posMoves.append(moves[i])