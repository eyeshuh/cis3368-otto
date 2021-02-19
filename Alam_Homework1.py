# Aysha Alam
# CIS 3368 - Otto
# Homework 1

import datetime
from datetime import date

import mysql.connector # importing the sql connector to allow python to communicate with it and execute commands

# class Contacts:
# def __init__(self, contact_id, contactDetails, creationDate):
#self.id = contact_id
#self.contactDetails = contactDetails
#self.creationDate = creationDate


my_db = mysql.connector.connect( # setting variable to establish connection to db
    host="cis3368-otto.cey6ttufijmi.us-east-2.rds.amazonaws.com",
    user="eyeshuh",
    password="admin3368",
    database="CIS3368db"
)

# setting variable for mysql cursor to execute commands within the established connection 
db_cursor = my_db.cursor()


# creating a menu function to output menu options for users to choose from 

def menu_output():
    print("MENU")
    print("a - Add contact") 
    print("d - Delete contact")  
    print("u - Update contact details")  # DONE BUT TRY A DIFFERENT APPROACH FOR THE DATE 
    print("b - Output all contacts in alphabetical order")  
    print("c - Output all contacts by creatation date")  
    print("o - Output all contacts") 
    print("q - Quit\n")

    print("Choose an option: ")

# Main function - Speaking to DB and executing what the user chooses from the menu. 

def main():
    menu_output()
    user_input = str(input())

    # A - ADD CONTACTS
    # If the user chooses 'a', prompt them to enter the contactDetail NAME
    # Then prompt them to enter the date in a string format of yyyy-mm-dd

    if user_input == 'a':
        add_contact = str(input("Please enter full name: "))
        add_date = str(input("Please enter date as yyyy-mm-dd: "))

        # Put user inputs into a mysql statement that will insert it into the DB

        sql_query_add_contact = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('%s', '%s')" % (
            add_contact, add_date)

        # Execute the sql command and commit it to the DB to view the new changes 

        db_cursor.execute(sql_query_add_contact)
        my_db.commit()

        # Tell the user the contact has been successfully inserted by counting the # of contacts added 

        print(db_cursor.rowcount, "contact inserted")

    # D - DELETE CONTACT

    elif user_input == 'd':
        sql_delete = str(input("Please enter the full name of the contact you wish to delete: \n"))

        remove_contact = """
        DELETE FROM contacts 
        WHERE contactDetails = '%s'""" % (sql_delete)

        db_cursor.execute(remove_contact)
        my_db.commit()

        print(db_cursor.rowcount, "contact deleted")

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



main()


#######################################################################################
# # # # # # # # # # # # # # # # # # #  references # # # # # # # # # # # # # # # # # # # 
#######################################################################################

# https://www.w3schools.com/python/python_mysql_insert.asp (Inserting a row into MySQL)
# https://www.w3schools.com/python/python_mysql_orderby.asp (Sorting outputs)
# https://www.w3resource.com/python-exercises/python-basic-exercise-3.php 
