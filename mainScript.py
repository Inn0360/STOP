import stepperScript as step
import Sun_Angles as sun
import RPi.GPIO as GPIO
from datetime import datetime
#Starting sequence
#1. initalise motors to ensure that they are in the right position
#2. connect to the internet/ping the internet to make sure to get address
#else, ask the user for a longitude / latitude

#Calculations
#request ip, location, latitude, longitude
ip,city,localLatitude,localLongitude = sun.ipLatlong()
year, month, day, greenwich_mean_time = sun.time()

input("->")

# First request for hour angle, and azimuth_angle 

hourAngle = sun.function_hour_angle(year, month, day, greenwich_mean_time, localLongitude)
declinationAngle = sun.function_declination_angle(year, month, day)
altitudeAngle = sun.function_altitude_angle(declinationAngle,localLatitude,hourAngle)
azimuthAngle = sun.function_azimuth_angle(declinationAngle, localLatitude, hourAngle, alititudeAngle)

#intial startup ALTITUDE
intial = 0
if initial == 0:
    angleSet = 90 - altitudeAngle
    step.move(angleSet, 0 , controlPins1) #control pins here probably wont work
    if azimuthAngle > 0:
        step.move(azimuthAngle, 1, controlPins2)
    else if azimuthAngle < 0:
        step.move(abs(azimuthAngle), 1, controlPins2)
#assume the device is placed North
#altitude
previousAngle
#NightTime
if altitudeAngle == 90 and azimuthAngle == 0:
    reset = 90 - previousAngle
    if reset == 0:
        break
    step.move(reset,0, controlPins1)



#Daytime


newAngle = alititudeAngle - 90
if (newAngle) == 0:
    print("not moving, altitude")
    
else if newAngle > 0:
    print("moving, altitude, clockwise")
    step.move(newAngle, 1, controlPins1)
else if newAngle < 0:
    print("moving, altitude, anticlockwise")
    step.move(newAngle, 0, controlPins1)
#Azimuth
azimuthNew = azimuthAngle - 90
if (azimuthNew) == 0:
    print("not moving, altitude")
    
else if azimuthNew > 0:
    print("moving, azimuth, clockwise")
else if azimuthNew < 0:
    print("moving, azimuth, anticlockwise")
    step.move(azimuthNew,)

- move the solar panel to its first angle ( give it the full angle)
- For every check there after, talk the previous angle, minus it by the new angle, and only move it by the difference
angle * 1.38 for movement in degrees

#call the program that yuhui wrote
#sideways = Azimuth
#Vertical = altitude

# controlling of motors
#Initial movement of stepper motors
#assuming clockwise direction is positive, and anti-clockwise direction is negative

#- need to make sure that it doesnt track after 180 degrees ie under the ground




if __name__ == '__main__':

