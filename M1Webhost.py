#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import route, run, request, abort
import datetime
import CRUD
import pymongo
from pymongo import MongoClient


#set up URL paths for REST service

#creates a new stock based on inputted JSON
@route('/stocks/api/v1.0/createStock/<newTicker>', method = 'POST')
def post_createStock(newTicker):
    postData = request.body.read()
    print(str(newTicker) + " " + str(postData))
    input_dict = json.loads(postData)
    print (input_dict)
    CRUD.create(input_dict)

#searches for a stock based on inputted ticker name
@route('/stocks/api/v1.0/getStock/<tickerName>', method = 'GET')
def get_getStock(tickerName):
    query = "{\"Ticker\" :" + "\"" + tickerName + "\"}" 
    result = CRUD.read(query)
    return json.dumps(result, default=str)

#updates stock with specified ticker name with inputted JSON values
@route('/stocks/api/v1.0/updateStock/<tickerName>', method = 'POST')
def get_updateStock(tickerName):
    postData = request.body.read()
    query = "{\"Ticker\" :" + "\"" + tickerName + "\"}"
    input_dict = json.loads(postData)
    input_dict2 = json.loads(query)
    CRUD.update(input_dict2, input_dict)

#deletes stock with specified ticker name
@route('/stocks/api/v1.0/deleteStock/<tickerName>', method = 'GET')
def get_delete(tickerName):
    query = "{\"Ticker\" :" + "\"" + tickerName + "\"}" 
    CRUD.delete(query)

#returns stocks with user inputted lists of tickers
@route('/stocks/api/v1.0/stockReport', method = 'POST')
def stockReport():
    postData = request.body.read()
    queryElements = []
    input_dict = json.loads(postData)
    for x in input_dict:
        queryString = "{\"Ticker\" : \"" + str(x) + "\"}"
        print (queryString)
        CRUD.read(queryString)

#returns top5 stocks in the user inputted industry
@route('/stocks/api/v1.0/industryReport/<industry>', method = 'GET')
def industryReport(industry):
    connection = MongoClient()
    db = connection['market']
    collection = db.stocks
    queryString = "{\"Industry\" : \"" + industry + "\"}"
    query = json.loads(queryString)
    print(query)
    results = collection.find(query).limit(5)
    for x in results:
        print(x)

if __name__ == '__main__':
    #app.run(debug=True)
    run(host='localhost', port=8080)
