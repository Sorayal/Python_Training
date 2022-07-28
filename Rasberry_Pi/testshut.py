#shutdown script for Pi
#watch Low Level on Pin5 to enter sleep mode
#status led on pin 7: ON = ready, Blink = confirm button

import RPi.GPIO as GPIO
import time
import os

# use the pin number as on the raspi board

GPIO.setmode(GPIO.BOARD)


#set pin 7 as output and High, pin 5 is input


GPIO.setup(7,GPIO.OUT)
GPIO.output(7, True)
GPIO.setup(5,GPIO.IN)

#start the loop every .5 seconds, waiting for LOW on pin 5
# then 2 short flashes with LED to confirm and shutdown to sleep mode

while True:
        if not(GPIO.input(5)):
                GPIO.output(7, False)
                time.sleep(.1)
                GPIO.output(7, True)
                time.sleep(.1)
                GPIO.output(7, False)
                time.sleep(.1)
                GPIO.output(7, True)
                os.system("sudo shutdown -h now")
        time.sleep(.5)
