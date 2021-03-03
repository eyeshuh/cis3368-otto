# Aysha Alam
# 1822564
# Homework 2 - CIS 3368

import requests
import json
import mysql.connector


data_request = requests.get("https://api.propublica.org/congress/v1/bills/subjects/taxation.json", headers = {'X-API-Key': '5ItJh3Z1KOmu2yCRe0klswSzzdDq100ZCjzcedXq'})
print (data_request.json()['results'][0])




