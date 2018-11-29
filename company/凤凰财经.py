# coding:utf-8
import requests
# from 短信轰炸.number_mongo import auto_number
# from number_mongo import number_BaFangZiYuan


def check_number(number):
    headers = {'Host': 'id.ifeng.com', 'Connection': 'keep-alive', 'Content-Length': '13', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache',
               'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
               'Origin': 'https://id.ifeng.com', 'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://id.ifeng.com/user/register/', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'prov=cn0571; city=0571; weather_city=zj_hz; region_ip=112.17.80.185; region_ver=1.30; userid=1529750058337_vox3je229; PHPSESSID=m9eagvmu71u9jolgkg4p2sl3n7'}
    url = "https://id.ifeng.com/api/checkMobile?callback=jQuery18306705617574472242_1529750071632"
    form_data = [('u', str(number)), ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(page)
    return page


def save_success_number(number):
    with open("success_凤凰财经.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_凤凰财经.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":
    check_number(18505615377)
    # for i in number_six.find({"number":"13609681999"}):
    #     print(i)
    # count = 0
    # while True:
    #     try:
    #         with open("flag_凤凰财经.txt")as f:
    #             count = int(f.read())
    #         for res in number_BaFangZiYuan.find({'_id': count}):
    #             line = res["number"].replace("\n", "")
    #             print(line, count)
    #             count += 1
    #             result = check_number(line)
    #             if str(result).find("3002") != -1:
    #                 save_success_number(number=line)
    #                 save(number=line)
    #             else:
    #                 save_faile_number(number=line)
    #         with open("flag_凤凰财经.txt", "w")as f:
    #             f.write(str(count))
    #     except:
    #         pass
# (function(){var JsonVarStr___={"code":0,"message":"\u624b\u673a\u53f7\u4e0d\u5b58\u5728","msgcode":"3001","data":{"res":"121"}}; jQuery18306705617574472242_1529750071632(JsonVarStr___);})();
# (function(){var JsonVarStr___={"code":1,"message":"\u624b\u673a\u53f7\u5df2\u5b58\u5728","msgcode":"3002","data":{"res":"122"}}; jQuery18306705617574472242_1529750071632(JsonVarStr___);})();
"""
13609681986 5885
(function(){var JsonVarStr___={"code":0,"message":"\u624b\u673a\u53f7\u4e0d\u5b58\u5728","msgcode":"3001","data":{"res":"121"}}; jQuery18306705617574472242_1529750071632(JsonVarStr___);})();
13609681999 5886
"""
