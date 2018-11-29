#encoding:utf-8

import time

from pymongo import MongoClient
from bson.objectid import ObjectId

client=MongoClient(host="localhost",port=27017)
db=client['dbdb']
col=db.number_139

# with open(r'F:\workdata\jibi\jilu.txt', 'r') as file:
#     count=int(file.readline())
# print(count)
# print(type(count))

# count=0
#
# for content in col.find().skip(count):
#     count+=1
#     id = content["_id"]
#     phone = content["number"]
#     print(phone)
#     time.sleep(1)
#     print(count)
#     with open(r'F:\workdata\jibi\jilu.txt', 'w') as file:
#             file.write(str(count))



def main():
    with open(r'F:\workdata\jibi\jilu.txt','r') as file:
        count=int(file.readline())
    print(count)
    for content in col.find().skip(count):
        count += 1
        id = content["_id"]
        phone = content["number"]
        print("id:{0}  phone:{1}".format(id,phone))
        time.sleep(1)
        print(count)
        with open(r'F:\workdata\jibi\jilu.txt','w') as file:
            file.write(str(count+1))

if __name__ == '__main__':
    main()
    time.sleep(1)