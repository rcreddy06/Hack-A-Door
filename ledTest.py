import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 6
GPIO.setup(led,GPIO.OUT)

GPIO.output(led, 1)
time.sleep(3)
GPIO.output(led,0)
