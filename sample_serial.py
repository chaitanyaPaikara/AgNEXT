import serial
import os
import time

ser = serial.Serial('/dev/ttyAMA0', 115200, timeout = 1)
print(ser.isOpen()) 
ser.flush()
ser.flushInput()
ser.flushInput()
ser.flushInput() #I feel there is need of more flushing as sometimes there is still data in buffer
ser.flushOutput()

print("Stage")

time.sleep(1)
ser.write('AT'+'\r\n')

print(" sleeping")

time.sleep(10)
x = ser.read(50)
print x
