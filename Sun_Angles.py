# http://www.powerfromthesun.net/Book/chapter03/chapter03.html#3.1.1%20Time

# Hour_Angle = 15*(Solar_Time - 12) (degrees)
# --Solar_Time = Local_Clock_Time + Longitude_Correction/15 + Equation_of_Time/60
# ----Longitude_Correction = (Local_Longitude -  Longitude_of_standard_time_zone_meridian)
# --Solar_Time = Greenwich_Mean_Time + Local_Longitude/15 + Equation_of_Time/60
# ----Equation_of_Time = 60 * sigma(k=0~5, Ak*cos(360*k*n/365.25)+Bk*sin(360*k*n/365.25)) (minutes)
# ------n = the number of days into a leap year cycle with n = 1 being January 1 of each leap year,
#           and n = 1461 corresponding December 31 of 4th tear of the leap year cycle.
# ------A0 = 2.0870E-4, A1 = +9.2869E-3, A2 = -5.2258E-2, A3 = -1.3077E-3, A4 = -2.1867E-3, A5 = -1.5100E-4,
# ------B0 = 0.0000E+0, B1 = -1.2228E-1, B2 = -1.5698E-1, B3 = -5.1602E-3, B4 = -2.9823E-3, B5 = -2.3463E-4.

# Declination_Angle = 0.39795 * cos(0.98563(N - 173))
# --N = The number of days since January 1.

# Latitude_Angle = arcsin(sin(Declination_Angle) * sin(Latitude_Angle)
#                         + cos(Declination_Angle) * sin(Latitude_Angle) * cos(Hour_Angle)

# Azimuth_Angle = 360 - arccos((sin(Declination_Angle) * sin(Latitude_Angle)
#                               - cos(Declination_Angle) * sin(Latitude_Angle) * cos(Hour_Angle))
#                              /cos(Latitude_Angle)  if: sin(Hour_Angle) > 0;
#               =       arccos((sin(Declination_Angle) * sin(Latitude_Angle)
#                                - cos(Declination_Angle) * sin(Latitude_Angle) * cos(Hour_Angle))
#                               /cos(Latitude_Angle)  if: sin(Hour_Angle) <= 0;

from math import asin, sin, pi, cos, acos
from typing import List
from datetime import datetime
import requests


def function_hour_angle(year: int, month: int, day: int, greenwich_mean_time: float, local_longitude: float):
    # The input year, month, day are integer
    # The input greenwich_mean_tie is hours
    # The input local_longitude is degrees.
    # The output is degrees.

    # Calculate the number of days in leap year cycle from date.
    number_of_days_in_leap_year_cycle = 0

    start_year_of_leap_year_cycle = int(year / 4) * 4
    for year_counter in range(start_year_of_leap_year_cycle, year):
        if int(year_counter / 4) * 4 == year_counter:
            number_of_days_in_leap_year_cycle = number_of_days_in_leap_year_cycle + 366
        else:
            number_of_days_in_leap_year_cycle = number_of_days_in_leap_year_cycle + 365

    for month_counter in range(1, month):
        if ((month_counter == 1) or (month_counter == 3) or (month_counter == 5) or (month_counter == 7) or
                (month_counter == 8) or (month_counter == 10) or (month_counter == 12)):
            number_of_days_in_leap_year_cycle = number_of_days_in_leap_year_cycle + 31
        elif (month_counter == 4) or (month_counter == 6) or (month_counter == 9) or (month_counter == 11):
            number_of_days_in_leap_year_cycle = number_of_days_in_leap_year_cycle + 30
        else:
            if int(year / 4) * 4 == year:
                number_of_days_in_leap_year_cycle = number_of_days_in_leap_year_cycle + 29
            else:
                number_of_days_in_leap_year_cycle = number_of_days_in_leap_year_cycle + 28

    number_of_days_in_leap_year_cycle = number_of_days_in_leap_year_cycle + day

    # Calculate Equation of time from number of days in leap year cycle
    a: List[float] = [0.00020870, 0.0092869, -0.052258, -0.0013077, -0.0021867, -0.00015100]
    b: List[float] = [0.00000000, -0.122280, -0.156980, -0.0051602, -0.0029823, -0.00023463]
    n = number_of_days_in_leap_year_cycle

    equation_of_time = 60 * ((a[0] * cos(360 * 0 * n / 365.25) + b[0] * sin(360 * 0 * n / 365.25)) +
                             (a[1] * cos(360 * 1 * n / 365.25) + b[1] * sin(360 * 1 * n / 365.25)) +
                             (a[2] * cos(360 * 2 * n / 365.25) + b[2] * sin(360 * 2 * n / 365.25)) +
                             (a[3] * cos(360 * 3 * n / 365.25) + b[3] * sin(360 * 3 * n / 365.25)) +
                             (a[4] * cos(360 * 4 * n / 365.25) + b[4] * sin(360 * 4 * n / 365.25)) +
                             (a[5] * cos(360 * 5 * n / 365.25) + b[5] * sin(360 * 5 * n / 365.25)))

    # Calculate Solar Time from greenwich_mean_time, Equation of Time, local_longitude.
    # solar_time = local_clock_time + equation_of_time / 60 + (local_longitude - longitude_of_time_zone_meridian) / 15
    solar_time = greenwich_mean_time + local_longitude / 15 + equation_of_time / 60

    # Calculate Hour Angle from Solar Time. The output is degrees.
    hour_angle = 15 * (solar_time - 12)

    return hour_angle


