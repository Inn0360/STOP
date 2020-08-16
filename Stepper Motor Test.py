import RPi.GPIO as GPIO
import time
from sys import exit

GPIO.setmode(GPIO.BOARD)

control_pins = [7,11,13,15]
direction = 0
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

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

GPIO.cleanup()

while 1:
  Running()
  time.sleep(1)

def shellScript():
  print('Motor Test Command Line \n *meow*')
    while 1:
      userInput = input("-->")
      if userInput is not None:
        if userInput = 'Back': #ANTI CLOCKWISE (1)
          direction = 1

        if userInput = 'Forward': # CLOCKWISE (2)
          direction = 2

        if userInput = 'halfFor': #(3)
          direction = 3

        if userInput = 'halfBac': # (4)
          direction = 4

        if userInput = 'Exit': 
          GPIO.cleanup()
          exit(0)
def Running:
  elif direction == 1: # anti clockwise
    for i in range(265):
      for halfstep in range(8):
        for pin in range(4):
          GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.001)

  elif direction == 2: #clockwise
    for i in range(265):
      for halfstep in range(7,0):
        for pin in range(3,0):
          GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.001)

  elif direction == 3: # half clockwise
    for i in range(132,0):
      for halfstep in range(7,0):
        for pin in range(4):
         GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.001)


  elif direction == 4: #half anti clockwise
    for i in range(133):
      for halfstep in range(8):
        for pin in range(4):
          GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.001)

    