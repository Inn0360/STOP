#Button test program

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.IN)
GPIO.setwarnings(False)
number = 0
GPIO.add_event_detect(19, GPIO.RISING)
while True:

    if(GPIO.event_detected(19)):
       print("press")


