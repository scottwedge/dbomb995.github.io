import json
import pymongo
from bson import json_util
from pymongo import MongoClient

#Opens connection to market.stocks MongoDB
connection = MongoClient()
db = connection['market']
collection = db.stocks

#Displays options for the user to select from when the menu() function is called
def option():
    print("")
    print("*" * 20)
    print("1: Create \n2: Read \n3: Update \n4: Delete \n5: Exit ")
    print("*" * 20)
    val = input("Select an option: ")
    return val

#converts JSON formatted strings to type JSON
def stringToJson(str1):
        JSON1 = json.loads(str1)
        return JSON1

#takes JSON formatted strings as input
def JSONinput():
    str1 = input("Please enter JSON formatted text: ")
    return str1

def create(input1):
    #if create() function is called from the menu() function then the function asks the user for input and creates a file based on user input
    if(input1 == ""):
        #takes json formatted string and creates a document
        try:
            print("You have selected to Create a new entry in the database ", end = '')
            result = collection.insert_one(stringToJson(str(JSONinput())))
            return result
        except:
            print("an error occurred during creation please try again")
            return ""
    #if create() function is passed a non-null argument creates file based on input
    else:
        result = collection.insert_one(input1)
        return result

def read(input1):
    #takes json formatted string and queries a document
    #If read function is called with an empty string passed then asks the user for input to search for
    if(input1 == ""):        
        try:
            print("You have selected to query an entry in the database ", end = '')
            result = collection.find(stringToJson(str(JSONinput())))
            for x in result:
                print (x)
            return result
        except:
            print("an error occurred during the read process please try again")
            return ""
    #if read() is called with a non-empty string searches for a file based on the passed parameters
    else:
        result = collection.find(stringToJson(str(input1)))
        value= {}
        for x in result:
            value.update(x)
            #print(x)
            continue
        return value
        
def update(input1, input2):
    #takes json formatted string and updates a document
    #if input1 and input2 are both empty asks the user for input
    if(input1 == "" and input2==""):
        try:
            print("You have selected to update an entry in the database ")
            print("Entry to be updated")
            oldData = stringToJson(str(JSONinput()))
            print("NEW DATA")
            newData = stringToJson(str(JSONinput()))
            result = collection.update(oldData, newData)
            return result
        except:
            print("an error occurred during the update process please try again")
            return ""
    #if input1 and input2 both =1 then function asks for a ticker symbol to search for and update
    elif(input1 == "1" and input2 == "1"):
        print("You have selected to update an entry in the database ")
        ticker = input("enter ticker symbol to update: ")
        tickerSymbolString = "{\"Ticker\" : " + "\"" + ticker + "\"} "
        tickerJson = stringToJson(tickerSymbolString)
        volume = input("enter volume amount: ")
        volumeString = "{\"Volume\" : " + "\"" + volume + "\"} "
        volumeJson = stringToJson(volumeString)
        result = collection.update(tickerJson, volumeJson)
        return result
    #if input1 and input2 are both non-empty & != 1 then function will update based on JSON formatted strings
    else:
        result = collection.update(input1, input2)
        return result

def delete(input1):
    #takes json formatted string and deletes a document
    #if input is empty asks the user for input then searches and deletes based on user input
    if(input1 == "1"):        
        try:
            print("You have selected to delete a new entry in the database ", end = '')
            result = collection.remove(stringToJson(str(JSONinput())))
            return result
        except:
            print("an error occurred during the deletion process please try again")
    #if input is = 1 then asks the user for a ticker symbol to search for and delete
    elif(input1 == ""):
        ticker = input("Please enter the ticker symbol of the entry you would like to delete: ")
        #tickerJson = stringToJson("{\"Ticker\" : \"" + ticker + "\"}" )
        tickerJson = print("{\"Ticker\" : \"" + ticker + "\"}" )
        result = collection.remove(tickerJson)
        return result
    #if input is non-empty and !=1 takes JSON formatted input and deletes an object
    else:
        result = collection.remove(stringToJson(str(input1)))
        return result

def displayALL():
        #Displays all entries in a database (Not Listed in menu)
        result = collection.find()
        for x in result:
            print (x)

def menu():
        #asks the user to choose an option
        loop = "x"
        while(loop == "x"):
            val = option()
            #calls create()
            if(val == "1"):
                print(create(""))
            #calls read()
            elif(val == "2"):
                print(read(""))
            #calls update()
            elif(val =="3"):
                print(update("1", "1"))
            #calls delete()
            elif(val == "4"):
                print(delete("1"))
            #exits loop
            elif(val == "5"):
                loop = "y"
            #calls displayALL()
            elif(val == "6"):
                displayALL()
            #catches values not previously listed
            else:
                print("Please Enter appropriate value")
#def main():
#   menu()

#main()
