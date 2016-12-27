#!/usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO

powerPin = 11

GPIO.setmode(GPIO.BOARD)

print("Turning on/off GSM Module")

GPIO.setup(powerPin, GPIO.OUT, initial=GPIO.LOW)
sleep(5)
GPIO.setup(powerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

