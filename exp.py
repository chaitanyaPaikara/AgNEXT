from bash import bash
from time import sleep
import serial

print "(Presumably) Shutting off GSM Module"
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout = 1)
ser.flush()
ser.flushInput()
ser.flushInput()
ser.flushInput() #I feel there is need of more flushing as sometimes th$
ser.flushOutput()

sleep(1)
bash("/home/pi/weatherStation/startGSMModule.py")
sleep(0.1)
resp = ser.read(200)
print resp
if "DOWN" in resp:
	sleep(5)
        bash("/home/pi/weatherStation/startGSMModule.py")
        sleep(30)
else:
       print "Looks like GSM Module was already turned off and now is turned on"
       sleep(30)
ser.close()
