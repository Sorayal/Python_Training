#Importieren der Bibiotheken für GPIO und Zeit
import RPi.GPIO as GPIO

import time

#GPIO Boardnummern sollen über GPIO  Nummern angesprochen werden
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

i=1
while i>=1:
#for i in range(20):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(21, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(19, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(19, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(16, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(16, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(19, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(19, GPIO.LOW)
    time.sleep(0.1)


