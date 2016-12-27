#!/usr/bin/python
####################################################################
# phant-loggerGSM.py
# Logs data to phant from a file
# Gopal Krishan Aggarwal @ Innovation Agro
# January 15, 2015 
#
# Description: This piece of code reads weather data from a file
# starting from nth line and tries to write this data to cloud through GSM
# module. When succesful in writing this data it increments this number 'n'
# stored in a separate file named 'lineToBeUploadedNext.txt' and tries to
# now upload the n+1th line if it exists and goes so on. 
########################################################################

import os
import urllib
import serial
import time
import re
import datetime
import subprocess

#################
## Phant Stuff ##
#################
server = "54.86.132.254" # This is the IP of data.sparkfun.com. Using IP instead of hostname may cause trouble in future if data.sparkfun.com changes their IP
publicKey = "EJA2onD8LzUrbKJ7wYgl"
privateKey = "dqm7wDkNJ2FNGdMpvVE7" 
params = "temp=11.38"

def gsmupload():
	ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)

	ser.flush()
	ser.flushInput()
	ser.flushInput()
	ser.flushInput() #I feel there is need of more flushing as sometimes there is still data in buffer
	ser.flushOutput()

	time.sleep(1)
	ser.write('AT+CIPSHUT\r\n')
	time.sleep(1)
	x = ser.read(50)
	print x
	time.sleep(0.5)
	ser.flushInput()

	ser.write('AT+CSTT="airtelgprs.com","",""\r\n')
	time.sleep(1)
	x = ser.read(50)
	print x
	ser.flushInput()


	ser.write('AT+CIICR\r\n')
	time.sleep(1)
	x = ser.read(50)
	print x
	ser.flushInput()

	time.sleep(5)

	ser.write('AT+CIFSR\r\n')
	time.sleep(0.1)
	x = ser.read(50)
	print x
	ser.flushInput()

	cipstart = 'AT+CIPSTART="TCP","' + server + '","80"\r\n'
	ser.write(cipstart) #Sparkfun data.sparkfun.com:  54.86.132.254
	time.sleep(1.5)  	#Sometimes it takes more time for connection (i.e. for "CONNECT OK" response)
	x = ser.read(100)
	print x
	ser.flushInput()

	ser.write('AT+CIPSEND\r\n')
	time.sleep(0.1)
	x = ser.read(50)
	print x
	ser.flushInput()
	
	request = 'GET /input/' + publicKey + '?private_key=' + privateKey + '&' + params + ' HTTP/1.1\r\n\r\n'
	print request
	ser.write(request)
	time.sleep(1)
	x = ser.read(50)
	print x
	ser.flushInput()

	ser.write(chr(26))
	time.sleep(1)
	x = ser.read(50)
	print x
	s = x
	
	ser.flushInput()

	time.sleep(1)
	x = ser.read(500)
	print x
	s = s + x
	x = ser.read(500)
	print x
	s = s + x

	y = ser.read(500)
	print y
	z = ser.read(500)
	print z
	s = s +  y + z
	print s
	ser.flushInput()

	ser.write('AT+CIPSHUT\r\n')
	x =  ser.read(50)
	print x
	ser.flushInput()
	time.sleep(20)
	ser.flushInput()
	ser.close()
	return s

# The following function just extracts timestamp string from phant headers.
# It requests for phant headers again and again until it has got a correct date 
def getPhantDate(s):
	print "REing"
	pat1123 = "\w{3}, \d{2} \w{3} \d{4} \d{2}:\d{2}:\d{2} \w{3}"
	pat1036 = "\w+?, \d{2}-\w{3}-\d{2} \d{2}:\d{2}:\d{2} \w{3}"
	patc = "\w{3} \w{3} \d+? \d{2}:\d{2}:\d{2} \d{4}"
	datepattern = re.compile("(?:%s)|(?:%s)|(?:%s)"%(pat1123,pat1036,patc))
	matcher = datepattern.search(s)
	while matcher is None:
		print "Didn't find pattern match of date"
		s = gsmupload()
		matcher = datepattern.search(s)
	phantDate = matcher.group(0)
	return phantDate




s = gsmupload() #Get a string of http headers from gsmupload() which will hopefully also contain a date string
print s
phantDate = getPhantDate(s) #After this line I expect a valid timestamp string extracted from phant headers

print "Fetched date through Phant headers. The string is: ", 
print phantDate

#It's time now to get a datetime object from this string
while True:
	try:
		dt = datetime.datetime.strptime(phantDate, "%a, %d %b %Y %H:%M:%S %Z").timetuple()
		print "I have got a correct (atleast syntactically) date and it is :",
		print type(dt)
		print dt
		break
	except:
		print "Couldn't get a valid datetime object" #Need to try again now
		s = gsmupload
		phantDate = getPhantDate(s)
		print "Fetched date through Phant headers once again and the string is: ",
		print phantDate
		pass
	print "I woulnd't be here if try was succesful"



#I assume that at this point of time I have a valid and correct dateTime. Use this to set system's dateTime
epochTime = time.mktime(dt)
print "Epoch time is: ",
print epochTime
subprocessCall = "sudo date -s @" + str(epochTime)
print "Executing the following command: "
print subprocessCall
subprocess.call(subprocessCall, shell=True) #Sets system time (Requires root, obviously)
