import pyttsx

class Speech():
	def __init__(self):
		self.engine = pyttsx.init()

		self.engine.setProperty('voice', 'en-wm')
		#Default english (kind of British?): en
		#American accent: en-us
		#Scottish accent: en-n
		#Fancy British accent: en-rp
		#Not fancy British Accent: en-wm

		self.engine.setProperty('voice','+f2')
		#Females voices: f1 - f5
		#Male voices: m1 - m7

		self.engine.setProperty('rate', 150)
		#Speed: 150 seems to be ideal