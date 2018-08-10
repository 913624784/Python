# -*- coding:utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup


class neihan():
    reload(sys)
    sys.setdefaultencoding("utf-8")

    def writeFile(self, page):
        '''
        将爬取出的内涵段子写入文件
        :param page:
        :return:
        '''
        fo = open("../out/neihan.txt", "a")
        fo.write(page + "\n")
        fo.close()

    def spider(self, startpage, endpage):
        '''
        爬取网站内容
        :return:
        '''
        user_agent = "Mozilla/5.0 (comptible:MSIE 9.0:Windows NT 6.1:Trident/5.0:)"
        headers = {"User-Agent": user_agent}

        for i in range(startpage, endpage + 1):
            url = "http://www.neihanpa.com/article/list_5_" + str(i) + ".html"
            re = requests.get(url, headers=headers)
            page = re.text.encode('iso-8859-1').decode('gbk')
            soup = BeautifulSoup(page, 'lxml')

            for j in range(1, 11):
                string = 'piclist' + str(j)
                t = soup.find(class_=string)
                title = t.find("h4").a.text
                print(title)
                content = t.find(class_="f18 mb20").text.strip()
                print(content)
                page = "title:" + title + "\ncontext:" + content + "\n"
                self.writeFile(page)
            print "第" + str(i) + "页爬取完毕"


if __name__ == '__main__':
    startpage = input("请输入爬取起始页：")
    endpage = input("请输入爬取终止页：")
    t = neihan()
    t.spider(startpage, endpage)
