# -*- coding:utf-8 -*-
import requests
import pymongo
import json
from pymongo import MongoClient
client=MongoClient(host="localhost",port=27017)
#创建数据库
db=client['dbdb']
#创建集合
col=db.auto_number_two
import time
#     time.sleep(3)
count=0
def num(count):
    count = 0
    while True:
        with open(r"F:\sghwork\mynumber.txt")as f:
            count = int(f.read())
        for content in col.find({'_id': count}):
               # print (content)
            id = content["_id"]
            number=content["number"]
            print (number)
            return number
        count += 1
        with open(r"F:\sghwork\mynumber.txt", 'w')as f:
            f.write(str(count))
def judge(phone=num(count)):

    url = "https://i.btc.com/auth/api/register/mobile/start"
    formdata = {
        "captcha": "",
        "email": "+86|" + phone,
    }
    headers = {
        "Accept": "application / json, text / plain, * / *",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "zh - CN, zh;q = 0.9",
        "Connection": "keep - alive",
        "Content - Length": "40",
        "Content - Type": "application / json;charset = UTF - 8",
        "Cookie": "acw_tc = AQAAAAdDpD6YJw0AwH0RcDiK45QVsSEZ;lang = zh - cn;_ga = GA1.2.1860027226.1533105990;_gid = GA1.2.1482395113.1533105990;XSRF - TOKEN = eyJpdiI6InorS243SFdpMlRPMTk2N3J4a0dBSmc9PSIsInZhbHVlIjoiMVJESUlxMm5FUnZXXC8xSUY1SFg1K3c9PSIsIm1hYyI6ImUwODZkNWJmYTFkMjZjYTYxMTA2ODY5YjlhMGQwZTIwZWMzY2Y0NGMxMzYzNTVmOGE2MGU4NzE5ZmNkNzAxZDEifQ % 3D % 3D;laravel_session = eyJpdiI6IjBRNWV4aWhwVzNWcHBlSkh5NGQyRlE9PSIsInZhbHVlIjoibGNsNGpkdDl6N3hFNmNYRHFhdW8yXC9rN1JvZnJYRkp3MGhrK0ltWGJLTnJYUXRjemNjaWJLSzNWWm9Hbjg0RGJ5WDFiMUNmRWNyZ0xZWkYzT04xQlFBPT0iLCJtYWMiOiJjYjY4ZjlmYWRjYjU3OGM5M2NlNzViMDhlY2IxZWQ1NzM5MTBhYjQyMzJkZGMyMjQ5MjUwMzM1NWQyYTk3OGYzIn0%3D",
        "Host": "i.btc.com",
        "Origin": "https: // i.btc.com",
        "Referer": "https: // i.btc.com / auth",
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.62Safari / 537.36",
        "X - XSRF - TOKEN": "eyJpdiI6InorS243SFdpMlRPMTk2N3J4a0dBSmc9PSIsInZhbHVlIjoiMVJESUlxMm5FUnZXXC8xSUY1SFg1K3c9PSIsIm1hYyI6ImUwODZkNWJmYTFkMjZjYTYxMTA2ODY5YjlhMGQwZTIwZWMzY2Y0NGMxMzYzNTVmOGE2MGU4NzE5ZmNkNzAxZDEifQ ==",
    }
    content = requests.post(url, headers=headers, data=formdata).text
    print(content)
    if content.find("user identifier exists") != -1:
        print("手机号已被注册")
        url = "http://122.114.183.102:8080/saveNumber/{0}/".format(phone, )
        print(requests.get(url).text)
        with open(r"F:\sghwork\btc1_phone.txt", "a")as f:
            f.write(phone + "\n")
            f.close()
    elif content.find("user identifier exists") == -1:
        print("手机号未被注册")
        with open(r"F:\sghwork\btc1_unphone.txt", "a")as f:
            f.write(phone + "\n")
            f.close()

