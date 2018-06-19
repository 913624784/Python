import requests,lxml
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (comptible:MSIE 9.0:Windows NT 6.1:Trident/5.0:)"
headers = {"User-Agent":user_agent}
url = "https://www.qiushibaike.com/"
re = requests.get(url,headers = headers)
soup = BeautifulSoup(re.text,'lxml')
mlist = soup.find_all(class_ = 'content')

for li in mlist:
    if li.find_all(class_ = 'thumb'):
        continue
    div = li.span.get_text()
    print(div)
    print("--------------------------------------------------------")
