#DO NOT RUN THIS SCRIPT IF YOU DON'T KNOW WHAT IS HAPPENING HERE! BASICALLY I HAVE TRIED TO AUTOMATE FEW STEPS MENTIONED IN Documention file
sudo apt-get update #Update repo info

sudo rm log lineToBeUploadedNext.txt weatherLocalCopy.data weatherPhant.data rainReading.txt
#Configuring i2c
printf "\nPlease manually configure i2c if not already configured by following the guide at https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c \n"
printf "Cancel the script if i2c is not configured yet\n"
sleep 5

#Setting up bmp085
printf "\nSetting up pressure sensor bmp085. Make sure it is connected and is being detected by i2cdetect"
sleep 2
sudo apt-get install git build-essential python-dev python-smbus
cd ./bmp085/Adafruit_Python_BMP
sudo python setup.py install

cd examples
sudo python simpletest.py #If everything is working fine then this should print pressure data on screen
cd ../../../
sleep 2

#Setting up DHT11 sensor
#Steps taken from https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/using-the-adafruit-bmp-python-library
printf "\nSetting up DHT11 temp-humidity sensor\n"
sleep 1
cd dht11/Adafruit_Python_DHT

sudo apt-get install build-essential python-dev python-openssl
sudo python setup.py install

cd examples

sudo ./AdafruitDHT.py 11 4 #This should print temp humidity data
cd ../../../
sleep 2

