# Reference https://www.modmypi.com/blog/raspberry-pi-gpio-sensing-motion-detection
 
# coding: utf-8 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 26
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
               print "Motion Detected! - To Allow access enter CTRL - C"
               time.sleep(2)

print "Ready"

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              time.sleep(100)
except KeyboardInterrupt:
               execfile('doorMotion.py'); 
               GPIO.cleanup()
               

