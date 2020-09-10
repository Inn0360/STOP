import RPi.GPIO as GPIO
import stepperScript
import Sun_Angles as sun
from datetime import datetime
#Starting sequence
1. initalise motors to ensure that they are in the right position
2. connect to the internet/ping the internet to make sure to get address
else, ask the user for a longitude / latitude

#Calculations
#request ip, location, latitude, longitude
ip,city,localLatitude,localLongitude = sun.ipLatlong()

# First request for hour angle, and azimuth_angle
hourAngle = sun.function_hour_angle(year, month, day, gree  nwich_mean_time, local_longitude)
declinationAngle = sun.function_declination_angle(year, month, day)
AlititudeAngle = sun.function_altitude_angle(declinationAngle,)
AzimuthAngle = sun.function_azimuth_angle


call the program that yuhui wrote
#sideways = Azimuth
#Vertical = altitude

# controlling of motors

- need to make sure that it doesnt track after 180 degrees ie under the ground


GPIO.cleanup()