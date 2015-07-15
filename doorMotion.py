# Reference https://www.modmypi.com/blog/raspberry-pi-gpio-sensing-motion-detection

# coding: utf-8 
import RPi.GPIO as GPIO
import time
import sys


GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
    print "Door Open!"
    execfile('ledtest.py')

    
print "Wait for Door to Open"
time.sleep(2)
print "Ready"

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                   time.sleep(2)
    
except KeyboardInterrupt:
                
               GPIO.cleanup()

