from Piece import Piece

class Knight(Piece):
	def __init__(self, name, color, ID, location, deathLoc):
		Piece.__init__(self, name, color, ID, location, deathLoc)

	def updatePosMoves(self, status):
		#Determines possible moves based on location
		self.posMoves = []

		locX = self.location[0]  #The x-coordinate of the piece
		locY = self.location[1]  #The y-coordinate of the piece

		#Possible moves
		move1 = [locX+2,locY+1] if self.move_on_board([locX+2,locY+1]) else None
		move2 = [locX+2,locY-1] if self.move_on_board([locX+2,locY-1]) else None
		move3 = [locX-2,locY+1] if self.move_on_board([locX-2,locY+1]) else None
		move4 = [locX-2,locY-1] if self.move_on_board([locX-2,locY-1]) else None
		move5 = [locX+1,locY+2] if self.move_on_board([locX+1,locY+2]) else None
		move6 = [locX-1,locY+2] if self.move_on_board([locX-1,locY+2]) else None
		move7 = [locX+1,locY-2] if self.move_on_board([locX+1,locY-2]) else None
		move8 = [locX-1,locY-2] if self.move_on_board([locX-1,locY-2]) else None
		moves = [move1,move2,move3,move4,move5,move6,move7,move8]

		#Board status of potential move spaces
		m1 = status[move1[0]][move1[1]] if move1 != None else ""
		m2 = status[move2[0]][move2[1]] if move2 != None else ""
		m3 = status[move3[0]][move3[1]] if move3 != None else ""
		m4 = status[move4[0]][move4[1]] if move4 != None else ""
		m5 = status[move5[0]][move5[1]] if move5 != None else ""
		m6 = status[move6[0]][move6[1]] if move6 != None else ""
		m7 = status[move7[0]][move7[1]] if move7 != None else ""
		m8 = status[move8[0]][move8[1]] if move8 != None else ""
		stats = [m1,m2,m3,m4,m5,m6,m7,m8]

		#Append all potential moves to list if they are legal
		for i in range(len(moves)):
			if stats[i] != "":										#If space on board:
				if stats[i] == None or stats[i].color != self.color:	#Append if space is empty or opponent piece in space
					self.posMoves.append(moves[i])