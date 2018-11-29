import time

from pymongo import MongoClient
from bson.objectid import ObjectId

client=MongoClient(host="localhost",port=27017)
db=client['dbdb']
col=db.number_139

# print(col.count())

# print(col.find({'_id':ObjectId}))

for content in col.find({'_id':ObjectId('5b4b40d3e6ba1b31105ce956')}):
    id = content["_id"]
    phone = content["number"]
    print("id{0}:phone{1}".format(id,phone))
count=0

for content in col.find():
    id = content["_id"]
    phone = content["number"]
    print("id{0}:phone{1}".format(id,phone))
    count=count+1
    print(count)
    with open('jilu.txt','w') as file:
        file.write(phone)
    time.sleep(2)

