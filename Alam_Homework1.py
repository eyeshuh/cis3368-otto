# Aysha Alam
# CIS 3368 - Otto
# Homework 1

# importing the sql connector to allow python to communicate with it and execute commands
import mysql.connector

# establishing class - contacts 

class Contacts:
    def __init__(self, contact_id, contactDetails, creationDate):
        self.id = contact_id
        self.contactDetails = contactDetails
        self.creationDate = creationDate

# Setting up DB
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

# creating a menu function to output menu options for users to choose from


def menu_output():
    print("MENU")
    print("a - Add contact")
    print("d - Delete contact")
    print("u - Update contact details")
    print("b - Output all contacts in alphabetical order")
    print("c - Output all contacts by creatation date")
    print("o - Output all contacts")
    print("q - Quit\n")

    print("Choose an option: ")

# Main Loop - Speaking to DB and executing designated commands until user decides to quit * #

while True:
    menu_output()  # Output the menu the entire time code is running to prompt the user to choose an option
    user_input = str(input())

    # A - ADD CONTACTS

    # If the user chooses 'a', prompt them to enter the contact NAME they wish to add
    # Then prompt them to enter the date in a string format of yyyy-mm-dd
    # Once user has completed both inputs, take those inputs and input them into the placeholders of the sql command
    # Execute the command then commit it to the DB to view the changes

    if user_input == 'a':
        add_contact = str(input("Please enter full name: "))
        add_date = str(input("Please enter date as yyyy-mm-dd: "))

        # Put user inputs into a mysql statement that will insert it into the DB

        sql_query_add_contact = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('%s', '%s')" % (
            add_contact, add_date)

        # Execute the sql command and commit it to the DB to view the new changes

        db_cursor.execute(sql_query_add_contact)
        my_db.commit() # reference 1

        # Tell the user the contact has been successfully inserted by counting the # of contacts added

        print(db_cursor.rowcount, "contact inserted")

    # D - DELETE CONTACT

    # Prompt the user to input the full name of the contact they wish to delete
    # Take the input from user and store it as a variable to use in the sql statement
    # Input the value to the delete sql statement
    # Execute the command then commit to the DB to view the final changes

    elif user_input == 'd':
        sql_delete = str(
            input("Please enter the full name of the contact you wish to delete: "))

        # Remove from table sql command

        remove_contact = """
        DELETE FROM contacts 
        WHERE contactDetails = '%s'""" % (sql_delete)

        db_cursor.execute(remove_contact)
        my_db.commit()

        # Tell the user the contact has been successfully deleted

        print(db_cursor.rowcount, "contact deleted")

    # U - UPDATE CONTACT DETAILS

    # User will provide 3 inputs - Name of contact they want to update
    # Followed by the new name to change it to (could be same or new)
    # Finally, entering a new date in yyyy-mm-dd (if they want to, could be the same as in record)
    # Note: I could have used datetime to automatically input the time BUT decided not to in order to provide
    # more flexibility for the user incase they wanted to add a SPECIFIC date

    # Once user has provided the inputs, store those values into variables
    # Use variables as "placeholders" to input into sql command

    # Use the update command to update the contact
    # First sql command - change the name to a new one (could be new or same)
    # Second sql command - change the date where the new contact name is (could be new or same)
    # Execute one at a time to avoid errors

    elif user_input == 'u':
        update_input_1 = str(
            input("Please enter the full name of the contact you wish to update: "))
        update_input_2 = str(input("Please enter the new name: "))
        update_input_3 = str(
            input("Please enter the new date in yyyy-mm-dd: "))

        # Command 1 - Changing the name based on a name already in the record

        update_query_1 = """ 
        UPDATE contacts 
        SET contactDetails = '%s' 
        WHERE contactDetails = '%s'""" % (update_input_2, update_input_1)

        db_cursor.execute(update_query_1)

        # Command 2 - Changing the date based on the new/altered contact

        update_query_2 = """ 
        UPDATE contacts 
        SET creationDate = '%s' 
        WHERE contactDetails = '%s' """ % (update_input_3, update_input_2)

        db_cursor.execute(update_query_2)
        my_db.commit() # reference 1

        # Tell the user the contact has been successfully updated by row count

        print(db_cursor.rowcount, "contact updated")

    # B - OUTPUT IN ALPHA ORDER

    # Create a variable that holds the sql command to output records sorted alphabetically
    # Execute the command
    # Use the fetchall class to retreive all the sorted data from the contacts table
    # Once records are retrieved, output them in a presentable format for the user
    # Create a for loop to read every record in the table and output them by their designated columns
    # Ex: ID: ; contactDetails: ; creationDate:

    elif user_input == "b":
        order_by_creation = "SELECT * FROM contacts ORDER BY contactDetails" # reference 2
        db_cursor.execute(order_by_creation)

        # Retrieve all data based on alphabetical order

        output_result = db_cursor.fetchall()
        print("List of contacts Alphabetically: \n")

        # For every row in the table, output them in their designated column + title

        for row in output_result:
            print("ID: ", row[0])
            print("contactDetails: ", row[1])
            print("creationDate: ", row[2], "\n")

    # C - OUTPUT BY CREATION DATE

    # Create a variable that holds the sql command to output the records according to creationDate (Old to new)
    # Execute the command
    # Use fetchall class to retrieve all the sorted records
    # Output the new sorted records by reading every row in the table and outputting them according to designated column

    elif user_input == 'c':
        order_by_creation = "SELECT * FROM contacts ORDER BY creationDate" # reference 2
        db_cursor.execute(order_by_creation)

        # Retrieve all data based on data (oldest to new)

        output_result = db_cursor.fetchall()
        print("List of contacts by creationDate: \n")

        # For every row in the table, output them in their designated column + title

        for row in output_result:
            print("ID: ", row[0])
            print("contactDetails: ", row[1])
            print("creationDate: ", row[2], "\n")

    # O - OUTPUT ALL CONTACTS

    # Variable holding the sql command to retreive ALL records (no specific order)
    # Execute the command
    # Use fetchall class to output all records
    # Read every row in the table and output it in a user friendly presentable format like the previous menu options

    elif user_input == 'o':
        output_all_sql = "SELECT * FROM contacts"
        db_cursor.execute(output_all_sql)

        # Retrieve all data - no specific order

        output_result = db_cursor.fetchall()
        print("Total number of contacts is: ", db_cursor.rowcount)

        # For every row in the table, output them in their designated column + title

        for row in output_result:
            print("ID: ", row[0])
            print("contactDetails: ", row[1])
            print("creationDate: ", row[2], "\n")

    # Q - QUIT PROGRAM

    # If user inputs q, break out of the program

    elif user_input == 'q':
        break


#######################################################################################
# # # # # # # # # # # # # # # # # # #  references # # # # # # # # # # # # # # # # # # #
#######################################################################################

# https://www.w3schools.com/python/python_mysql_insert.asp (Inserting a row into MySQL)
# https://www.w3schools.com/python/python_mysql_orderby.asp (Sorting outputs)
