import requests


def check_number():
    url = "https://https.60api.com/pc/userCenter/v2/beforeLoginVali?accountName=18505615375"
    headers ={'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9', 'authorization': 'null', 'cache-control': 'no-cache', 'from': 'PC', 'lang': 'zh', 'origin': 'https://www.bjex.com', 'pragma': 'no-cache', 'referer': 'https://www.bjex.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    page = requests.get(url, headers=headers).text
    print(page)
    return page

def save_success_number(number):
    with open("success_币君.txt", "a+")as f:
        f.write(str(number) + "\n")

def save_faile_number(number):
    with open("faile_币君.txt", "a+")as f:
        f.write(str(number) + "\n")

if __name__ == "__main__":
    check_number()
    # count = 0
    # with open("data16.txt")as f:
    #     while True:
    #         res = f.readline()
    #         if not res:
    #             break
    #         line = res[2:].replace("\n", "")
    #         print(line, count)
    #         count += 1
    #         result = check_number(line)
    #         if str(result).find("已存在")!=-1 :
    #             save_success_number(number=line)
    #         else:
    #             save_faile_number(number=line)
