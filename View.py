import time
import serial
from Control import Control

#Degs between squares
XCONSTANT = 130; #Multiplied by 2 in Arduino
YCONSTANT = 130; #Multiplied by 2 in Arduino
 
class Mover():
	def __init__(self):
		self.motorShield = MotorShield()

	def movePiece(self, curPos, newPos, pieceType, castle):
		curPosX = curPos[0]
		curPosY = curPos[1]
		newPosX = newPos[0]
		newPosY = newPos[1]
		pieceType = pieceType.lower()		

		#Move the carriage to the correct piece
		self.motorShield.move(curPosX,curPosY,2)

		#Move the piece in the Y direction
		if curPosX == newPosX and curPosY != newPosY:
			self.motorShield.move("",newPosY,1)

		#Move the piece in the X direction
		elif curPosX != newPosX and curPosY == newPosY:
			if not castle:
				self.motorShield.move(newPosX,"",1)
			else:
				self.motorShield.move("",curPosY+0.5,1) #Move it between squares
				self.motorShield.move(newPosX,"",1)		#Move it in the X direction
				self.motorShield.move("",curPosY,1)		#Move it in the Y direction

		#Move the piece in both directions
		elif curPosX != newPosX and curPosY != newPosY:
			#If the piece is not a knight:
			if pieceType != "knight":
				self.motorShield.move(newPosX,newPosY,1)			
			else:  #If the piece is a knight:		
				self.motorShield.move(curPosX-0.5,curPosY-0.5,1)	#Move it between squares
				self.motorShield.move("",newPosY+0.5,1)				#Move it in the Y direction & between sqaures
				self.motorShield.move(newPosX,"",1)					#Move it in the X direction
				self.motorShield.move("",newPosY,1)					#Move it back to center of square

	def moveToDeath(self,curPos,deathPos):
		curPosX = curPos[0]
		curPosY = curPos[1]
		centerPosY = 4
		deathPosX = deathPos[0]
		deathPosY = deathPos[1]

		#Move the carriage to the correct piece
		self.motorShield.move(curPosX,curPosY,2)

		#Move the piece between squares
		self.motorShield.move(curPosX+0.5,curPosY+0.5,1)	#Move it between squares

		#Move the carriage to the center of the board
		self.motorShield.move("",centerPosY+0.5,1)

		#Move it in the X direction
		self.motorShield.move(deathPosX+0.5,"",1)

		#Move it in the Y direction		
		self.motorShield.move("",deathPosY,1)

		#Move it back to the center of the square
		self.motorShield.move(deathPosX,"",1)


class MotorShield():
	def __init__(self):
		#Zero carriage and turn off magnet	
		self.curXPos = 0
		self.curYPos = 0
		self.curMag = 2

		#Connect to the correct serial port
		serialPorts = ["/dev/ttyACM0","/dev/ttyACM1","/dev/ttyACM2","/dev/ttyACM3","/dev/ttyACM4","/dev/ttyACM5"]
		for port in serialPorts:
			try:
				self.ser = serial.Serial(port, 9600)
				print "Connected to port " + port
				time.sleep(2)
				break
			except:
				pass
		else:
			print "Could not connect to serial port. Please check the Arduino connection and try again."


	def move(self,newXPos,newYPos,newMag):
		#Refresh values
		xdir = 1
		ydir = 1
		xdist = 0
		ydist = 0

		#Deal with the X direction and distance
		if newXPos != "":
			if newXPos - self.curXPos >= 0:
				xdir = 1 #forward
			else:
				xdir = 2 #backwards				
			xdist = abs(newXPos-self.curXPos)*XCONSTANT

		#Deal with the Y direction and distance
		if newYPos != "":
			if newYPos - self.curYPos >= 0:
				ydir = 1 #forward
			else:
				ydir = 2 #backwards	
			ydist = abs(newYPos-self.curYPos)*YCONSTANT
		
		try:
			#Build and send the serial command
			command = int(100000000*newMag + 10000000*xdir + 10000*xdist + 1000*ydir + ydist)
			self.ser.write(str(command))

			#Wait for Arduino to carry out command
			not_read = True
			while not_read:
				if self.ser.readline() == "Done\n":
					not_read = False

			#Update the current state of the carriage
			self.curMag = newMag
			if newXPos != "":
				self.curXPos = newXPos
			if newYPos != "":
				self.curYPos = newYPos

		except:
			print "Serial command could not be sent. Please check the Arduino connection and try again."
