import os
import urllib
import serial
import time
ser = serial.Serial('/dev/ttyS0', 115200, timeout = 1)
print (ser.isOpen())
ser.flush()
ser.flushInput()
ser.flushInput()
ser.flushInput() 
ser.flushOutput()
time.sleep(1)
print ("1")
ser.write('AT/r/n')
time.sleep(5)
x = ser.read(50)
print x
print("2")
x = ser.read(50)
time.sleep(1)
print x
print ("3")
print ("1")
ser.write('AT+CSQ/r/n')
time.sleep(5)
x = ser.read(50)
print x

#log.write(x)
time.sleep(0.5)
ser.flushInput()
