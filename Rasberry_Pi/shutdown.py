import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)

GPIO.output(12, GPIO.HIGH)
os.system("sudo shutdown -h now")
