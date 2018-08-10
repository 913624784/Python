# encoding=utf-8
import re, urllib2


class neihanba():
    def inter(self, startPage, endPage):
        url = "http://www.neihanpa.com/article/list_5_"
        for page in range(startPage, endPage + 1):
            urlFull = url + str(page) + ".html"
            html = self.loadPage(urlFull, page)
            self.dealPage(html, page)

    def loadPage(self, url, page):
        print "正在爬取第" + str(page) + "页数据。。。。"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        request = urllib2.Request(url, headers=header)
        response = urllib2.urlopen(request)
        html = response.read()

        return html

    def writePage(self, context, page):
        print "正在将第" + str(page) + "页数据写入文件。。。"
        with open("../out/neihanba.txt", "a") as file:
            file.writelines(context + "\n")

    def dealPage(self, html, page):
        # 先把li标签里的内容爬出来
        partten = re.compile('<li class="piclist\d+">(.*?)</li>', re.S)
        titleList = partten.findall(html)
        for li in titleList:
            # 标题的正则
            li_title = re.compile('<a href="/article/\d+.html">(.*?)</a>', re.S)
            title = li_title.findall(li)
            for t in title:
                fin_title = t.replace("<b>", "").replace("</b>", "")
                fin = "Title:" + fin_title
                self.writePage(fin, page)

            # 内容的正则
            li_context = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)
            context = li_context.findall(li)
            for c in context:
                fin_context = c.replace("<p>", "").replace("</p>", "").replace("<br>", "") \
                    .replace("<br />", "").replace("&ldquo", "").replace("&rdquo", "") \
                    .replace("&hellip", "").replace(' ', '')
                fin = "Context:" + fin_context.strip() + "\n\n"
                self.writePage(fin, page)


if __name__ == '__main__':
    startPage = raw_input("请输入爬虫的起始页：")
    endPage = raw_input("请输入爬虫的终止页：")
    n = neihanba()
    n.inter(int(startPage), int(endPage))
