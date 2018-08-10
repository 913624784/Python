# encoding=utf-8
import requests
from bs4 import BeautifulSoup

url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&sm=0&p=1'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': user_agent}
r = requests.get(url, headers=headers)  # 连接
content = r.text  # 获取内容，自动转码unicode
soup = BeautifulSoup(content, "lxml")
tags1 = soup.select('div .newlist_list_content')
tag1 = tags1[0]#第一个div标签
tag2 = tag1.find_all(name='table')
tags2 = tag2.find_all(name='tbody')
tags3=tags2.find_all(name='a')

for tag in tags3:
    print tag.get('href')
    print tag.string
    print tag.next_element.next_element.string