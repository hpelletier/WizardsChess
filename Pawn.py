from Piece import Piece
from Speech import Speech

class Pawn(Piece):
	def __init__(self, name, color, ID, location, deathLoc):
		Piece.__init__(self, name, color, ID, location, deathLoc)
		self.just_moved_two = False
		self.updates_since_moved_two = 0
		self.on_fifth_rank = False
		self.can_en_passant_left = False
		self.can_en_passant_right = False
		
	def updatePosMoves(self, status):
		#Determines possible moves based on location
		self.posMoves = []

		locX = self.location[0]  #The x-coordinate of the piece
		locY = self.location[1]  #The y-coordinate of the piece

		if self.just_moved_two:
			self.updates_since_moved_two += 1
 		
 		#Reset values
 		if self.updates_since_moved_two >= 4:		
 			self.just_moved_two = False
 			self.updates_since_moved_two = 0
		self.can_en_passant_left = False
		self.can_en_passant_right = False

		#Potential moves for a white piece
		if self.color == "white":      
			one_ahead = [locX,locY-1] if self.move_on_board([locX,locY-1]) else None
			two_ahead = [locX,locY-2] if self.move_on_board([locX,locY-2]) else None
			left_diag = [locX-1,locY-1] if self.move_on_board([locX-1,locY-1]) else None
			right_diag = [locX+1,locY-1] if self.move_on_board([locX+1,locY-1]) else None
			if self.on_fifth_rank:
				left_en_passant = [locX-1,locY] if self.move_on_board([locX-1,locY]) else None
				right_en_passant = [locX+1,locY] if self.move_on_board([locX+1,locY]) else None

		#Potential moves for a black piece
		elif self.color == "black":     
			one_ahead = [locX,locY+1] if self.move_on_board([locX,locY+1]) else None
			two_ahead = [locX,locY+2] if self.move_on_board([locX,locY+2]) else None
			left_diag = [locX-1,locY+1] if self.move_on_board([locX-1,locY+1]) else None
			right_diag = [locX+1,locY+1] if self.move_on_board([locX+1,locY+1]) else None
			if self.on_fifth_rank:
				left_en_passant = [locX-1,locY] if self.move_on_board([locX-1,locY]) else None
				right_en_passant = [locX+1,locY] if self.move_on_board([locX+1,locY]) else None

		#Board status of potential move spaces
		oa = status[one_ahead[0]][one_ahead[1]] if one_ahead != None else ""
		ta = status[two_ahead[0]][two_ahead[1]] if two_ahead != None else ""
		ld = status[left_diag[0]][left_diag[1]] if left_diag != None else ""
		rd = status[right_diag[0]][right_diag[1]] if right_diag != None else ""
		if self.on_fifth_rank:
			lep = status[left_en_passant[0]][left_en_passant[1]] if left_en_passant != None else ""
			rep = status[right_en_passant[0]][right_en_passant[1]] if right_en_passant != None else ""

		#Append potential moves to list of possible moves if they are legal
		if oa == None:																	#Append space one-ahead if on board and empty
			self.posMoves.append(one_ahead)
		if ta == None and not self.hasMoved:											#Append space two-ahead if on board and empty, and piece at starting location
			self.posMoves.append(two_ahead)
		if ld != "" and ld != None:														#Append space left-diagonal if on board and opponent piece in space	
		 	self.posMoves.append(left_diag) if ld.color != self.color else 0
		if rd != "" and rd != None:														#Append space right-diagonal if on board and opponent piece in space
			self.posMoves.append(right_diag) if rd.color != self.color else 0
		if self.on_fifth_rank:																#If the pawn is in position to en passant:															
			if lep != "" and lep != None and lep.name == "pawn" and lep.just_moved_two:		#Append space left-diagonal if on board and opponent pawn that just moved two in space
				self.posMoves.append(left_diag) if lep.color != self.color else 0
				self.can_en_passant_left = True
			if rep != "" and rep != None and rep.name == "pawn" and rep.just_moved_two:		#Append space right-diagonal if on board and opponent pawn that just moved two in space
				self.posMoves.append(right_diag) if rep.color != self.color else 0
				self.can_en_passant_right = True


	#Override move function to add en passant rules
	def move(self, mover, speech, newLocation, status, castle):

		#Check if the pawn is moving two spaces
		if (newLocation[1] == self.location[1]-2 and self.color == "white") or (newLocation[1] == self.location[1]+2 and self.color =="black"):
			self.just_moved_two = True

		#Check if the pawn is moving to its fifth rank
		self.on_fifth_rank = False
		if (newLocation[1] == 5 and self.color == "black") or (newLocation[1] == 4 and self.color == "white"):
			self.on_fifth_rank = True

		#If piece is performing en passant, explode the correct piece
		if self.can_en_passant_right:
			if self.color == "white" and newLocation[0] == self.location[0]+1 and newLocation[1] == self.location[1]-1:
				piece = status[self.location[0]+1][self.location[1]]
				piece.explode(mover,speech)
			elif self.color == "black" and newLocation[0] == self.location[0]+1 and newLocation[1] == self.location[1]+1:
				status[self.location[0]+1][self.location[1]]
				piece.explode(mover,speech)
		if self.can_en_passant_left:
			if self.color == "white" and newLocation[0] == self.location[0]-1 and newLocation[1] == self.location[1]-1:
				piece = status[self.location[0]-1][self.location[1]]
				piece.explode(mover,speech)
			elif self.color == "black" and newLocation[0] == self.location[0]-1 and newLocation[1] == self.location[1]+1:
				piece = status[self.location[0]-1][self.location[1]]
				piece.explode(mover,speech)

		#Send the motor command to move the piece
		mover.movePiece(self.location,newLocation,self.name,castle)

		#Update the board status of the piece
		self.location = newLocation
		self.hasMoved = True