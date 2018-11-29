from pymongo import MongoClient
from bson.objectid import ObjectId

connection=MongoClient('localhost',27017)
dbdb=connection['dbdb']
print(dbdb.auto_number.find({"_id":{"$gte":836001}}).count())
# collection.find_one({‘_id‘:ObjectId(‘50f0d76347f4ec148890ef1e‘)})
print(dbdb.auto_number.find({"_id":836001}))
curson=dbdb.auto_number.find({"_id":836001})
for c in curson:
    print(c['number'])

list=[]
for user in dbdb.auto_number.find({"_id":{"$gte":836020}}):
    # print(user)
    list.append(user)

list0=list[:5]
print(list0)
for i in range(len(list0)):
    print(list0[i])
    # print(list0.get('number'))
    for key,value in list0[i].items():
        print(value)