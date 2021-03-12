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



# # # # # # # Setting up DB # # # # # # #

# Setting variable to establish connection to db
# In the varialbe define the sql connector by adding the host, user, password, and db name the code will be speaking to

my_db = mysql.connector.connect(
    host="cis3368-otto.cey6ttufijmi.us-east-2.rds.amazonaws.com",
    user="eyeshuh",
    password="admin3368",
    database="CIS3368db"
)

# setting variable for mysql cursor to execute commands within the established connection
db_cursor = my_db.cursor()



def menu():
    print("")
    print("HOUSTON WEATHER INFORMATION\n")
    print("c - Display current weather conditions") # completed 
    print("f - Display the feel's like temperature") # completed
    print("h - Display current humidity") # completed 
    print("m - View today's low and high temperatures") # completed 
    print("t - Display current temperature") # completed 
    print("a - Add record to Database")
    print("v - View database")
    print("q - Quit\n") # completed 

    print("Choose an option: ")


##########################################################################################

# SETTING VARIABLES OUT OF LOOP # 

current_temp = data_request['main']['temp']
current_temp = math.floor(current_temp)

min_temp = data_request['main']['temp_min']
min_temp = math.floor(min_temp)

max_temp = data_request['main']['temp_max']
max_temp = math.floor(max_temp)

humidity_outside = data_request['main']['humidity']

current_conditions = data_request['weather'][0]['description']
##########################################################################################

while True:
    menu()
    user_input = str(input())


    if user_input == 'c':
        print("Today's weather conditions contain: ", current_conditions)
        print("\n")


    elif user_input == 'f':
        feels_like = data_request['main']['feels_like']
        feels_like = math.floor(feels_like)
        print("The temperature outside feels like: ", feels_like, "degrees")
        print("\n")


    elif user_input == 'h':
        print("The current humidity outside is: ", humidity_outside, "%")
        print("\n")


    elif user_input == 'm':
        print("Today's low is: ", min_temp, "degrees")
        print("Today's high is: ", max_temp, "degrees")
        print("\n")


    elif user_input == 't':
        print("The current temperature outside is: ", current_temp, "degrees")
        print("\n")


    elif user_input == 'a':
        sql_query = """
        INSERT INTO results (currenttemp, high, low, humidity, conditions, tempdate)
        VALUES (%s, %s, %s, %s, '%s', curdate())""" % (current_temp, max_temp, min_temp, humidity_outside, current_conditions) 

        db_cursor.execute(sql_query)
        my_db.commit()
        print(db_cursor.rowcount, "record added")

    elif user_input == 'v':
        view = "SELECT * from results"
        db_cursor.execute(view)
        results = db_cursor.fetchall()

        for row in results:
            print("ID: ", row[0])
            print("Current temp: ", row[1])
            print("High: ", row[2])
            print("Low: ", row[3])
            print("Humidity: ", row[4])
            print("Conditions: ", row[5])
            print("Date: ", row[6])


    elif user_input == 'q':
        break





