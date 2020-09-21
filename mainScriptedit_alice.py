import stepperScript as step
import sunanglesedit_alice as sun
import RPi.GPIO as GPIO
from datetime import datetime
import time

#Global Variables
controlPins2 = [15,13,12,11] # HORIZONTAL (Azimuth)
controlPins1 = [36,35,33,31] # VERTICAL (altitiude)
#Starting sequence
#1. initalise motors to ensure that they are in the right position
#2. connect to the internet/ping the internet to make sure to get address
#else, ask the user for a longitude / latitude
    #Calculations
#request ip, location, latitude, longitude

def noInternet(): 
    try:   
        respond = requests.get('http://ip-api.com/json/')                   # 上网获得本机外网IP地址的信息
        start = respond.content.find(b'\"query\":\"', 0) + 9                # 在content中查找IP地址开始位置
        end = respond.content.find(b'\"', start)                            # 在content中查找IP地址结束位置
        ip = respond.content[start:end]                                     # 取出IP地址，ip是bytes-link
        start = respond.content.find(b'\"city\":\"', 0) + 8                 # 在content中查找City开始位置
        end = respond.content.find(b'\"', start)                            # 在content中查找City结束位置
        city = respond.content[start:end]                                   # 取出City，City是bytes-link
        start = respond.content.find(b'\"lat\":', 0) + 6                    # 在content中查找lat开始位置
        end = respond.content.find(b',', start)                             # 在content中查找lat结束位置
        latitude_angle = float(respond.content[start:end])                  # 取出lat，转换为float
        start = respond.content.find(b'\"lon\":', 0) + 6                    # 在content中查找lon开始位置
        end = respond.content.find(b',', start)                             # 在content中查找lon结束位置
        local_longitude = float(respond.content[start:end])                 # 取出lon，转换为float
    except:
        print("Error: No Connection")

    if (ip,city, latitude_angle,local_longitude  == 0):
        check = 0
        while check is not 2:
            latitude_angle = input("## No Connection. Please enter local Latitude of Device --> ")
            local_longitude = input("## No Connection. Please enter local Latitude of Device --> ")
            #latitude (-90 to 90)
            if latitude_angle > -90 and latitude_angle < 90:
                check += 1
            else:
                print("Latitude is invalid, please try again")
            if local_longitude > -180 and local_longitude < 180:
                check += 1
            else:
                print("Longitude is invalid, please try again")
            #Longitude ( -180 to 180)
    # First request for hour angle, and azimuth_angle 
    #both vertical only need 90 degrees of movement


#intial startup ALTITUDE
def initialise(altitudeAngle, azimuthAngle):
    azimuthAngle, altitudeAngle  = sun.sunAngles()
    initial = 0
    if initial == 0:
        step.move(altitudeAngle, 0 , controlPins1) 
        if azimuthAngle > 0:
            step.move(azimuthAngle, 1, controlPins2)
        elif azimuthAngle < 0:
            step.move(abs(azimuthAngle), 1, controlPins2)

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
        ok+= 1
    elif (previousAziAngle < 0):
        resetAzi = abs(previousAziAngle)
        print("moving, azimuth, anticlockwise")
        step.move(resetAzi, 0, controlPins1)
        ok+= 1
    
    if (previousAltAngle > 0):
        resetAlt = previousAltAngle
        print("moving, altitude, clockwise")
        step.move(resetAlt, 1, controlPins2)
        ok+= 1
    elif (previousAltAngle < 0):
        resetAlt = abs(previousAltAngle)
        print("moving, altitude, anticlockwise")
        step.move(resetAlt, 0, controlPins2)
        ok+= 1

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

#- move the solar panel to its first angle ( give it the full angle)
#- For every check there after, talk the previous angle, minus it by the new angle, and only move it by the difference
#angle * 1.38 for movement in degrees

#call the program that yuhui wrote
#sideways = Azimuth
#Vertical = altitude

# controlling of motors
# Initial movement of stepper motors
# assuming clockwise direction is positive, and anti-clockwise direction is negative

#- need to make sure that it doesnt track after 180 degrees ie under the ground
if __name__ == '__main__':
    
    

    init = 0 
    while (init == 0): 
        if altitudeAngle == 404 and azimuthAngle == 404:
            init = 0
        else: 
            initialise(altitudeAngle, azimuthAngle)
            init = 1 
        time.sleep(10) #program sleeps for 10 seconds before executing more 

    while (init > 0):
        changeAngle(altitudeAngle, previousAltAngle, azimuthAngle, previousAziAngle)
        if altitudeAngle == 404 and azimuthAngle == 404:
            angleReset(previousAziAngle, previousAziAngle) 
            init = 0
        time.sleep(10)


 


