import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.HIGH)
time.sleep(1/5.0)
GPIO.output(13, GPIO.LOW)
time.sleep(1)
print('PIN13 an und ausgeschaltet')
exit()
