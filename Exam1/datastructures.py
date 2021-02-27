import hello
import mysql.connector
from mysql.connector import Error


# read from console
#value = input("Please enter a string: \n")

# output directly as part of string
#print(f"You entered {value}")

# output a string message
#message = "You entered %s" % (value)
# print(message)

# dictionaies
mydict = {
    "firstname": "Jane",
    "lastname": "Doe",
    "birthyear": 2001,
}

fname = mydict["firstname"]
# print(fname)

mydict = {
    "firstname": "Jane",
    "lastname": "Doe",
    "birthyear": 2001,
    "children": ["Jack", "John", "James"]
}
# print(mydict)

mydict["birthyear"] = 2000
# print(mydict)

mydict.update({"birthyear": 1995})
# print(mydict)

# if "children" in mydict:
#print("We have children")

mydict["father"] = "Jeff"
# print(mydict)

mydict.pop("father")
# print(mydict)

mydict["father"] = "Jeff"
del mydict["father"]
# print(mydict)

mydict.clear()
# print(mydict)

# lists
# ordered, changable, duplicates, multiple data types

mylist = ["apple", "kiwi", "pear"]
print(mylist)
mylist = ["apple", "kiwi", "pear", "apple", "apple"]
print(mylist)
list_len = len(mylist)
print(list_len)

mylist = [100, 150, 900, 1200]
print(mylist)

mylist = [False, True, False]
mylist = ["apple", 300, "True", "alex", [1, 2, 3, 4, 5]]
print(mylist)

print(mylist[1])
print(mylist[-1])

print(mylist[1:4])  # not including 4
print(mylist[:4])
print(mylist[-3:-1])

if "alex" in mylist:
    print(mylist[3])

else:
    print(mylist)

mylist[1] = 500
print(mylist)

mylist.insert(2, "Totally unrelated string")
print(mylist)

mylist.append("yellow")
print(mylist)

more_colors = ["red", "blue", "green"]
mylist.extend(more_colors)
print(mylist)

mylist.pop(0)
print(mylist)

del mylist[-1]
print(mylist)

for x in mylist:
    print(x)

# mylist.sort() will cause errors cause different data types

mylist = ["red", "blue", "purple", "green", "white"]
print(mylist)
mylist.sort()
print(mylist)

con = hello.create_connection("cis3368-otto.cey6ttufijmi.us-east-2.rds.amazonaws.com", "eyeshuh", "admin3368", "CIS3368db")
select_users = "SELECT * FROM users"
users = hello.execute_read_query(con, select_users)
print(users)

print(users[0])

conn = hello.create_connection("cis3368-otto.cey6ttufijmi.us-east-2.rds.amazonaws.com", "eyeshuh", "admin3368", "CIS3368db")

cursor = conn.cursor(dictionary = True)
sql = "SELECT * FROM users"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row)
    print(row["firstname"], row["lastname"])

    if (row["firstname"] == "Aysha"):
        row["firstname"] = "Alexander"