if __name__ == "__main__":
    num(0)
    judge()
    # count = 0
    # while True:
    #     with open(r"F:\sghwork\mynumber.txt")as f:
    #         count = int(f.read())
    #     for content in col.find({'_id': count}):
    #            # print (content)
    #         id = content["_id"]
    #         number=content["number"]
    #         print (number)
    #     count += 1
    #     with open(r"F:\sghwork\mynumber.txt", 'w')as f:
    #         f.write(str(count))

    #     time.sleep(3)
    #     for content in col.find({'_id': count}):
    #            # print (content)
    #         id = content["_id"]
    #     count += 1
    #     with open(r"F:\sghwork\mynumber.txt", 'w')as f:
    #         f.write(str(count))
    # id=content["_id"]
    # print (id)
    # number=content["number"]
    # print (number)

# res=col.find()
# c=res.find('_id',)
# number=c['_id']

# def judge(phone):
#     url="https://i.btc.com/auth/api/register/mobile/start"
#     formdata = {
#         "captcha": "",
#         "email":  "+86|"+phone,
#     }
#     headers={
#         "Accept": "application / json, text / plain, * / *",
#         "Accept - Encoding": "gzip, deflate, br",
#         "Accept - Language": "zh - CN, zh;q = 0.9",
#         "Connection": "keep - alive",
#         "Content - Length": "40",
#         "Content - Type": "application / json;charset = UTF - 8",
#         "Cookie": "acw_tc = AQAAAAdDpD6YJw0AwH0RcDiK45QVsSEZ;lang = zh - cn;_ga = GA1.2.1860027226.1533105990;_gid = GA1.2.1482395113.1533105990;XSRF - TOKEN = eyJpdiI6InorS243SFdpMlRPMTk2N3J4a0dBSmc9PSIsInZhbHVlIjoiMVJESUlxMm5FUnZXXC8xSUY1SFg1K3c9PSIsIm1hYyI6ImUwODZkNWJmYTFkMjZjYTYxMTA2ODY5YjlhMGQwZTIwZWMzY2Y0NGMxMzYzNTVmOGE2MGU4NzE5ZmNkNzAxZDEifQ % 3D % 3D;laravel_session = eyJpdiI6IjBRNWV4aWhwVzNWcHBlSkh5NGQyRlE9PSIsInZhbHVlIjoibGNsNGpkdDl6N3hFNmNYRHFhdW8yXC9rN1JvZnJYRkp3MGhrK0ltWGJLTnJYUXRjemNjaWJLSzNWWm9Hbjg0RGJ5WDFiMUNmRWNyZ0xZWkYzT04xQlFBPT0iLCJtYWMiOiJjYjY4ZjlmYWRjYjU3OGM5M2NlNzViMDhlY2IxZWQ1NzM5MTBhYjQyMzJkZGMyMjQ5MjUwMzM1NWQyYTk3OGYzIn0%3D",
#         "Host": "i.btc.com",
#         "Origin": "https: // i.btc.com",
#         "Referer": "https: // i.btc.com / auth",
#         "User - Agent": "Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.62Safari / 537.36",
#         "X - XSRF - TOKEN": "eyJpdiI6InorS243SFdpMlRPMTk2N3J4a0dBSmc9PSIsInZhbHVlIjoiMVJESUlxMm5FUnZXXC8xSUY1SFg1K3c9PSIsIm1hYyI6ImUwODZkNWJmYTFkMjZjYTYxMTA2ODY5YjlhMGQwZTIwZWMzY2Y0NGMxMzYzNTVmOGE2MGU4NzE5ZmNkNzAxZDEifQ ==",
#     }
#     content=requests.post(url,headers=headers,data=formdata).text
#     print (content)
#     if content.find("user identifier exists")!=-1:
#         print("手机号已被注册")
#         url="http://122.114.183.102:8080/saveNumber/{0}/".format(phone,)
#         print(requests.get(url).text)
#         with open(r"F:\sghwork\btc1_phone.txt", "a")as f:
#             f.write(phone + "\n")
#             f.close()
#     elif content.find("user identifier exists") == -1:
#         print("手机号未被注册")
#         with open(r"F:\sghwork\btc1_unphone.txt", "a")as f:
#             f.write(phone + "\n")
#             f.close()
# judge('15890954093')
# 13247785048
# {"err_no":1011,"err_msg":"user identifier not exists","errors":null}