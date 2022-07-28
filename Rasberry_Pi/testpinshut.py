#shutdown script for Pi
#watch Low Level on Pin5 to enter sleep mode
#status led on pin 7: ON = ready, Blink = confirm button

import RPi.GPIO as GPIO
import time
import os

# use the pin number as on the raspi board

GPIO.setmode(GPIO.BOARD)


#set pin 7 as output and High, pin 5 is input


GPIO.setup(38,GPIO.OUT)
GPIO.output(38, True)
GPIO.setup(40,GPIO.IN)

#start the loop every .5 seconds, waiting for LOW on pin 5
# then 2 short flashes with LED to confirm and shutdown to sleep mode

while True:
        if not(GPIO.input(40)):
                GPIO.output(38, False)
                time.sleep(.1)
                GPIO.output(38, True)
                time.sleep(.1)
                GPIO.output(38, False)
                time.sleep(.1)
                GPIO.output(38, True)
                os.system("sudo shutdown -h now")
        time.sleep(.5)
