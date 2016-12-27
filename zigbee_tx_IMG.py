import serial
from sys import argv
import time

#script, DHT1, DHT2, BMP1, BMP2 = argv
# Enable USB Communication
ser = serial.Serial('/dev/ttyUSB0', 38400,timeout=.5)
#data = raw_input('>')
#ser.write(data+'\n')
flag = True
f = open('image.jpg','rb')
l = f.read(1024)
while (l):
    print 'Sending...'
    ser.write(l)
    l = f.read(1024)
    time.sleep(2)
ser.write('end')
f.close()
print "Done Sending"

'''
while ser.readline().strip() is not 'Recieved':
    	ser.write(l)
''' 

'''
    while flag:
    	incoming = ser.readline().strip()
    	print incoming
    	if incoming is 'Recieved':
    		flag = False
    	incoming = None
    flag = True
    '''
