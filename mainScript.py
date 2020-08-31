import stepperScript
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
stepperScript.initalise()

GPIO.cleanup()