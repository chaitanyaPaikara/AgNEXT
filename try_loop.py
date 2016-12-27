import os
import urllib
import serial
import time
ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
print (ser.isOpen())
while (1):
	ser.flush()
	ser.flushInput()
	ser.flushInput()
	ser.flushInput() 
	ser.flushOutput()
	time.sleep(1)
	print ("1")
	ser.write('AT'+'\r\n')
	time.sleep(1)
	x = ser.read(50)
	print x
	print("2")
	x = ser.read(50)
	time.sleep(1)
	print x
	print ("3")
	#log.write(x)
	time.sleep(0.5)
	ser.flushInput()

ser.close()
