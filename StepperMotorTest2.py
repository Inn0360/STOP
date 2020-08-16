import RPi.GPIO as GPIO
import time
from sys import exit

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
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


def shellScript():
  print('Motor Test Command Line \n *meow*')
  while 1:
    print('here')
    userInput = input("--> ")
    if userInput is not None:
        if userInput == "1": #ANTI CLOCKWISE (1)
            print('AntiClockFull')
            direction = 1
            Running(direction)
            for pin in control_pins:
                GPIO.output(pin,0)
        elif userInput == '2': # CLOCKWISE (2)
            print('ClockFull')
            direction = 2
            Running(direction)
            for pin in control_pins:
                GPIO.output(pin,0)
        elif userInput == '3': #(3)
            print('AntiClockHalf')
            direction = 3
            Running(direction)
            for pin in control_pins:
                GPIO.output(pin,0)
        elif userInput == '4': # (4)
            print('ClockHalf')
            direction = 4
            Running(direction)
            for pin in control_pins:
                GPIO.output(pin,0)
        elif userInput == '5': 
            GPIO.cleanup()
            exit(0)
        elif userInput == '6': 
            direction = 6
            Running(direction)
            for pin in control_pins:
                GPIO.output(pin,0)
def Running(direction):
  if direction == 1: # anti clockwise
    print(1)
    for i in range(265):
      for halfstep in range(8):
        for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)

  elif direction == 2: #clockwise
    print(1)
    for i in range(265):
      for halfstep in range(7,0,-1):
        for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)

  elif direction == 4: # half clockwise
    print(1)
    for i in range(133):
      for halfstep in range(7,0,-1):
        for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)


  elif direction == 3: #quarter  anti clockwise
    print(1)
    for i in range(133):
      for halfstep in range(8):
        for pin in range(4):
          GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)
  elif direction == 6:
      print(1)
      for i in range(1):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

def main():
    shellScript()
    while 1:
        Running()


if __name__ == "__main__":
    main()