def function_declination_angle(year: int, month: int, day: int):
    # This function will calculate Declination Angle of SUN. The input is date, and output is degrees.
    # Declination_Angle = arcsin(0.39795 * cos(0.98563(N - 173)))
    # --N = The number of days since January 1.

    n = 0
    for month_counter in range(1, month):
        if ((month_counter == 1) or (month_counter == 3) or (month_counter == 5) or (month_counter == 7) or
                (month_counter == 8) or (month_counter == 10) or (month_counter == 12)):
            n = n + 31
        elif (month_counter == 4) or (month_counter == 6) or (month_counter == 9) or (month_counter == 11):
            n = n + 30
        else:
            if int(year / 4) * 4 == year:
                n = n + 29
            else:
                n = n + 28
    n = n + day

    # declination_angle = asin(0.39795 * cos(0.98563*(n - 173)*pi/180)) * 180 / pi
    declination_angle = asin(sin(23.45 * pi / 180) * cos(360 / 365 * (n - 173) * pi / 180)) * 180 / pi

    return declination_angle


def function_altitude_angle(declination_angle: float, latitude_angle: float, hour_angle: float):
    # This function will calculate Altitude Angle of Solar Battery Panel from Declination Angle of SUN,
    # Latitude Angle of Location, and Hour Angle. The input and output are degrees.
    altitude_angle = asin(sin(pi * declination_angle / 180) * sin(pi * latitude_angle / 180) +
                          cos(pi * declination_angle / 180) * cos(pi * latitude_angle / 180) *
                          cos(pi * hour_angle / 180)) / pi * 180
    if altitude_angle < 0:
        altitude_angle = 90  # 太阳到地球背面去了，让太阳能板正对天上。
    return altitude_angle


def function_azimuth_angle(declination_angle: float, latitude_angle: float, hour_angle: float, altitude_angle: float):
    # This function will calculate Azimuth Angle of Solar Battery Panel from Declination Angle of SUN,
    # Latitude Angle of Location, and Hour Angle. The input and output are degrees.
    if altitude_angle == 90:
        azimuth_angle = 0  # 太阳到背面去了，让太阳能版正对着北。
    else:
        azimuth_angle = acos((sin(pi * declination_angle / 180) * cos(pi * latitude_angle / 180) -
                              cos(pi * declination_angle / 180) * sin(pi * latitude_angle / 180) *
                              cos(pi * hour_angle / 180)) / cos(pi * altitude_angle / 180)) / pi * 180
    if sin(pi * hour_angle / 180) > 0:
        # azimuth_angle = 360 - azimuth_angle  # 0~90朝东北，90~180朝东南，180~270朝西南，270~360朝西北
        azimuth_angle = - azimuth_angle  # 0~90朝东北，90~180朝东南，0~-90朝西北，-90~-180朝西南。

    return azimuth_angle

def ipLatlong():
    # obtain IP address, City, local_latitude, local_longitude of your computer
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
        local_latitude = float(respond.content[start:end])                  # 取出lat，转换为float
        start = respond.content.find(b'\"lon\":', 0) + 6                    # 在content中查找lon开始位置
        end = respond.content.find(b',', start)                             # 在content中查找lon结束位置
        local_longitude = float(respond.content[start:end])                 # 取出lon，转换为float
        return(ip,city,local_latitude,local_longitude)  
    except:
        print("Error: No Connection")
        return(0,0,0,0)

def time():
    utc_now = datetime.utcnow()
    year = utc_now.year
    month = utc_now.month
    day = utc_now.day
    greenwich_mean_time = utc_now.hour + utc_now.minute / 60 + utc_now.second / 3600
    return(year, month, day, greenwich_mean_time)

    

"""
    year = 2020
    month = 1
    day = 1
    greenwich_mean_time = 0
    local_longitude = 0
    local_latitude = 0

    while year <= 2023:
        print(f'\nYear = {year}, Month = {month}, Day = {day}, greenwich_mean_time = {greenwich_mean_time}')

        # Calculate Hour Angle
        hour_angle = function_hour_angle(year, month, day, greenwich_mean_time, local_longitude)
        print(f'Hour Angle = {hour_angle}')

        # Calculate Declination Angle of SUN, (3.22, 0; 6.21, 23.45; 9.23, 0; 12.22, -23.45)
        declination_angle = function_declination_angle(year, month, day)
        print(f'Declination Angle of SUN = {declination_angle}')

        # Calculate Altitude Angle of Solar Batty Panel
        altitude_angle = function_altitude_angle(declination_angle, local_latitude, hour_angle)
        print(f'Latitude Angle = {altitude_angle}')

        # Calculate Azimuth Angle of Solar Batty Panel
        azimuth_angle = function_azimuth_angle(declination_angle, local_latitude, hour_angle, altitude_angle)
        print(f'Azimuth Angle = {azimuth_angle}')

        greenwich_mean_time = greenwich_mean_time + 1
        if greenwich_mean_time == 24:
            greenwich_mean_time = 0
            day = day + 1
        if ((month == 1) | (month == 3) | (month == 5) | (month == 7) | (month == 8) | (month == 10) | (month == 12)) \
                & (day == 32):
            month = month + 1
            day = 1
        if ((month == 4) | (month == 6) | (month == 9) | (month == 11)) & (day == 31):
            month = month + 1
            day = 1
        if (month == 2) & (int(year / 4) * 4 == year) & (day == 30):
            month = month + 1
            day = 1
        if (month == 2) & (int(year / 4) * 4 != year) & (day == 29):
            month = month + 1
            day = 1
        if month == 13:
            year = year + 1
            month = 1
"""
