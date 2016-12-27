#!/usr/bin/env bash

DHTTempHumidity=`sudo python /home/pi/weatherStation/dht11/Adafruit_Python_DHT/examples/AdafruitDHT_copy.py 11 4`; #Runs the script mentioned in backticks and stores the result in the variable. 11 specifies that DHT11 is being used and 4 specifies it is connected to pin 4 of pi. Visit the Adafruit website for more details.

BMPPressureTemp=`sudo python /home/pi/weatherStation/bmp085/Adafruit_Python_BMP/examples/simpletest_copy.py`; #Similar to above for BMP pressure sensor.

RainGaugeReading=`cat /home/pi/weatherStation/rainReading.txt` #The script getRainGaugeReading.py which was run at boot-time stores the result in rainReading.txt every 3 mins. Here we are fetching that reading and storing it in the variable.

WindSpeedReading=`python /home/pi/weatherStation/getWindSpeed.py` #Get the current wind speed. (This needs to be changed and made similar to rainGaugeReading)

WindDirection=`python /home/pi/weatherStation/getWindDirection.py` #Get current wind direction.

echo "Rain Gauge Reading is: $RainGaugeReading"
echo "Wind speed is: $WindSpeedReading"
echo "Wind direction is: $WindDirection"

command="sudo python /home/pi/weatherStation/updateFilesWithWeatherData.py $DHTTempHumidity $BMPPressureTemp $RainGaugeReading $WindSpeedReading $WindDirection" #Construct the command string
echo "The command is $command" #Print the command which is going to be executed.
eval $command #Evaluate that command.

# BETTER OPTION (prevents the conflict of multiple scripts writing on same file):
# At this point of time we have latest weather data appended to weatherLocalCopy.data and
# we also have another identical file weatherPhant.data which we will use to upload data
# to phant. The algo goes as follows:
# 1) Check if script phant-loggerGSM.py is running
#	Case 'no':It is not running. This case should occur only when there is only one
#		row of weather data (i.e. the latest one) is left for uploading which is GOOD! In some
#		rare scenario it might happen that we enter this 'yes' case yet there is no
#		row of data in file to be uploaded -- or can't it?
# 		i) In this case run the script phant-loggerGSM.py
#	Case 'yes' : i.e. script phant-loggerGSM.py is already running! This would be because
# 		the script is trying to upload previous data only.
# 		i)Don't do anything since previously running phant-logger.py will handle the
# 		 latest data too.

process=`ps -aux | grep 'phant-loggerGSM.py' | wc -l`	#Check if phant-loggerGSM.py is already running
echo $process #If result is 2 then phant-loggerGSM.py is running
if [ $process -eq 1 ]; then #If phant-loggerGSM.py is not running then run it to upload the latest reading
	echo "Going to run phant-loggerGSM.py"
	python /home/pi/weatherStation/phant-loggerGSM.py
else
	echo "Seems like phant-loggerGSM.py is already running" #If phant-loggerGSM.py is already running it means it is trying to upload previous readings.
fi
