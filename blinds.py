#!/usr/bin/python
# Use the pin number as argument for the script

import RPi.GPIO as GPIO
import time
import sys  # to be possible to import argument

PIN =  int(sys.argv[1])
print('Eingabe war PIN: ' + str(PIN))

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)
time.sleep(1/5.0)
GPIO.output(PIN, GPIO.LOW)
time.sleep(1)
print('PIN ' + str(PIN) + ' an und ausgeschaltet')
exit()
