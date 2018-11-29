# coding:utf-8
import requests
# from 短信轰炸.number_mongo import number_six
# from number_mongo import number_BaFangZiYuan
# ###403 Forbidden


def check_number(number):
    headers = {'Host': 'bixin.com', 'Connection': 'keep-alive', 'Content-Length': '115', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Origin': 'https://bixin.com', 'Upgrade-Insecure-Requests': '1',
               'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Referer': 'https://bixin.com/auth/forget/', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'csrftoken=GAt6OL6mLdlUNNek6x6xO9jEJ11hhUEARCsVgxhooAFRvpLCdcf8G9KXCoHeN0MC; browser=SvUqX_bRFyDsOyuVIQygsg; djlanguage=zh-hans; country=cn; sessionid=9m13e5h7os73et3u21ogu6br6cp0t67l'}
    url = "https://bixin.com/auth/forget/"
    form_data = [
        ('csrfmiddlewaretoken', "Hh23K66MVecpgwJcIIJQlnaGGl1FjZYkSj1ScShOyBwmY8guPnSrdnBZzIHCP56m"),
        ('account', "+86" + str(number)),
        ('code', ""),
    ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page


def save_success_number(number):
    with open("success_币信.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币信.txt", "a+")as f:
        f.write(str(number) + "\n")


if __name__ == "__main__":
    check_number("13247785048")
    # count = 0
    # while True:
    #     try:
    #         with open("flag_币信.txt")as f:
    #             count = int(f.read())
    #         for res in number_BaFangZiYuan.find({'_id': count}):
    #             line = res["number"].replace("\n", "")
    #             print(line, count)
    #             count += 1
    #             result = check_number(line)
    #             if str(result).find("无法重置密码") != -1:
    #                 save_success_number(number=line)
    #             else:
    #                 save_faile_number(number=line)
    #         with open("flag_币信.txt", "w")as f:
    #             f.write(str(count))
    #     except:
    #         pass
"""
<div id="account_error" class="line-alert text-danger" >
        未找到该用户
</div>
        无法重置密码
"""
