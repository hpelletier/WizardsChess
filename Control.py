from Speech import Speech
import speech_recognition as sr
import SoundTest


class Control():
	def __init__(self):
		self.input = ""
		self.translated = []
		self.sp = Speech()

		#Dictionary mapping column and row names to ints
		self.cols = {'a':2,'b':3,'c':4,'d':5,'e':6,'f':7,'g':8,'h':9}
		self.rows = {'1':8,'2':7,'3':6,'4':5,'5':4,'6':3,'7':2,'8':1}


	def listen():
		call(["amixer", "set", "Capture", "70"])
		call(["arecord", '-f', 'dat', '-c', '1', '-D', 'hw:0,0', '-d', '5', '-V', 'mono', 'test.wav'])
		r = sr.Recognizer(language = "en-US", key = "AIzaSyB5HMzhJDY9iKLLku6_gQRGleTmFgiq4Ec")
		
		with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
		    audio = r.record(source)                        # extract audio data from the file
		try:
			return r.recognize(audio)
		except:
			return None


	def getKeyboardInput(self,player):
		#Get input from the player and return the translated move
		#Turn is of the form "Piece ID to Location"
		#Ex: Knight 2 A4

		self.sp.engine.say(player + " player, your move.")
		self.sp.engine.runAndWait()

		self.input = str(raw_input(player + " player, your move.\n\n"))

		return self.translate()


	def getVoiceInput(self,player):
		while True: 
			self.sp.engine.say(player + " player, your move. Press enter to speak.")
			self.sp.engine.runAndWait()

			cont = str(raw_input(player + " player, your move. Press enter to speak.\n\n"))

			phrase = SoundTest.interpret()
			if phrase != None:
				self.input = phrase

				return self.translate()
				

	def translate(self):
		#Split the input into its pieces
		lis = self.input.split()

		#Check the input to make sure that it's vaid
		success = self.checkInput(lis)

		#Translate & return the move if it's valid, else return False
		if success:																#If the input is valid:
			if len(lis) == 3:
				kind = lis[0].lower()												#Get the kind
				ID = int(lis[1])													#Get the ID
				destination = [self.cols[lis[2][0].lower()],self.rows[lis[2][1]]]	#Get the destination, looking up the row letter in the dict
				self.translated = [kind,ID,destination]								#Add these to translated
			elif len(lis) == 2:
				direction = lis[0].lower()
				com = lis[1].lower()
				self.translated = [direction,com]
		else:																	#If input is not valid:
			self.translated = success											#translated = False
		return self.translated


	def checkInput(self,lis):
		#Check that there's enough information and that it's formatted correctly
		#For a Standard Move:
		if len(lis) == 3:
			#Unpack move
			kind = lis[0]
			ID = lis[1]
			dest = lis[2]
			#Check that the given ID is an integer
			try:
				ID = int(ID)
			except:
				self.sp.engine.say("Piece eye dee must be an integer.")
				self.sp.engine.runAndWait()	
				print "Piece ID must be an integer.\n"
				return False
			#Check that the given destination is a letter in the dict and an integer
			try:
				x = self.cols[dest[0].lower()]
				y = self.rows[dest[1]]
			except:
				self.sp.engine.say("Destination must be a valid letter and number.")
				self.sp.engine.runAndWait()	
				print "Destination must be a letter (A-H) and an integer (1-8).\n"
				return False
			#Check that the given destination is on the board
			if x < 2 or x > 9 or y < 1 or y > 8:
				self.sp.engine.say("Destination must be on the board.")
				self.sp.engine.runAndWait()	
				print "Destination must be on the board.\n"
				return False
			#Return True if everything looks okay
			return True

		#For a Castle Move:
		elif len(lis) == 2:
			#Unpack move
			direction = lis[0]
			com = lis[1]
			#Check that the direction is valid
			if (direction.lower() != "queenside" and direction.lower() != "kingside") or (com.lower() != "castle"):
				self.sp.engine.say("Move not formatted correctly. For example, queen side castle.")
				self.sp.engine.runAndWait()	
				print "Move not formatted correctly. Format: 'Queenside Castle'\n"
				return False
			return True

		else:
			self.sp.engine.say("Move not formatted correctly. For example, Knight 1 H3.")
			self.sp.engine.runAndWait()													
			print "Move not formatted correctly. Format: 'Knight 1 H3'\n"
			return False