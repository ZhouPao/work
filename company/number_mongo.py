# coding:utf-8
import pymongo
# from mongo_auto_id import getNextValue, getNextValue_SIX, getNextValue_BaFangZiYuan

# 导入自增函数
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.mynumberdb
dbdb = client['dbdb']
"""
# 有顺序的100多万数据，来自原始数据
auto_number = dbdb["auto_number"]
auto_number.ensure_index("number",unique=True)
# 原有数据
number_all= db.number_all
number_all.ensure_index("number",unique=True)
# whatsapp的六万数据
number_six = dbdb.number_six
number_six.ensure_index("number",unique=True)
"""
# 八方资源
number_BaFangZiYuan = dbdb.number_BaFangZiYuan
number_BaFangZiYuan.ensure_index("number",unique=True)

# ly72
# number_ly72 = dbdb.number_ly72
# number_ly72.ensure_index("number", unique=True)
if __name__ == "__main__":
    # pass
    with open("八方资源网电话号码.txt")as f:
        while True:
            res = f.readline()
            if not res:
                break
            number = res.replace("\n", "")
            print(number)
            number_BaFangZiYuan.insert_one({'_id': getNextValue_BaFangZiYuan("number"), "number": number})
    print(number_BaFangZiYuan.count())
    # for i in auto_number.find({"_id":1}):
    #     print(i)
    # for index ,i in enumerate(number_all.find(),1):
    #     print(index)
    #     auto_number.insert_one({'_id': getNextValue('number'), 'number':str(i["number"]).replace("\n","")})
