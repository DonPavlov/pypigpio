import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)
time.sleep(1/5.0)
GPIO.output(5, GPIO.LOW)
time.sleep(1)
print('PIN13 an und ausgeschaltet')
exit()
