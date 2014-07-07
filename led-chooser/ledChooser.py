import sys
import serial

# connection simple configuration
# replace /dev/ttyACM0 with ardino port on your machine
serial_conn = serial.Serial()
serial_conn.port = "/dev/ttyACM0"
serial_conn.baudrate = 9600

# our leds
leds = 'a', 'b', 'c'

# connect
try:
	serial_conn.open()

except serial.SerialException:
	print "can not connect to serial port"
	sys.exit(1)

while True:
	ch = raw_input("Type A, B, or C to turn on a led. q to exit: ").lower()

	if ch in leds:
		# tell arduino about our choice
		serial_conn.write(ch)
		# read arduino response
		print serial_conn.readline().rstrip()
		continue

	if ch == 'q':
		serial_conn.close()
		sys.exit(0)
	else:
		print "empty or wrong input"