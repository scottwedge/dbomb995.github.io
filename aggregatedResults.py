import json
import pymongo
from bson import json_util
from pymongo import MongoClient
#Opens Connection to MongoDB market.stocks
connection = MongoClient()
db = connection['market']
collection = db.stocks

#Queries for user inputted sector, then aggragates those displaying the Industries of the results and number of companies that are listed under those industries 
def search(sector):
    result = collection.aggregate([{"$match": {"Sector" : str(sector)}}, {"$group" : {"_id" : "$Industry", "count" : {"$sum": 1}}}])
    for x in result:
        print (x)
    return result

#Asks user for input
def main():
    sector = input("input Sector: ")
    print (search(sector))

main()

