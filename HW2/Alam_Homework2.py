# Aysha Alam
# 1822564
# Homework 2 - CIS 3368

import requests
import json
import mysql.connector
import math

# requesting the weather api using requests.get
# previously requested token inputted within the url

# api requesting data to show houston weather conditions in farenheit units

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

# # # # # # # DB SETUP COMPLETED  # # # # # # #

# defining the menu options for user #


def menu():
    print("")
    print("HOUSTON WEATHER INFORMATION\n")

    # user can choose to display current weather conditions i.e. cloudy
    print("c - Display current weather conditions")
    # user can choose to display feels like temp
    print("f - Display the feel's like temperature")
    # user can choose to display humidity
    print("h - Display current humidity")
    # user can choose to display todays high and low temps
    print("m - View today's low and high temperatures")
    # user can choose to display current weather in degrees
    print("t - Display current temperature")
    # user can choose to add record to DB
    print("a - Add record to Database")
    # user can choose to view all data in DB
    print("v - View database")
    # user can choose to quit the program
    print("q - Quit\n")

    print("Choose an option: ")


# MENU OPTION FUNCTION COMPLETED

##########################################################################################

# SETTING VARIABLES OUT OF LOOP #
# setting variables to hold current temp, min and max temp, humidity, and current conditions
# later will use these variables to output it within the while loop

# # # # # # PARSED DATA FROM WEATHER API # # # # # #

# current temp data retrieved from the main field of api
current_temp = data_request['main']['temp']
# avoiding decimal temperatures, round it down once the number is retrieved
current_temp = math.floor(current_temp)

# min and max temp retrieved from the main field of api
min_temp = data_request['main']['temp_min']
# avoid decimal temperatures, round it down once the number is retrieved
min_temp = math.floor(min_temp)

max_temp = data_request['main']['temp_max']
max_temp = math.floor(max_temp)


# display the feels like temp under the main field
feels_like = data_request['main']['feels_like']
# avoid decimal temperatures, round it down once the number is retrieved
feels_like = math.floor(feels_like)

# humidity data under the main field
humidity_outside = data_request['main']['humidity']

# to avoid slice error under the weather field, choose the description object with [0] and retrieve data
current_conditions = data_request['weather'][0]['description']

##########################################################################################

# While loop to keep the menu constantly outputting for user until they quit the program

while True:
    # output the menu first, then prompt user to choose one of the options and store it into a variable as string
    menu()
    user_input = str(input())
    print("")

    # if the user chooses c
    # output the current weather conditions outside with the current conditions variable stored above

    if user_input == 'c':
        print("Today's weather conditions contain: ", current_conditions)
        print("\n")

    # if the user chooses f
    # display the feels like temperature with the feels like variable stored above

    elif user_input == 'f':
        print("The temperature outside feels like: ", feels_like, "degrees")
        print("\n")

    # if the user chooses h
    # display the humidity using the humidity variable set above

    elif user_input == 'h':
        print("The current humidity outside is: ", humidity_outside, "%")
        print("\n")

    # if the user chooses m
    # display the min and max temp with the variables stored above

    elif user_input == 'm':
        print("Today's low is: ", min_temp, "degrees")
        print("Today's high is: ", max_temp, "degrees")
        print("\n")

    # if the user chooses t
    # display the current temperature outside with the current temp variable stored above

    elif user_input == 't':
        print("The current temperature outside is: ", current_temp, "degrees")
        print("\n")

    # if the user chooses a
    # add record to data
    # record will contain id, current temp, max and min temp, humidity, current conditions
    # mysql will automatically add todays date under the date column

    elif user_input == 'a':

        # use the insert into table query to add all values
        # once the query is added into variable, execute that variable and commit to the db to view changes

        sql_query = """
        INSERT INTO results (currenttemp, high, low, humidity, conditions, tempdate)
        VALUES (%s, %s, %s, %s, '%s', curdate())""" % (current_temp, max_temp, min_temp, humidity_outside, current_conditions)

        db_cursor.execute(sql_query)
        my_db.commit()

        # notify user the record has been successfully added to the DB

        print(db_cursor.rowcount, "record added")

    # if the user chooses v
    # display the data from the database

    elif user_input == 'v':

        # use the select all method to show everything in the results table
        # use the fetchall method to retreive all data from table and store it into a varaible

        view = "SELECT * from results"
        db_cursor.execute(view)
        results = db_cursor.fetchall()

        # for loop to loop over every row and output all the data within the row
        # display the id, current temp, high and low temp, humidity, conditions, and DATE

        for row in results:
            print("ID: ", row[0])
            print("Current temp: ", row[1])
            print("High: ", row[2])
            print("Low: ", row[3])
            print("Humidity: ", row[4])
            print("Conditions: ", row[5])
            print("Date: ", row[6])

    # if the user chooses q
    # BREAK THE PROGRAM

    elif user_input == 'q':
        break


# REFERENCES #

# https://openweathermap.org/current#parameter
