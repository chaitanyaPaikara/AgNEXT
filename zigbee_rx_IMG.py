import serial

# Enable USB Communication
ser = serial.Serial('/dev/ttyUSB1', 38400,timeout=.5)
f = open('Image_recieved_1.png','wb')
flag = True
while flag:
	while ser.inWaiting():
		print 'Receiving...'
		incoming = ser.read(1024).strip()
		ser.flushInput()
		#print incoming
		#ser.write('Recieved')'
		if str(incoming)=='end':
			flag = False
			f.close()
			print "Done Receiving\n"
			break
		else:
			f.write(incoming)
print'Thank you for connecting'
