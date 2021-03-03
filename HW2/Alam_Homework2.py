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
    print("a - Display current weather")
    print("l - Display long and lad coordinates")



