#encoding:utf-8
with open("请求头.txt")as f:
    res = f.readlines()
headers ={}
for r in res:
    headers[r.split(": ")[0]]=r.split(": ")[1].replace("\n","")
print(headers)


