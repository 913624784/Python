# encoding=utf-8

import urllib
import requests
import sys
from bs4 import BeautifulSoup


class zhilian():
    reload(sys)
    sys.setdefaultencoding("utf-8")

    def writeFile(self, infom):
        '''
        将公司信息写入文件
        :param infom:
        :return:
        '''

        fo = open("../out/zhilian.txt", "a")
        fo.write(infom + "\n")
        fo.close()

    def spider(self, work, address, startPage, endPage):
        '''
        爬取公司信息及二次爬取
        :param work:
        :param address:
        :param startPage:
        :param endPage:
        :return:
        '''
        user_agent = "Mozilla/5.0 (comptible:MSIE 9.0:Windows NT 6.1:Trident/5.0:)"
        headers = {"User-Agent": user_agent}
        for page in range(startPage, endPage + 1):
            url = "http://sou.zhaopin.com/jobs/searchresult.ashx?{}&{}&sm=0&{}" \
                .format(urllib.urlencode({"jl": address}), urllib.urlencode({"kw": work}),
                        urllib.urlencode({"p": page}))
            re = requests.get(url, headers=headers)

            soup = BeautifulSoup(re.text, "lxml")
            mlist = soup.find_all("table", {'cellpadding': '0'})
            for i in mlist:
                try:
                    href = i.find(class_="zwmc").a.get("href")
                    name = i.find(class_="gsmc").text
                    re = requests.get(href, headers=headers)
                    sou = BeautifulSoup(re.text, "lxml")
                    slist = sou.find_all("li")
                    money = slist[9].strong.text
                    exp = slist[13].strong.text
                    print(slist)
                    infom = name + "  " + money + "   " + exp
                    self.writeFile(infom)
                except:
                    print "no"


if __name__ == '__main__':
    '''
    work = raw_input("请输入职位名称：")
    address = raw_input("请输入工作地址：")
    startPage = raw_input("请输入起始页：")
    endPage = raw_input("请输入终止页：")
    '''

    zh = zhilian()
    zh.spider("大数据开发工程师", "杭州", 1, 1)
# zh.spider(work,address,int(startPage),int(endPage))
