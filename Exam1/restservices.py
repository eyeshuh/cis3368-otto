import requests
import json
import keys
import hello
import mysql.connector


#response = requests.get("http://http://api.open-notify.org/astros.json")
#print(response)

# print(response.json())
# response.text()
# response.content()

hero_response = requests.get("https://superheroapi.com/api/%s/69" % (keys.Keys.getsuperheroapikey()), verify=False)
print(hero_response)
print("\n\n")

json_hero_response = hero_response.json()
print(json_hero_response)
print("\n\n")

hero_name = json_hero_response["name"]
print("The hero's name is: %s" % (hero_name))
print("\n\n")

hero_powers = json_hero_response["powerstats"]
print(hero_powers)
print("\n\n")

hero_strength = hero_powers["strength"]
print("%s's strength is: %s" % (hero_powers, hero_strength))
print("\n\n")

# add this hero to the db

my_db = mysql.connector.connect(
    host="cis3368-otto.cey6ttufijmi.us-east-2.rds.amazonaws.com",
    user="eyeshuh",
    password="admin3368",
    database="CIS3368db"
)

db_cursor = my_db.cursor()

query = "INSERT INTO hero (name, strength) VALUES ('%s', '%s')" % (hero_name, hero_strength)

db_cursor.execute(query)
my_db.commit()
print(db_cursor.rowcount, "hero added")
