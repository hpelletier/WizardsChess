import time
import serial

def sendCommand():

	#Connect to the correct Serial Port
	serialPorts = ["/dev/ttyACM0","/dev/ttyACM1","/dev/ttyACM2","/dev/ttyACM3","/dev/ttyACM4","/dev/ttyACM5"]
	for port in serialPorts:
		try:
			ser = serial.Serial(port, 9600)
			print "Connected to port " + port
			time.sleep(1)
			break
		except:
			pass
	else:
		print "Could not connect to serial port. Please check Arduino connection and try again."
		
	while True:
		#Get user input
		command = raw_input("Mag.XDir.XDist.YDir.YDist: ")

		#Sanity check
		print "Mag:" + str(int(command)/100000000);
		print "xDir:" + str((int(command)/10000000)%10);
		print "xDist:" + str((int(command)/10000)%1000);
		print "yDir:" + str((int(command)/1000)%10);
		print "yDist:" + str(int(command)%1000);

		#Write to serial
		ser.write(command)
		
		#Wait for Arduino
		not_read = True
		while not_read:
			if ser.readline() == "Done\n":
				print "Done!"
				not_read = False

sendCommand()
