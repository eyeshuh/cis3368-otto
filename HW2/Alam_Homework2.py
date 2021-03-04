# Aysha Alam
# 1822564
# Homework 2 - CIS 3368

import requests
import json
import mysql.connector

# 5fb8dd6b3ff2fb635e104eb9e0d4ac2f

data_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Houston,Texas&appid=5fb8dd6b3ff2fb635e104eb9e0d4ac2f").json()
print(data_request)
print("\n\n")

print(data_request['weather'])
print("\n\n")

print(data_request['weather'][0]['main'])
print("\n\n")

print(data_request['weather'][0]['description'])
print("\n\n")

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

while True:
    menu()
    user_input = str(input())
    
    if user_input == 'q':
        break




# relevant parts of API #


# print(data_request['weather'][0]['main'])
# weather main, temp (t- main temp), description (weather.desc), feels like (main), min and max for day (main min and max)
# humidity (main), sunrise and sunset (sys)



