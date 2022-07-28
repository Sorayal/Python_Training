# Importieren der Bibiotheken für GPIO und Zeit
import RPi.GPIO as GPIO

import time

#GPIO Boardnummern sollen über GPIO  Nummern angesprochen werden
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

for i in range(20):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(21, GPIO.LOW)
    time.sleep(0.5)
    print("bla")

