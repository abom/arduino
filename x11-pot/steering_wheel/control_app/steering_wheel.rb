require 'x11_sendkey'
require 'serialport'

# in /usr/include/X11/keysymdef.h
Up = 0xff52
Down = 0xff54
Left = 0xff51
Right = 0xff53


begin
  serial = SerialPort.open('/dev/ttyACM0')
  serial.baud = 9600
  #@serial.data_bits = 8
  #@serial.stop_bits = 1
  #@serial.parity = SerialPort::NONE
rescue  => e
	$stderr.puts "connection error\n#{e.message}"
	exit(1)
end


while true
	d = serial.read
	next if d.empty?
	value = d.to_f
	if value < 4
		X11.sendKey(Right)
	elsif value > 5
		X11.sendKey(Left)
	end
end
