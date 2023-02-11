from urllib.error import HTTPError
import requests
import os
def writein(s,Path):
    if os.path.isfile(Path):
        with open(Path,'w+',encoding='utf-8') as f1:
            f1.write(s)
            return True
    return False

def httpget(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding= response.apparent_encoding
    except HTTPError as e:
        print(e)
    else:
        return response.text

print('请输入网址和目录:')
s = input()
s1 = s.split(' ')
html = str(s1[0])
path = str(s1[1])
httprd = httpget(html)
if writein(httprd,path):
    print('文件已写入')
else:
    print('文件写入失败')