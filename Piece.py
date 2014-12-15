class Piece():
	def __init__(self, name, color, ID, location, deathLoc):
		self.name = name
		self.color = color
		self.ID = ID
		self.location = location	
		self.deathLoc = deathLoc
		self.hasMoved = False
		self.posMoves = [] #List of possible moves

	def isDead(self):
		if self.location == self.deathLoc:
			return True
		return False


	def move(self, mover, speech, newLocation, status, castle):
		#Send the motor command to move the piece
		mover.movePiece(self.location,newLocation,self.name,castle)

		#Update the board status of the piece
		self.location = newLocation
		self.hasMoved = True


	def explode(self, mover, speech):
		#Send the motor command to move the piece
		mover.moveToDeath(self.location,self.deathLoc)

		#Update the board status of the piece
		self.location = self.deathLoc

		#Announce the death of the piece
		speech.engine.say(self.color + ' ' + self.name + ' ' + str(self.ID) + ' has fallen!')
		speech.engine.runAndWait()
		print self.color.capitalize() + ' ' + self.name.capitalize() + ' ' + str(self.ID) + ' has fallen!'


	def updatePosMoves(self,status):
		#Defined specifically for each piece
		#Determines the available moves for a piece based on its type and location
		pass

	def updateLocation(self,newLocation):
		#Sets a new location for a piece
		self.location = newLoc

	def move_on_board(self,move):
		#Checks if a given move is on the board
		if move[0] >= 2 and move[0] <= 9:
			if move[1] >= 1 and move[1] <= 8:
				return True
		return False