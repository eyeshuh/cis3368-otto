from user import User
import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection(
    "cis3368-otto.cey6ttufijmi.us-east-2.rds.amazonaws.com", "eyeshuh", "admin3368", "CIS3368db")

# create a new entry and add it to the table
dob = datetime.datetime(2021, 1, 1)
str_dob = dob.date().isoformat()
query = "INSERT INTO users (firstname, lastname, dateofbirth) VALUES ('Thomas','Edison','" + str_dob + "')"
#### execute_query(connection, query) ###

# select all users and calculate their age in days
select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)

for user in users:
    dob = user[3]
    today = date.today()
    dayinterval = today - dob
    print(user[1] + " is " + str(dayinterval.days) + " days old")

##########################################################################################
# add a table for invoices
create_invoice_table = """

CREATE TABLE IF NOT EXISTS invoices(
id INT AUTO_INCREMENT,
amount INT,
description VARCHAR(255) NOT NULL,
user_id INTEGER UNSIGNED NOT NULL,
FOREIGN KEY fk_user_id(user_id) REFERENCES users(id),
PRIMARY KEY (id)
)"""

#execute_query(connection, create_invoice_table)

# add invoice record to invoice table
invoice_from_user = 1
invoice_amount = 50
invoice_description = "Harry Potter Books"

query = "INSERT INTO invoices (amount, description, user_id) VALUES (%s, '%s', %s)" % (invoice_amount, invoice_description, invoice_from_user)

#execute_query(connection, query)

# updating invoice record
new_amount = 30
update_invoice_query = """
UPDATE invoices
SET amount = %s
WHERE id = 1 """ % (new_amount)

#execute_query(connection, update_invoice_query)

# delete invoice record from invoice table
invoice_id_to_delete = 1
delete_statement = "DELETE FROM invoices WHERE id = %s" % (invoice_id_to_delete)

#execute_query(connection, delete_statement)

# delete invoices table
delete_table_statement = "DROP TABLE invoices"

#execute_query(connection, delete_table_statement)

## CONCLUDES CRUD OPERATIONS ##