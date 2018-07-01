# encoding=utf-8
import requests
from bs4 import BeautifulSoup

url = 'http://www.qianlima.com/zb/area_305/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': user_agent}
r = requests.get(url, headers=headers)  # 连接
content = r.text  # 获取内容，自动转码unicode
soup = BeautifulSoup(content, "lxml")
#tags1 = soup.select('div .shixian_zhaobiao')
ts=soup.find_all('div',{'class':'shixian_zhaobiao'})
tag1 = ts[0]#第一个div标签
tag2 = tag1.find(name='dl')
tag3 = tag2.find_all(name='dt')
for i in tag3:
    name=i.a.text
    date = tag2.find("dd").string
    her =i.a.get("href")
    print name+" "+date+" "+her