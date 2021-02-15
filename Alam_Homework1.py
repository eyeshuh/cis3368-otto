# Aysha Alam
# CIS 3368 - Otto
# Homework 1

# Implement a menu of options for a user to modify the contact details
# Each option is represented by a single character
# The program initially outputs the menu, and outputs the menu after a user chooses an option

#import datetime
#from datetime import date

import mysql.connector

import datetime
from datetime import date


class Contacts:
    def __init__(self, contact_id, contactDetails, creationDate):
        self.id = contact_id
        self.contactDetails = contactDetails
        self.creationDate = creationDate


my_db = mysql.connector.connect(
    host="db connection address",
    user="username",
    password="password",
    database="dbname"
)

db_cursor = my_db.cursor()


def menu_output():
    print("MENU")
    print("a - Add contact")  # Done
    print("d - Delete contact")
    print("u - Update contact details")
    print("b - Output all contacts in alphabetical order")
    print("c - Output all contacts by creatation date")
    print("o - Output all contacts")  # Done
    print("q - Quit\n")  # Done

    print("Choose an option: ")


def main():
    menu_output()
    user_input = str(input())

    # A - ADD CONTACTS

    if user_input == 'a':
        add_contact = str(input("Please enter full name: "))
        add_date = str(input("Please enter date as yyyy/mm/dd"))

        sql_query_add_contact = "INSERT INTO contacts (contactDetails, creationDate) VALUES (%s, %s)"
        sql_query_add_contact_value = (add_contact, add_contact)

        db_cursor.execute(sql_query_add_contact, sql_query_add_contact_value)
        my_db.commit()
        print(db_cursor.rowcount, "contact inesrted")

    # C - OUTPUT BY CREATION DATE

    # O - OUTPUT ALL CONTACTS

    elif user_input == 'o':
        output_all_sql = "SELECT * FROM contacts"
        db_cursor.execute(output_all_sql)
        #my_db.commit()
        print("All contacts:\n")

        db_cursor.fetchall()
        print("Total number of contacts is: ", db_cursor.rowcount)

        for row in records:
            print("ID: ", row[0])
            print("contactDetails: ", row[1])
            print("creationDate: ", row[2], "\n")

    # Q - QUIT PROGRAM

    elif user_input == 'q':
        quit


main()


# references
# https://www.w3schools.com/python/python_mysql_insert.asp
