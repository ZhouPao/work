from pymongo import MongoClient
from bson.objectid import ObjectId
import re

connection=MongoClient('localhost',27017)
dbdb=connection['dbdb']
# print(dbdb.auto_number.find({"_id":{"$gte":836001}}).count())

list=[]
for user in dbdb.auto_number.find({"_id":{"$gte":836020}}):
    print(user)
    list.append(user)
    # for key,value in user:
    #     print()

list0=list[:5]
print(list0)
for i in range(len(list0)):
    print(list0[i])
    # for j in range(len(list0[i])):
    for key,value in list0[i].items():
        print(value)



# with open('number.txt','wb') as f:
#     for user in dbdb.auto_number.find({"_id":{"$gte":836020}}):
#         print(user)
#         print(type(user))


# def mongo_list(num_list):
#     print(dbdb.auto_number.find({"_id":{"$gte":836001}}).count())
    # for user in dbdb.auto_number.find({"_id":{"$gte":836001}}):
    #     print(user)


# collections=dbdb.collection
# print(collections)
# num=collections["auto_number"]
# print(num)
# print(num.find({"_id":836001}))

# def conn_mongodb():
#     try:
#         pass
#     except

