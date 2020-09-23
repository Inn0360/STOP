#Writen by Howin Tam, Spring 2020 Applications Studio A
#Stepper Motor Script controls two motors connected to a custom PCB

import RPi.GPIO as GPIO
import time
from sys import exit


halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

def move(degrees,rotation,device):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False) # remove this later lol
  print("Rotate Direction = {0}".format(rotation))
  amount = round(degrees * 1.38)
  # rotation == 0 means anticlockwise
  # rotation == 1 means clockwise
  for pin in device: # sets up the pins as inputs  
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)
  #Anti Clockwise
  if rotation == 0:
     for i in range(amount):
      for halfstep in range(8):
        for pin in range(4):
            GPIO.output(device[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)

  #Clockwise
  if rotation == 1:
      for i in range(amount):
        for halfstep in range(7, 0, -1):
          for pin in range(4):
            GPIO.output(device[pin], halfstep_seq[halfstep][pin])
          time.sleep(0.001)
  for pin in device:
    GPIO.output(pin,0)
  return

#value of 1.38 for 1 degree movement
# pins 19 21
def initalise(horizontal, vertical): #initialise the stepper motors
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Horizontal
  GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Vertical
  
  for pin in horizontal: # sets up the pins as inputs
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)
  for pin in vertical:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

  hor = 19
  vert = 21
  #horizontal, anticlockwise
  GPIO.add_event_detect(19, GPIO.RISING)
  triggerH = rotateHit(hor,horizontal)
  
  if triggerH == 1:
    print("setting to 90")
    rotateReset(hor,horizontal)
  #vertical
  GPIO.add_event_detect(21, GPIO.RISING)
  triggerV = rotateHit(vert, vertical)
  if triggerV == 1:
    rotateReset(vert,vertical)
  print("done")
  return

def rotateHit(pins,motor):
  
  for i in range(180):
      for halfstep in range(8):
        for pin in range(4):
          GPIO.output(motor[pin], halfstep_seq[halfstep][pin])
          if GPIO.event_detected(pins):
            return(1)
          time.sleep(0.001)

def rotateReset(pins,motor):   #Azimuth
  for i in range(90):
    for halfstep in range(7,0,-1):
      for pin in range(4):
        GPIO.output(motor[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.001)