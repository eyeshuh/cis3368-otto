# Aysha Alam
# 1822564
# CIS 3368 - EXAM 1

import requests
import json
import mysql.connector

# ask user to input the state and date in which they want to locate data
# state input must be in abbreviation format
# date input must be in yyyymmdd format
# both inputs stored as a string

state_input = str(input(
    "Enter the state for which the COVID data should be retrieved (e.g. NY): "))
date_input = str(input(
    "Enter the date for which the COVID data should be retrieved (e.g. 20210306): "))

print("\n")

# once inputs stored and retrieved, take those inputs and put them into the placeholders for API requests
# place holders will make it easy to input the state AND date all in one request and retrieve info
# once data is requested, store and output it into JSON format and begin parsing it

covid_data = requests.get(
    "https://api.covidtracking.com/v1/states/%s/%s.json" % (state_input, date_input)).json()
print("\n")

# creating variables to hold information related to necessary fields for output
# for each output, refer to the json formatted data
# retrieve specific fields similar to accessing a dictionary using []

# retrieving state information from API using the state field
covid_data_state = covid_data['state']
# retrieving date information from API using the date field
covid_data_date = covid_data['date']
# retrieving positive cases information from API using the positive field
covid_data_positive = covid_data['positive']
# retrieving death information from API using the death field
covid_data_death = covid_data['death']

# output the data in order of state, date, positive cases, and deaths with retrieved data stored into variables
# function created to hold all output information


def data_ouput():
    print("State: %s" % covid_data_state)
    print("Date: %s" % covid_data_date)
    print("Positive Cases: %s" % covid_data_positive)
    print("Deaths: %s" % covid_data_death)
    print("\n")


# call the function to output the data
data_ouput()

# # # # # ADDING INFORMATION TO THE DATABASE # # # # #

# establish a connection to remote DB
# once connection is established, input covid query
# query will consist of id, date, state, positiveIncrease, and deathIncrease


# setting up host, user, password, and db using mysql connector
my_db = mysql.connector.connect(
    host="cis3368-otto.cey6ttufijmi.us-east-2.rds.amazonaws.com",
    user="eyeshuh",
    password="admin3368",
    database="CIS3368db"
)

# DB cursor created to communicate with DB connection and perform CRUD; in this case = ADD

db_cursor = my_db.cursor()

# query to insert data and values into the DB
# placeholders used to input user inputs as values
covid_query = "INSERT INTO exam1 (date, state, positiveIncrease, deathIncrease) VALUES ('%s', '%s', '%s', '%s')" % (
    covid_data_date, covid_data_state, covid_data_positive, covid_data_death)

# execute the covid query
db_cursor.execute(covid_query)

# commit it into the DB to apply and view the changes
my_db.commit()

# let user know the information has been added into the DB
print(db_cursor.rowcount, "row of covid statistics added")
