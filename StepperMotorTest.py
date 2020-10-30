import RPi.GPIO as GPIO
import time
from sys import exit

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
control_pins = [15, 13, 12, 11]
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
        elif userInput 
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

  def angleReset(previousAziAngle, previousAltAngle):
    # if altitudeAngle == 404 and azimuthAngle == 404: (needs to be placed in main loop as a condition)    
    ok = 0
    if (previousAziAngle < 0):
        resetAzi = previousAziAngle
        print("moving, azimuth, clockwise")
        print("resetting clockwise by {0}".format(resetAzi))
        step.move(resetAzi, 1, controlPins1)
        ok+= 1
    elif (previousAziAngle > 0):
        resetAzi = abs(previousAziAngle)
        print("moving, azimuth, anticlockwise")
        print("resetting anticlockwise by {0}".format(resetAzi))
        step.move(resetAzi, 0, controlPins1)
        ok+= 1
    
    if (previousAltAngle > 0):
        resetAlt = previousAltAngle
        print("moving, altitude, clockwise")
        print("resetting clockwise by {0}".format(resetAlt))
        step.move(resetAlt, 0, controlPins2)
        ok+= 1
   # elif (previousAltAngle < 0):
   #     resetAlt = abs(previousAltAngle)
    #    print("moving, altitude, anticlockwise")
    #    print("resetting anticlockwise by {0}".format(resetAlt))
    #    step.move(resetAlt, 0, controlPins2)
     #   ok+= 1

    if (ok == 2):
        return 1
    else:
        return 0

def main():
    shellScript()
    while 1:
        Running()


if __name__ == "__main__":
    main()
