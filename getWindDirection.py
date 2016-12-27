#! /usr/bin/env python
# Author:	Gopal Krishan Aggarwal and Piyush Mangtani
# Contact: 	gopalkriagg@gmail.com
# Desc: 	This assumes arduino is connected as /dev/ttyACM0 device to RasPi. It reads the analog 0 pin of arduino and calculates the wind direction from the analog value as done below. Read sparkfun weather meter's datasheet for more details.

from nanpy import ArduinoApi
from nanpy import SerialManager
c = SerialManager(device='/dev/ttyUSB1')

from time import sleep


a = ArduinoApi(c)


direction = a.analogRead(0)
if direction>= 728 and direction <= 792 :
	d = 0
	#print  "The wind direction is : NORTH " + str(direction)

elif direction >=228  and direction <=257 :
	d = 180
#		print  "The wind direction is : SOUTH " + str(direction)

elif direction >= 0 and direction <= 97 :
	d = 90
#		print "The wind direction is : EAST " + str(direction)

elif direction >=924 and direction <=961 :
	d = 270
#  	      print "The wind direction is : WEST " + str(direction)

elif direction >= 384 and direction<= 442:
	d = 45
#  	      print "The wind direction is : NORTH-EAST " + str(direction)

elif direction >= 837 and direction <= 908 :
	d = 360-45
# 	      print "The wind direction is : NORTH-WEST " + str(direction)

elif direction >= 128 and direction <= 152 :
	d = 135
#	     print "The wind direction is : SOUTH-EAST " + str(direction)

elif direction >= 543 and direction <=587 :
	d = 225
#	     print "The wind direction is : SOUTH-WEST " + str(direction)


else : d = -1
print d,
sleep(0.1)
