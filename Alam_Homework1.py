# Aysha Alam
# CIS 3368 - Otto
# Homework 1

import datetime
from datetime import date

import mysql.connector

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
    print("a - Add contact")  # Done
    print("d - Delete contact")  # IP
    print("u - Update contact details")  # DONE BUT TRY A DIFFERENT APPROACH FOR THE DATE 
    print("b - Output all contacts in alphabetical order")  # Done
    print("c - Output all contacts by creatation date")  # Done
    print("o - Output all contacts")  # Done
    print("q - Quit\n")  # Done

    print("Choose an option: ")


def main():
    menu_output()

    while True:
        user_input = str(input())

        if user_input != 'a' or if user_input != 'd' or if user_input != 'u' or if user_input != 'b' or if user_input != 'c' or if user_input != 'o' or if user_input != 'q':
            print("Invalid. Please choose one of the following menu options: \n")


        # A - ADD CONTACTS

        elif user_input == 'a':
            add_contact = str(input("Please enter full name: "))
            add_date = str(input("Please enter date as yyyy-mm-dd: "))

            sql_query_add_contact = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('%s', '%s')" % (
                add_contact, add_date)

            db_cursor.execute(sql_query_add_contact)
            my_db.commit()
            print(db_cursor.rowcount, "contact inserted")

        # D - DELETE CONTACT

        elif user_input == 'd':
            pass
            # sql_delete = int(input("Please enter the ID of the contact you wish to delete: \n")
            #delete_contact = """DELETE FROM contacts WHERE id = %s"""

            #db_cursor.execute(delete_contact, sql_delete)
            # my_db.commit()

            #print(db_cursor.rowcount, "contact deleted")

        # U - UPDATE CONTACT DETAILS

        elif user_input == 'u':
            update_input_1 = str(input("Please enter the full name of the contact you wish to update: "))
            update_input_2 = str(input("Please enter the new name: "))
            update_input_3 = str(input("Please enter the new date in yyyy-mm-dd: "))

            update_query_1 = """ 
            UPDATE contacts 
            SET contactDetails = '%s' 
            WHERE contactDetails = '%s'""" % (update_input_2, update_input_1)

            db_cursor.execute(update_query_1)

            update_query_2 = """ 
            UPDATE contacts 
            SET creationDate = '%s' 
            WHERE contactDetails = '%s' """ % (update_input_3, update_input_2)

            db_cursor.execute(update_query_2)
            my_db.commit()

            print(db_cursor.rowcount, "contact updated")

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

        menu_output()


main()


# references
# https://www.w3schools.com/python/python_mysql_insert.asp
# https://www.w3schools.com/python/python_mysql_orderby.asp
# https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
