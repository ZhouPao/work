#coding:utf-8
import requests
# from 短信轰炸.number_mongo import auto_number
from number_mongo import number_BaFangZiYuan


def check_number(number):
    headers = {'Host': 'u.caixin.com', 'Connection': 'keep-alive', 'Content-Length': '19', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://u.caixin.com', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://u.caixin.com/user/register.html', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'CX_FROM=null; GUID=1893157932; T_GUID=1529746051313; GID30=1893157932; point=1529769599000; gr_user_id=2cfe9d58-9ce7-42fb-adff-27bfbde8c8bd; 872f3eaac31f373e_gr_session_id=5d892590-6e7c-4f7a-aac9-a75c7fb3f964_true; JSESSIONID=FB4FBCF3352B4685CB3CEA3867A66A97; CAIXIN_UUID=898e803f1f89412fb2273e2fbb6c2d46; backUrl=http%3A//u.caixin.com/user/register.html; ENTITY_ID=register; ENTITY_COUNT=1; lastTime=1529746053063; firstTime=1529746053063; gr_session_id_872f3eaac31f373e=ebfc4202-4eab-4bb6-9ad0-ca8c2eda1125_true'}
    url = "http://u.caixin.com/user/check_mobile.json"
    form_data = [('account', str(number)),]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page
def save_success_number(number):
    with open("success_财新网.txt", "a+")as f:
        f.write(str(number) + "\n")
def save_faile_number(number):
    with open("faile_财新网.txt", "a+")as f:
        f.write(str(number) + "\n")
if __name__=="__main__":
    count = 1
    while True:
        with open("flag_财新网.txt")as f:
            count = int(f.read())
        for res in number_BaFangZiYuan.find({'_id': count}):
            line = res["number"].replace("\n", "")
            print(line, count)
            count += 1
            result = check_number(line)
            if str(result).find('"exists":"1"') != -1:
                save_success_number(number=line)
            else:
                save_faile_number(number=line)
        with open("flag_财新网.txt", "w")as f:
            f.write(str(count))
# {"success":true,"err_code":"0","data":{"exists":"0"}}
# {"success":true,"err_code":"0","data":{"exists":"1"}}

