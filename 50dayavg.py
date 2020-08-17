import json
import pymongo
from bson import json_util
from pymongo import MongoClient

#Opens Connection to market.stocks mongoDB
connection = MongoClient()
db = connection['market']
collection = db.stocks

#Searches for everything in the database with a key of "50-Day Simple Moving Average" and a value between the user inputted numbers
def FiftyDayAvg(low, high):
    result = collection.find({"50-Day Simple Moving Average" : {"$gt" : float(low), "$lt" : float(high)}})
    for x in result:
        print(x)
    return result

#takes input from the user
def main():
    print("this function will return all files with a 50 day moving avg between the inputted numbers")
    low = input("input the low value: ")
    high = input("input the high value: ")
    print (FiftyDayAvg(low, high))

main()

