#encoding:utf-8

import requests

def check_number(number):
    headers={
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer null",
        "fzm-request-os": "web",
        "fzm-request-uuid": "",
        # "fzm-user-ip": "112.17.125.192",
        "origin": "https://www.zhaobi.com",
        "referer": "https://www.zhaobi.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    url="https://zb2api.licai.cn/api/member/isreg?mobile="+str(
        number)+"&area=86&type=sms&email=&broker_code="
    # form_data = [
    #     ("mobile", number),
    #     ("area","86"),
    #     "type": "sms,",
    #     "email": "",
    #     "broker_code": "",
    # ]
    page = requests.get(url, headers=headers).text
    print(page)
    return page


# {"code":200,"ecode":"200","error":"OK","message":"OK","data":{"uid":199939,"ispwd":0}}

if __name__ == '__main__':
    check_number("13247785048")
