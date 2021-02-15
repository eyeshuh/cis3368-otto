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


# class Contacts:
# def __init__(self, contact_id, contactDetails, creationDate):
#self.id = contact_id
#self.contactDetails = contactDetails
#self.creationDate = creationDate


my_db = mysql.connector.connect(
    host="cis3368-otto.cey6ttufijmi.us-east-2.rds.amazonaws.com",
    user="eyeshuh",
    password="admin3368",
    database="CIS3368db"
)

# setting variable for mysql cursor to execute commands
db_cursor = my_db.cursor()


def menu_output():
    print("MENU")
    print("a - Add contact")  # IP
    print("d - Delete contact")  # IP
    print("u - Update contact details")  # IP
    print("b - Output all contacts in alphabetical order")  # Done
    print("c - Output all contacts by creatation date")  # Done
    print("o - Output all contacts")  # Done
    print("q - Quit\n")  # Done

    print("Choose an option: ")


def main():
    menu_output()
    user_input = str(input())

    # A - ADD CONTACTS

    if user_input == 'a':
        pass
        add_contact = str(input("Please enter full name: "))
        add_date = str(input("Please enter date as yyyy/mm/dd"))

        sql_query_add_contact = "INSERT INTO contacts (contactDetails, creationDate) VALUES (%s, %s)"
        sql_query_add_contact_value = (add_contact, add_date)

        db_cursor.execute(sql_query_add_contact, sql_query_add_contact_value)
        my_db.commit()
        print(db_cursor.rowcount, "contact inesrted")

    # D - DELETE CONTACT

    # elif user_input == 'd':
        # pass
        # delete_query = str(input("Please enter the FULL name of the contact you wish to delete: \n")
        #delete_contact = "DELETE FROM contacts WHERE contactDetails = '%s'" % (delete_query)
        # delete_contact = "DELETE FROM contacts WHERE contactDetails = " + delete_query "
        # db_cursor.execute(delete_contact)

        #print(db_cursor.rowcount, "contact deleted")

    # U - UPDATE CONTACT DETAILS
    # B - OUTPUT IN ALPHA ORDER

    elif user_input == "b":
        order_by_creation = "SELECT * FROM contacts ORDER BY contactDetails"
        db_cursor.execute(order_by_creation)

        output_result = db_cursor.fetchall()
        print("List of contacts Alphabetically: \n")

        for row in output_result:
            print("ID: ", row[0])
            print("contactDetails: ", row[1])
            print("creationDate: ", row[2], "\n")

    # C - OUTPUT BY CREATION DATE

    elif user_input == 'c':
        order_by_creation = "SELECT * FROM contacts ORDER BY creationDate"
        db_cursor.execute(order_by_creation)

        output_result = db_cursor.fetchall()
        print("List of contacts by creationDate: \n")

        for row in output_result:
            print("ID: ", row[0])
            print("contactDetails: ", row[1])
            print("creationDate: ", row[2], "\n")

    # O - OUTPUT ALL CONTACTS

    elif user_input == 'o':
        output_all_sql = "SELECT * FROM contacts"
        db_cursor.execute(output_all_sql)

        output_result = db_cursor.fetchall()
        print("Total number of contacts is: ", db_cursor.rowcount)

        for row in output_result:
            print("ID: ", row[0])
            print("contactDetails: ", row[1])
            print("creationDate: ", row[2], "\n")

    # Q - QUIT PROGRAM

    elif user_input == 'q':
        quit


main()


# references
# https://www.w3schools.com/python/python_mysql_insert.asp
# https://www.w3schools.com/python/python_mysql_orderby.asp
