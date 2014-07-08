import serial

class NFCInterface(object):

	def __init__(self, port='', baud=9600):
		self.port = port
		self.baud = baud
		self.serial_conn = None
		
	def connectToArduino(self):
		port = self.port
		baud = self.baud

		try:
			self.serial_conn = serial.Serial()
			self.serial_conn.port = port
			self.serial_conn.baudrate = baud
			self.serial_conn.open()

		except serial.SerialException, e:
			self.serial_conn = None
			#raise e
			print "can not connect to serial port at %s\n%s" % (port, str(e))

	def isConnected(self):
		return self.serial_conn is not None

	def getCurrentID(self):
		if self.isConnected():
			return self.serial_conn.readline().rstrip()



if __name__ == '__main__':
	nfc = NFCInterface('/dev/ttyACM0', 9600)
	nfc.connectToArduino()
	if nfc.isConnected():
		while True:
			user_id =  nfc.getCurrentID()
			if user_id:
				print user_id