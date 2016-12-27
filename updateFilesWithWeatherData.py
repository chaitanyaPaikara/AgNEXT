####################################################################
# updateFilesWithWeatherData.py
# Raspberry Pi Phant 
# Gopal Krishan Aggarwal @ Innovation Agro
# January 15, 2016
# Description: This piece of code receives various weather parameters
# from command line and appends them to two files: "weatherPhant.data" 
# and "weatherLocalCopy.data".
########################################################################

import time              # time used for delays
import datetime		 # For timestamp in data to be saved
import socket            # socket used to get host name/IP
import sys		 # For command-line arguments


fields = ["hostname", "tempdht", "humidity", "tempbmp", "pressure", "rainfall", "windspeed", "winddirection", "pitimestamp"] # Your feed's data fields

myHostname = socket.gethostname() # Send local host name as one data field

data = {} # Create empty set, then fill in with our three fields:

data[fields[0]] = myHostname #time.strftime("%A %B %d, %Y %H:%M:%S %Z")
for i in range(1, len(sys.argv)):
	data[fields[i]] = float(sys.argv[i])

data[fields[8]] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

outputFilePhant = open("/home/pi/weatherStation/weatherPhant.data", "a")
outputFileLocalCopy = open("/home/pi/weatherStation/weatherLocalCopy.data", "a")
for i in range(0, len(fields)):
	print "{} = {}".format(fields[i], data[fields[i]])
	outputFilePhant.write(str(data[fields[i]]))
	outputFilePhant.write(", ")
	outputFileLocalCopy.write(str(data[fields[i]]))
	outputFileLocalCopy.write(", ")

outputFilePhant.write("\n")
outputFilePhant.close()
outputFileLocalCopy.write("\n")
outputFileLocalCopy.close()
time.sleep(0.5) # I don't exactly know the reason for this delay. Maybe, some time is needed to empty the buffer
