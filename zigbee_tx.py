import serial
from sys import argv

script, DHT1, DHT2, BMP1, BMP2 = argv
# Enable USB Communication
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
#data = raw_input('>')

ser.write(data+'\n')
ser.write(DHT1+'\n')
ser.write(DHT2+'\n')
ser.write(BMP1+'\n')
ser.write(BMP2+'\n')
