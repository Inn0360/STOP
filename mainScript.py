import stepperScript as step
import Sun_Angles as sun
import RPi.GPIO as GPIO
from datetime import datetime

#Global Variables
controlPins2 = [15,13,12,11] # HORIZONTAL (Azimuth)
controlPins1 = [36,35,33,31] # VERTICAL (altitiude)
#Starting sequence
#1. initalise motors to ensure that they are in the right position
#2. connect to the internet/ping the internet to make sure to get address
#else, ask the user for a longitude / latitude

#Calculations
#request ip, location, latitude, longitude
year, month, day, greenwich_mean_time = sun.time()
ip,city,localLatitude,localLongitude = sun.ipLatlong()
if (ip,city, localLatitude,localLongitude == 0):
    check = 0
    while check is not 2:
        localLatitude = input("## No Connection. Please enter local Latitude of Device --> ")
        localLongitude = input("## No Connection. Please enter local Latitude of Device --> ")
        #latitude (-90 to 90)
        if localLatitude > -90 and localLatitude < 90:
            ++check
        else:
            print("Latitude is invalid, please try again")
        if localLongitude > -180 and localLongitude < 180:
            ++check
        else:
            print("Longitude is invalid, please try again")
        #Longitude ( -180 to 180)
# First request for hour angle, and azimuth_angle 
#both vertical only need 90 degrees of movement

hourAngle = sun.function_hour_angle(year, month, day, greenwich_mean_time, localLongitude)
declinationAngle = sun.function_declination_angle(year, month, day)
altitudeAngle = 90 - sun.function_altitude_angle(declinationAngle,localLatitude,hourAngle)
azimuthAngle = sun.function_azimuth_angle(declinationAngle, localLatitude, hourAngle, alititudeAngle)

#intial startup ALTITUDE
def initialise():
    intial = 0
    if initial == 0:
        step.move(altitudeAngle, 0 , controlPins1) 
        if azimuthAngle > 0:
            step.move(azimuthAngle, 1, controlPins2)
        elif azimuthAngle < 0:
            step.move(abs(azimuthAngle), 1, controlPins2)
        else:
            continue
    previousAltAngle = altitudeAngle
    previousAziAngle = azimuthAngle
return previousAltAngle, previousAziAngle


#assume the device is placed North
#altitude
#NightTime/Reset
def angleReset(previousAziAngle, previousAltAngle):
    # if altitudeAngle == 404 and azimuthAngle == 404: (needs to be placed in main loop as a condition)    
    ok = 0
    if (previousAziAngle > 0):
        resetAzi = previousAziAngle
        print("moving, azimuth, clockwise")
        step.move(resetAzi, 1, controlPins1)
        ok++ 
    elif (previousAziAngle < 0):
        resetAzi = abs(previousAziAngle)
        print("moving, azimuth, anticlockwise")
        step.move(resetAzi, 0, controlPins1)
        ok++
    
    if (previousAltAngle > 0):
        resetAlt = previousAltAngle
        print("moving, altitude, clockwise")
        step.move(resetAlt, 1, controlPins2)
        ok++
    elif (previousAltAngle < 0):
        resetAlt = abs(previousAltAngle)
        print("moving, altitude, anticlockwise")
        step.move(resetAlt, 0, controlPins2)
        ok++

    if (ok == 2):
        return 1
    else:
        return 0


#Daytime
def changeAngle(altitudeAngle, previousAltAngle, azimuthAngle, previousAziAngle):
    altitudeDifference =  previousAltAngle - alititudeAngle
    if (altitudeDifference) == 0:
        print("not moving, altitude")
    elif altitudeDifference > 0:
        print("moving, altitude, clockwise")
        step.move(altitudeDifference, 1, controlPins1)
    elif altitudeDifference < 0:
        print("moving, altitude, anticlockwise")
        step.move(abs(altitudeDifference), 0, controlPins1)
    previousAltAngle = altitudeAngle #after changes, then set angle as 'previous angle'.

    #Azimuth
    azimuthDifference = azimuthAngle - previousAziAngle
    if (azimuthDifference) == 0:
        print("not moving, azimuth")
    elif azimuthDifference > 0:
        print("moving, azimuth, clockwise")
        step.move(azimuthDifference, 1, controlPins2)
    elif azimuthDifference < 0:
        print("moving, azimuth, anticlockwise")
        step.move(abs(azimuthDifference), 0, controlPins2)
    previousAziAngle = azimuthAngle

return previousAziAngle, previousAltAngle


# if the difference is negative, move anticlockwise 
# if difference is positive, move clockwise

- move the solar panel to its first angle ( give it the full angle)
- For every check there after, talk the previous angle, minus it by the new angle, and only move it by the difference
angle * 1.38 for movement in degrees

#call the program that yuhui wrote
#sideways = Azimuth
#Vertical = altitude

# controlling of motors
# Initial movement of stepper motors
# assuming clockwise direction is positive, and anti-clockwise direction is negative

#- need to make sure that it doesnt track after 180 degrees ie under the ground
if __name__ == '__main__':

    init = 0 
    while init = 0: 
        if altitudeAngle == 404 and azimuthAngle == 404:
            init = 0
        else: 
            initialise()
            init = 1 

    while init > 0
        changeAngle(altitudeAngle, previousAltAngle, azimuthAngle, previousAziAngle)
        if altitudeAngle == 404 and azimuthAngle == 404:
            angleReset(previousAziAngle, previousAziAngle) 
            init = 0


 


