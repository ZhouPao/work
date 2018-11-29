import requests
import json

# def send_sms(mobile):
#     url="http://www.bishijie.com/api/user/getSms?type=2&uuid=web_pc&mobile="+mobile
#     headers = {
#         "Host": "www.bishijie.com",
#         "Connection": "keep-alive",
#         "Pragma": "no-cache",
#         "Cache-Control": "no-cache",
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#         "X-Requested-With": "XMLHttpRequest",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
#         "Referer": "http://www.bishijie.com/kuaixun/",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "Cookie": "acw_tc=AQAAAAQGURW2xwEAuVARcFwdkmITNX9p; PHPSESSID=4ha06s31jk7k9qnrtg7cvr1t35; Hm_lvt_760519477a6dd9d6ef4ae6014436ab92=1529644618; Hm_lpvt_760519477a6dd9d6ef4ae6014436ab92=1529644618; __lnkrntdmcvrd=-1",
#     }

def check_number(number):
    headers = {
        "Host": "www.bishijie.com",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "acw_tc=AQAAAAQGURW2xwEAuVARcFwdkmITNX9p; PHPSESSID=4ha06s31jk7k9qnrtg7cvr1t35; Hm_lvt_760519477a6dd9d6ef4ae6014436ab92=1529644618; Hm_lpvt_760519477a6dd9d6ef4ae6014436ab92=1529644618; __lnkrntdmcvrd=-1",
        "Referer": "http://www.bishijie.com/kuaixun/",
    }
    url="http://www.bishijie.com/api/user/login?mobile="+str(number)+"&passwd=202cb962ac59075b964b07152d234b70&uuid=web_pc"

    page = requests.get(url, headers=headers).text
    print(page)
    return page


if __name__ == '__main__':
    check_number("13247785048")

