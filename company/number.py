#encoding:utf-8
from pymongo import MongoClient
from bson.objectid import ObjectId

connection=MongoClient('localhost',27017)
dbdb=connection['dbdb']
curson=dbdb.auto_number.find({"_id":836001})
for c in curson:
    print(c['number'])