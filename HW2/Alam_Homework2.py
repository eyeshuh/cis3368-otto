# Aysha Alam
# 1822564
# Homework 2 - CIS 3368

import requests
import json
import mysql.connector
import math

# 5fb8dd6b3ff2fb635e104eb9e0d4ac2f

data_request = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?q=Houston,Texas&units=imperial&appid=5fb8dd6b3ff2fb635e104eb9e0d4ac2f").json()


def menu():
    print("c - Display current weather conditions")
    print("f - Display the feel's like temperature")
    print("h - Display current humidity")
    print("m - View today's low and high temperatures")
    print("s - View today's sunrise and sunset times")
    print("t - Display current temperature")
    print("a - Add record to Database")
    print("v - View database")
    print("q - Quit\n")

    print("Choose an option: ")


menu()
user_input = str(input())

if user_input == 'f':
    feels_like = data_request['main']['feels_like']
    feels_like = math.floor(feels_like)
    print(feels_like, "degrees")

elif user_input == 'h':
    print("The current humidity outside is: ",
          data_request['main']['humidity'], "%")

elif user_input == 'm':
    min_temp = data_request['main']['temp_min']
    min_temp = math.floor(min_temp)

    max_temp = data_request['main']['temp_max']
    max_temp = math.floor(max_temp)

    print("Today's low is: ", min_temp, "degrees")
    print("Today's high is: ", max_temp, "degrees")


# relevant parts of API #


# print(data_request['weather'][0]['main'])
# weather main, temp (t- main temp), description (weather.desc), feels like (main), min and max for day (main min and max)
# humidity (main), sunrise and sunset (sys)
