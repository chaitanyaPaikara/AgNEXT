#! /usr/bin/env python
# Author:	Gopal Krishan Aggarwal and Piyush Mangtani
# Contact: 	gopalkriagg@gmail.com
# Desc: 	This script must run at boot time. It continously coutns number of bucket tips inside rain gauge and after every 3 mins stores the amountof rainfall in rainReading.txt file and resets the rainfall counter. i.e. it stores the amount of rainfall in last 3 mins in rainRading.txt file.
from time import sleep
import RPi.GPIO as GPIO

rainGaugePin = 16
bucketTips = 0               #Maintains the count of how many times bucket inside rain gauge tipped


GPIO.setmode(GPIO.BOARD)
GPIO.setup(rainGaugePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#IncBucketTipsCount() increments the count of bucketTips
def IncBucketTipsCount(y):
        global bucketTips
        bucketTips += 1
	print "Bucket tipped"

try:
	GPIO.add_event_detect(rainGaugePin, GPIO.FALLING, callback = IncBucketTipsCount, bouncetime = 100)
except:
        GPIO.add_event_detect(rainGaugePin, GPIO.FALLING, callback = IncBucketTipsCount, bouncetime = 100)

def resetRainfallReading():
	global bucketTips
	bucketTips = 0

def getRainfallReading():
	rainfall =  bucketTips * 0.2794 
	return rainfall	#Rainfall in millimeters in last 3 minutes

def chorus():
	f = open('/home/pi/weatherStation/rainReading.txt', 'w', 0)
	f.write(str(getRainfallReading()))
	resetRainfallReading()
	f.close()

while True:
	sleep(30)		#After every 3 minutes 
	chorus()		#perform this chorus
