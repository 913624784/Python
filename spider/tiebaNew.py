#encoding=utf-8

import re,urllib,urllib2

class tieba():
    def spider(self,name,startPage,endPage):
        '''
        贴吧爬虫的主调度器
        :param name: 贴吧名
        :param startPage: 起始页
        :param endPage: 终止页
        :return:
        '''
        url = "http://tieba.baidu.com/f?ie=utf-8&"
        url += urllib.urlencode({"kw":name})
        print(url)
        for page in range(startPage,endPage+1):
            pn = 50 * (page-1)
            urlFull = url + "&"+ urllib.urlencode({"pn":pn})
            html = self.loadPage(urlFull,page)
            self.dealPage(html,page)



    def loadPage(self,url,page):
        '''
        爬取网页源代码
        :param url: 要爬取的地址
        :return: 返回爬取的源代码
        '''
        print "正在爬取第"+str(page)+"页数据。。。。"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }

        request = urllib2.Request(url, headers=header)

        response = urllib2.urlopen(request)

        html = response.read()

        return html

    def writePage(self,context,page):
        '''
        将爬取到的源代码写入文件
        :param html: 源代码
        :param page: 页数
        :return:
        '''
        print "正在将第"+str(page)+"页数据写入文件。。。"
        with open("neihanba.txt","a") as file:
            file.writelines(context+"\n")

    def dealPage(self,html,page):
        partten = re.compile(r'<a\s+rel="noreferrer"\s+href="/p/\d+"\s+title=".*?"\s+target="_blank"\s+class="j_th_tit\s+">(.*?)</a>',re.S)
        titleList = partten.findall(html)
        for title in titleList:
            self.writePage(title, page)

if __name__ == '__main__':
    name = raw_input("请输入贴吧名：")
    startPage = raw_input("请输入起始页：")
    endPage = raw_input("请输入终止页：")


    print "爬虫开始。。。"
    t = tieba()
    t.spider(name,int(startPage),int(endPage))
    print "爬取结束。。。。"

